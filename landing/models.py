from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True, default=None)
    logo = models.ImageField(upload_to='logo/', blank=True)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Компания"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Компании"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name

    def __unicode__(self):
        return self.logo.url


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Категория"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Категории"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name


class Fabric(models.Model):
    name = models.CharField(max_length=64)
    short_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    logo = models.ImageField(upload_to='logo/', blank=True)
    category = models.ManyToManyField(ProductCategory, blank=True, default=None)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Фабрика"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Фабрики"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name

    def __unicode__(self):
        return self.logo.url


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)
    article = models.CharField(max_length=7, default="артикул", unique=True)
    # purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Цена закупки
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # allowance = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=20)  # торговая надбавка
    # discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    short_description = models.TextField(max_length=128, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    prod_active = models.BooleanField(default=True)
    year_model = models.CharField(max_length=10, default="2018")
    # status_new = models.BooleanField(default=True)
    # status_sale = models.BooleanField(default=True)
    # second_hands = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)
    fabric = models.ForeignKey(Fabric, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    # sizes = models.ManyToManyField(ProductSizes, blank=True, null=True, default=None)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Товар"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Товары"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s %s" % (self.price, self.name)

    def __unicode__(self):
        return self.image.url


class Service(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Сервис"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Сервисы"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели в админке
        return "%s" % self.name


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Статус"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Статусы"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели в админке
        return "%s" % self.name


class Zvonki(models.Model):
    verbose_name = models.CharField(max_length=64, verbose_name="Ваше имя")
    phone = models.CharField(max_length=15, blank=False, null=False, default="+375", verbose_name="Телефон")
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL,
                                 verbose_name="Выберете, со специалистом какого направления желаете пообщаться")
    short_description = models.TextField(max_length=128, blank=True, null=True, default=None,
                                         verbose_name="Дополнительная информация")
    status = models.ForeignKey(Status, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Звонок"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Звонки"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели в админке
        return "%s %s" % (self.category, self.status)


class Questions(models.Model):
    verbose_name = models.CharField(max_length=64, verbose_name="Ваше имя")
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    short_description = models.TextField(max_length=600, blank=True, null=True, default=None,
                                         verbose_name="Задайте свой вопрос")
    email = models.EmailField(max_length=128, blank=True, null=False, verbose_name="email")
    status = models.ForeignKey(Status, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Вопрос"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Вопросы"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели в админке
        return "%s %s" % (self.category, self.status)
