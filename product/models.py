from django.db import models
from django.utils.translation import gettext as _

class Category(models.Model):
    name = models.CharField("Название", max_length=200)
    img = models.ImageField("Изображение", upload_to="product-category/%Y_%m")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="sub_categories")
    name = models.CharField("Название", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
class Product(models.Model):
    PRICE_FOR_CHOICES = [
        ('шт', 'Штука'),
        ('кг', 'Килограмм'),
        ('л', 'Литр'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price_for = models.CharField("Цена за", choices=PRICE_FOR_CHOICES, default="шт", max_length=10)
    old_price = models.CharField("Старая цена", max_length=100, blank=True, null=True)
    wholesale_price = models.FloatField("Оптовая цена", null=True, blank=True)
    sales = models.IntegerField(_("Количество продаж"), default=0)
    status = models.CharField(max_length=50)  # Example status field

    def __str__(self):
        return self.name

