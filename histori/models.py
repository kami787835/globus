from django.db import models
from django.utils.translation import gettext as _
class Stories(models.Model):
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)
    img = models.ImageField(_("Изображение"), upload_to="story_images")
    link = models.URLField(_('Ссылка'), max_length=500, blank=True, null=True, help_text='Если есть')

    class Meta:
        verbose_name = _("История")
        verbose_name_plural = _("Истории")


class StoryVideos(models.Model):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE, related_name="stories")
    url = models.FileField(_("История"), upload_to="stories")
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)

    class Meta:
        verbose_name = _("Истории")
        verbose_name_plural = _("История")

    def __str__(self):
        return self.created_at.strftime("%d %B %Y г. %H:%M")

class Cards(models.Model):
    TYPE_CHOICES = [
        (1, 'Специальные предложения'),
        (2, 'Акция')
    ]

    type = models.IntegerField('Тип', choices=TYPE_CHOICES)
    text = models.TextField('Описание', blank=True, null=True)
    title = models.CharField('Название', max_length=150, help_text='Успей купить!')
    datefrom = models.DateField('Дата начала акции')
    dateto = models.DateField('Дата окончания акции')
    date = models.CharField(blank=True, null=True, max_length=150, editable=False)
    img = models.ImageField('Картинка', upload_to='promotions/%Y_%m')

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки (Акция/Предложения)'

    def __str__(self):
        return self.title