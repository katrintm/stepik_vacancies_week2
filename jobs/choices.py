from django.db import models


class GradeChoices(models.TextChoices):
    JUNIOR = 'j', 'Младший (junior)'
    MIDDLE = 'm', 'Средний (middle)'
    SENIOR = 's', 'Старший (senior)'


class StatusChoices(models.TextChoices):
    YES = 'y', 'Ищу работу'
    MAYBE = 'm', 'Открыт к предложениям'
    NO = 'n', 'Не ищу работу'
