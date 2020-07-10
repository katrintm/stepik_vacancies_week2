from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .choices import StatusChoices, GradeChoices
from .models import Application, Company, Vacancy, Speciality, Resume


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2',)


class ApplicationForm(forms.ModelForm):
    written_username = forms.CharField(max_length=64, label='Вас зовут')
    written_phone = forms.CharField(max_length=12, label='Ваш телефон')
    written_cover_letter = forms.CharField(
        widget=forms.Textarea,
        label='Сопроводительное письмо')

    class Meta:
        model = Application
        fields = ['written_username',
                  'written_phone',
                  'written_cover_letter']


class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        max_length=64,
        label='Название компании',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyName'})
    )
    location = forms.CharField(
        max_length=64,
        label='География',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyLocation'})
    )
    description = forms.CharField(
        label='Информация о компании',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 4,
                   'id': 'companyInfo',
                   'style': "color:#000;"})
    )
    employee_count = forms.IntegerField(
        label='Количество человек в компании',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyTeam'})
    )

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo',
                  'description', 'employee_count']


class VacancyForm(forms.ModelForm):
    title = forms.CharField(
        label='Название вакансии',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'vacancyTitle'})
    )
    skills = forms.CharField(
        label='Требуемые навыки',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3,
                   'style': 'color:#000;',
                   'id': 'vacancySkills'})
    )
    description = forms.CharField(
        label='Описание вакансии',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 13,
                   'style': 'color:#000;',
                   'id': 'vacancyDescription'})
    )
    salary_min = forms.IntegerField(
        label='Зарплата от',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'vacancySalaryMin'})
    )
    salary_max = forms.IntegerField(
        label='Зарплата до',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'vacancySalaryMax'})
    )
    speciality = forms.ModelChoiceField(
        label='Специализация',
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2',
                   'id': 'vacancySpecialization'}),
        queryset=Speciality.objects.all(),
        empty_label='Выберите значение'
    )

    class Meta:
        model = Vacancy
        fields = ['title', 'speciality',
                  'skills', 'description',
                  'salary_min', 'salary_max']


class ResumeForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'userName'})
    )
    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'userSurname'})
    )
    status = forms.ChoiceField(
        label='Готовность к работе',
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2',
                   'id': 'userReady'}),
        choices=StatusChoices.choices
    )
    salary = forms.IntegerField(
        label='Ожидаемое вознаграждение',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'userSalary'})
    )
    grade = forms.ChoiceField(
        label='Квалификация',
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2',
                   'id': 'userQualification'}),
        choices=GradeChoices.choices
    )
    education = forms.CharField(
        label='Образование',
        widget=forms.Textarea(
            attrs={'class': 'form-control text-uppercase',
                   'rows': 4,
                   'style': 'color:#000;',
                   'id': 'userEducation'})
    )
    experience = forms.CharField(
        label='Опыт работы',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 4,
                   'style': 'color:#000;',
                   'id': 'userExperience'})
    )
    portfolio = forms.CharField(
        label='Ссылка на портфолио',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'userPortfolio'})
    )
    speciality = forms.ModelChoiceField(
        label='Специализация',
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2',
                   'id': 'userSpecialization'}),
        queryset=Speciality.objects.all(),
        empty_label='Выберите значение'
    )

    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'speciality', 'grade',
                  'education', 'experience', 'portfolio']
