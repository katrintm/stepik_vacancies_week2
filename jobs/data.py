""" Вакансии """

jobs = [

    {"title": "Разработчик на Python", "cat": "backend",
     "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "• Python • REST • API"},
    {"title": "Разработчик в проект на Django", "cat": "backend",
     "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "• Python • Django • HTTP"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend",
     "company": "swiftattack", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "• Swift • iOS • Solid"},
    {"title": "Мидл программист на Python", "cat": "backend",
     "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "• Python • Flask • SQL"},
    {"title": "Питонист в стартап", "cat": "backend",
     "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим",
     "skills": "• Python • bootstrap • REST"},
    {"title": "Frontend-разработчик", "cat": "frontend",
     "company": "troller", "salary_from": "70000",
     "salary_to": "120000", "posted": "2020-06-12",
     "desc": "Ищем амбициозного, активного и самостоятельного человека, \
     который стремится развиваться и делать интересный и полезный проект \
     в качестве front-end разработчика.",
     "skills": "• React.js • ExtJS • Bootstrap"},
    {"title": "Frontend-разработчик", "cat": "frontend",
     "company": "primalassault", "salary_from": "90000",
     "salary_to": "120000", "posted": "2020-06-15",
     "desc": "Ищем талантливого разработчика, \
     для создания сервисов и личного кабинета",
     "skills": "• Angular2 • HTML5 • CSS3"}

]

""" Компании """

companies = [

    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreath"},
    {"title": "hirey "},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}

]

""" Категории """

specialties = [

    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}

]

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'
