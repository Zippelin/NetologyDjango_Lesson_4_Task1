from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=150, verbose_name='Название телефона')
    price = models.FloatField(verbose_name='Цена')
    image = models.URLField(verbose_name='Ссылка')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=150)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = str(self.name).replace(' ', '_')
        super(Phone, self).save(force_insert, force_update, using, update_fields)