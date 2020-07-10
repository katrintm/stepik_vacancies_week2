from django.contrib.auth import login, authenticate
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from jobs.choices import StatusChoices, GradeChoices
from jobs.forms import ApplicationForm, CompanyForm, VacancyForm, ResumeForm
from jobs.forms import SignupForm
from jobs.models import Application, Resume
from jobs.models import Company
from jobs.models import Speciality
from jobs.models import Vacancy

from datetime import date


class MainView(View):
    def get(self, request):
        specialities = Speciality.objects.all().\
            annotate(count=Count('vacancies'))
        companies = Company.objects.all().annotate(count=Count('vacancies'))
        return render(
            request, 'index.html', context={
                'specialities': specialities,
                'companies': companies
            }
        )


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'vacancies.html', context={
                'vacancies': vacancies,
                'title': 'Все вакансии',
                'word_for_vacancies': word_for_vacancies
            }
        )


class CategoryVacanciesView(View):
    def get(self, request, category):
        try:
            speciality = Speciality.objects.get(code=category)
        except Speciality.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        vacancies = Vacancy.objects.filter(speciality=speciality)
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'vacancies.html', context={
                'vacancies': vacancies,
                'title': speciality.title,
                'word_for_vacancies': word_for_vacancies
            }
        )


class CompanyView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        vacancies = Vacancy.objects.filter(company=company)
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'company.html', context={
                'company': company,
                'vacancies': vacancies,
                'word_for_vacancies': word_for_vacancies
            }
        )


class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        company = Company.objects.get(id=vacancy.company.id)
        form = ApplicationForm()

        return render(
            request, 'vacancy.html', context={
                'vacancy': vacancy,
                'company': company,
                'form': form
            }
        )

    def post(self, request, vacancy_id):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.vacancy = Vacancy.objects.get(id=vacancy_id)
            form.user = request.user if request.user.is_authenticated else None
            form.save()
            return redirect(f'/vacancies/{vacancy_id}/send/')

        return render(
            request, 'vacancy.html',
            context={
                'form': form
            }
        )


class CompaniesView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(
            request, 'companies.html', context={
                'companies': companies
            }
        )


class VacancySendView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        return render(
            request, 'sent.html', context={
                'vacancy': vacancy
            }
        )


class MyCompanyView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user)
            form = CompanyForm(instance=company)
            return render(
                request, 'company_edit.html', context={
                    'company': company,
                    'form': form
                }
            )
        except Company.DoesNotExist:
            return render(
                request, 'company_not_found.html', context={
                }
            )

    def post(self, request):
        current_user = request.user
        company = Company.objects.get(owner=current_user)

        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            form = form.save(commit=False)
            form.owner = current_user
            form.save()
            return redirect('/mycompany/')
        else:
            form = CompanyForm(instance=company)

        return render(
            request, 'company_edit.html',
            context={
                'form': form,
                'company': company
            })


class MyCompanyCreateView(View):
    def get(self, request):

        form = CompanyForm()

        return render(
            request, 'company_create.html', context={
                'form': form
            }
        )

    def post(self, request):
        if request.method == "POST":
            form = CompanyForm(request.POST)
            print(form.is_valid(), form.errors)
            if form.is_valid():
                form = form.save(commit=False)
                form.owner = request.user
                form.logo = 'https://place-hold.it/130x80'
                form.save()
                return redirect('/mycompany/', pk=form.pk)
        else:
            form = CompanyForm()
        return render(request, 'company_create.html', {'form': form})


class MyCompanyVacanciesView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user)
        except Company.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        vacancies = Vacancy.objects.filter(company=company)
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'vacancies_list.html', context={
                'company': company,
                'vacancies': vacancies,
                'title': 'Все вакансии',
                'word_for_vacancies': word_for_vacancies
            }
        )


class MyCompanyVacancyView(View):
    def get(self, request, vacancy_id):
        try:
            company = Company.objects.get(owner=request.user)
        except Company.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )

        if Vacancy.objects.get(id=vacancy_id).company == company:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            specialities = Speciality.objects.all()
            applications = Application.objects.filter(vacancy=vacancy)

            form = VacancyForm(instance=vacancy)

            return render(
                request, 'vacancy_edit.html', context={
                    'company': company,
                    'vacancy': vacancy,
                    'specialities': specialities,
                    'applications': applications,
                    'form': form
                }
            )

        else:
            return render(
                request, '404.html', context={
                }
            )

    def post(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        company = Company.objects.get(owner=request.user)

        form = VacancyForm(request.POST, instance=vacancy)

        if form.is_valid():
            form = form.save(commit=False)
            form.company = company
            form.save()
            return redirect(f'/mycompany/vacancies/{vacancy_id}')
        else:
            form = VacancyForm(instance=vacancy)

        applications = Application.objects.filter(vacancy=vacancy)

        return render(
            request, 'vacancy_edit.html',
            context={
                'applications': applications,
                'company': company,
                'form': form,
                'vacancy': vacancy,
            }
        )


class MyCompanyVacancyCreateView(View):
    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user)
        except Company.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        form = VacancyForm()
        return render(
            request, 'vacancy_create.html', context={
                'company': company,
                'form': form
            }
        )

    def post(self, request):
        if request.method == "POST":
            form = VacancyForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.owner = request.user
                form.published_at = date.today()
                form.company = Company.objects.get(owner=request.user)
                form.save()
                return redirect('/mycompany/vacancies/', pk=form.pk)
        else:
            form = VacancyForm()
        return render(request, 'vacancy_create.html', {'form': form})


class ResumeView(View):
    def get(self, request):
        try:
            resume = Resume.objects.get(user=request.user)
            form = ResumeForm(instance=resume)
            return render(
                request, 'resume_edit.html', context={
                    'resume': resume,
                    'form': form
                }
            )
        except Resume.DoesNotExist:
            return render(
                request, 'resume_not_found.html', context={
                }
            )

    def post(self, request):
        current_user = request.user
        resume = Resume.objects.get(user=current_user)

        form = ResumeForm(request.POST, instance=resume)
        print(form.is_valid(), form.errors)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = current_user
            form.save()
            return redirect('/myresume/')
        else:
            form = ResumeForm(instance=resume)

        return render(
            request, 'resume_edit.html',
            context={
                'form': form,
                'resume': resume
            })


class ResumeCreateView(View):
    def get(self, request):

        form = ResumeForm()

        return render(
            request, 'resume_create.html', context={
                'form': form
            }
        )

    def post(self, request):
        if request.method == "POST":
            form = ResumeForm(request.POST)
            print(form.is_valid(), form.errors)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('/myresume/', pk=form.pk)
        else:
            form = ResumeForm()
        return render(request, 'resume_create.html', {'form': form})


class UserResumeView(View):
    def get(self, request, user_id):
        try:
            resume = Resume.objects.get(user=user_id)
            resume_status = StatusChoices(value=resume.status)
            resume_grade = GradeChoices(value=resume.grade)
        except Resume.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        return render(
            request, 'resume.html', context={
                'resume': resume,
                'resume_status': resume_status,
                'resume_grade': resume_grade
            }
        )


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def custom_handler404(request, exception):
    return render(
        request, '404.html', context={
        }
    )


def vacancies_ending(number_of_vacancies):
    if (number_of_vacancies == 1) or \
            (number_of_vacancies > 20 and number_of_vacancies % 10 == 1):
        return 'вакансия'
    elif (number_of_vacancies in (2, 3, 4)) or \
            (number_of_vacancies > 20 and
             number_of_vacancies % 10 in (2, 3, 4)):
        return 'вакансии'
    else:
        return 'вакансий'


def search(request):
    try:
        q = request.GET.get('s')
    except None:
        q = None
    if q:
        vacancies = Vacancy.objects.filter(
            Q(title__icontains=q) | Q(skills__icontains=q)
            | Q(description__icontains=q)).distinct()
        template = 'vacancies.html'
        word_for_vacancies = vacancies_ending(len(vacancies))
        context = {
            'query': q,
            'vacancies': vacancies,
            'title': 'Результаты поиска',
            'word_for_vacancies': word_for_vacancies
        }
    else:
        template = 'index.html'
        context = {}

    return render(request, template, context)
