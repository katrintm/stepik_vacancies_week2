from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from jobs.views import CategoryVacanciesView
from jobs.views import ResumeCreateView
from jobs.views import CompaniesView
from jobs.views import CompanyView
from jobs.views import MainView
from jobs.views import MyCompanyCreateView
from jobs.views import MyCompanyVacanciesView
from jobs.views import MyCompanyVacancyCreateView
from jobs.views import MyCompanyVacancyView
from jobs.views import MyCompanyView
from jobs.views import ResumeView
from jobs.views import VacanciesView
from jobs.views import VacancySendView
from jobs.views import VacancyView
from jobs.views import custom_handler404
from jobs.views import search
from jobs.views import signup
from jobs.views import UserResumeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:category>/', CategoryVacanciesView.as_view()),
    path('companies/<int:company_id>/', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view()),
    path('companies/', CompaniesView.as_view()),
    path('vacancies/<int:vacancy_id>/send/', VacancySendView.as_view()),
    path('mycompany/', MyCompanyView.as_view()),
    path('mycompany/create/', MyCompanyCreateView.as_view()),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyVacancyView.as_view()),
    path('mycompany/vacancies/create/', MyCompanyVacancyCreateView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('search/', search, name='search'),
    path('myresume/', ResumeView.as_view()),
    path('myresume/create/', ResumeCreateView.as_view()),
    path('resume/<int:user_id>/', UserResumeView.as_view())
]

handler404 = custom_handler404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
