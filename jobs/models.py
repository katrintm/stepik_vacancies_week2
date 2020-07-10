from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(
        upload_to='MEDIA_COMPANY_IMAGE_DIR',
        blank=True, null=True)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Speciality(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(
        upload_to='MEDIA_SPECIALITY_IMAGE_DIR',
        blank=True, null=True)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __unicode__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    speciality = models.ForeignKey(
        Speciality,
        related_name='vacancies',
        on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        related_name='vacancies',
        on_delete=models.CASCADE)
    skills = models.CharField(max_length=256)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(
        Vacancy,
        related_name='applications',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='applications',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Resume(models.Model):
    user = models.ForeignKey(
        User,
        related_name='resume',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    salary = models.IntegerField()
    speciality = models.ForeignKey(
        Speciality,
        related_name='resume',
        on_delete=models.CASCADE)
    grade = models.CharField(max_length=64)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
