from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from .choices import *
import random
class User(AbstractUser):
    username = None
    roll_request = models.BooleanField(default=False)
    phone = models.CharField("Номер телефона", max_length=20, unique=True)
    code = models.IntegerField("Код активации", null=True, blank=True)
    activated = models.BooleanField("Активировано", default=False)

    bonus_id = models.CharField("Бонусный ID", max_length=255, null=True, blank=True)
    bonus = models.DecimalField("Бонус пользователя", max_digits=10, decimal_places=2, null=True, blank=True)
    qrimg = models.ImageField("QRcode Пользователя", null=True, blank=True)

    # Notification
    notification = models.BooleanField("Получать уведомления", default=False)
    auto_brightness = models.BooleanField("Авто яркость", default=False)
    email = models.EmailField("Электронная почта", max_length=254, blank=True, null=True)
    USERNAME_FIELD = "phone"
    objects = CustomUserManager()

    # Detail
    USER_CHOICE = (
        ('1', 'Клиент'),
        ('2', 'Оптовик')
    )
    user_roll = models.CharField('Роль', max_length=100, choices=USER_CHOICE, default='1')
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=50, choices=GENDERS_CHOICES, null=True, blank=True)
    language = models.CharField("Родной язык", max_length=50, choices=LANGUAGE_CHOICES, null=True, blank=True)
    married = models.CharField("Семейное положение", max_length=100, choices=MARRIED_CHOICES, null=True, blank=True)
    status = models.CharField("Социальный статус", max_length=100, choices=SOCIAL_STATUS_CHOICES, null=True, blank=True)
    city = models.CharField("Город проживания", max_length=100, choices=CITY_CHOICES, null=True, blank=True)
    children = models.BooleanField("Наличие детей", default=False)
    animal = models.BooleanField("Наличие домашних животных", default=False)
    car = models.BooleanField("Наличие автомобиля", default=False)

    def __str__(self):
        return str(self.phone)  # Вернем номер телефона в виде строки

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        bonus_id = f"{1000200030004000 + int(self.id)}"
        self.bonus_id = bonus_id
        self.code = int(random.randint(100_000, 999_999))
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
