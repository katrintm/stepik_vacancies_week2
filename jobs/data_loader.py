from jobs import data
from jobs.models import Speciality, Company, Vacancy

Vacancy.objects.all().delete()
Speciality.objects.all().delete()
Company.objects.all().delete()

for speciality in data.specialties:
    Speciality.objects.create(
        code=speciality['code'],
        title=speciality['title'],
        picture=f'specty_{speciality["code"]}.png'
    )

for company in data.companies:
    Company.objects.create(
        name=company['title'],
        location='Moscow',
        description='Описание компании',
        employee_count=100
    )

for job in data.jobs:
    speciality = Speciality.objects.get(code=job['cat'])
    company = Company.objects.get(name=job['company'])
    Vacancy.objects.create(
        title=job['title'],
        speciality=speciality,
        company=company,
        description=job['desc'],
        salary_min=int(job['salary_from']),
        salary_max=int(job['salary_to']),
        published_at=job['posted']
    )

Company.objects.filter(name='workiro').update(logo='logo1.png')
Company.objects.filter(name='rebelrage').update(logo='logo2.png')
Company.objects.filter(name='staffingsmarter').update(logo='logo3.png')
Company.objects.filter(name='evilthreath').update(logo='logo4.png')
Company.objects.filter(name='hirey').update(logo='logo5.png')
Company.objects.filter(name='swiftattack').update(logo='logo6.png')
Company.objects.filter(name='troller').update(logo='logo7.png')
Company.objects.filter(name='primalassault').update(logo='logo8.png')
