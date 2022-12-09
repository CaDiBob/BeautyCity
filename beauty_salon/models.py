from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from users.models import User


class Salon(models.Model):
    name = models.CharField(
        'Название салона',
        max_length=255,
        db_index=True,
    )
    image = models.ImageField(
        'Изображение',
        db_index=True,
    )
    address = models.CharField(
        'адрес',
        max_length=255,
        db_index=True
    )

    def __str__(self):
        return f'{self.name} {self.address}'

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Worker(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        db_index=True
    )
    specialization = models.ForeignKey(
        'Category',
        related_name='workers',
        verbose_name='Специализация',
        on_delete=models.CASCADE,
        db_index=True
    )
    salon = models.ForeignKey(
        Salon,
        related_name='workers',
        verbose_name='Салон',
        on_delete=models.CASCADE,
        db_index=True
    )
    foto = models.ImageField(
        'Фотография',
        db_index=True
    )
    reviews_qty = models.TextField(
        'Отзыв',
        db_index=True,
    )
    experience = models.CharField(
        'Опыт работы',
        max_length=255,
        db_index=True
    )

    def __str__(self):
        return f'{self.name} {self.specialization} {self.salon}'

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Category(models.Model):
    name = models.CharField(
        'Категория услуг',
        max_length=255,
        db_index=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class PaymentMethod(models.TextChoices):
    CASHLESS = 'cashless', 'Безналичный'
    CASH = 'cash', 'Наличные'


class PaymentStatus(models.TextChoices):
    PAID = 'paid', 'Оплачен'
    NOT_PAID = 'not_paid', 'Не оплачен'


class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name='orders',
        verbose_name='Кто заказал',
        on_delete=models.CASCADE,
        db_index=True
    )
    procedure = models.ForeignKey(
        'Service',
        related_name='orders',
        verbose_name='Процедура',
        on_delete=models.CASCADE,
        db_index=True
    )
    worker = models.ForeignKey(
        Worker,
        related_name='orders',
        verbose_name='Специалист',
        on_delete=models.CASCADE,
        db_index=True
    )
    salon = models.ForeignKey(
        Salon,
        related_name='orders',
        verbose_name='Салон',
        on_delete=models.CASCADE,
        db_index=True
    )
    created_at = models.DateTimeField(
        'Дата и время создания',
        default=timezone.now,
        db_index=True
    )
    payment_method = models.CharField(
        'Способ оплаты',
        max_length=12,
        blank=True,
        choices=PaymentMethod.choices,
        db_index=True,
    )
    payment_status = models.CharField(
        'Статус оплаты',
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.NOT_PAID,
        db_index=True
    )

    def __str__(self):
        return f'{self.procedure} {self.worker.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Service(models.Model):
    name = models.CharField(
        'Название процедуры',
        max_length=255,
        db_index=True
    )
    category = models.ForeignKey(
        'Category',
        related_name='services',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        db_index=True
    )
    descriptions = models.TextField(
        'Описание',
        db_index=True
    )
    image = models.ImageField(
        'Изображение',
        db_index=True
    )
    duration = models.CharField(
        'Продолжительность',
        max_length=255,
        db_index=True
    )
    price = models.DecimalField(
        'цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        db_index=True
    )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'


class Schedule(models.Model):
    salon = models.ForeignKey(
        Salon,
        related_name='schedules',
        verbose_name='Салон',
        on_delete=models.CASCADE,
        db_index=True
    )
    order = models.ForeignKey(
        Order,
        related_name='schedules',
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        db_index=True
    )
    time_start = models.TimeField(
        'Время начала',
        db_index=True
    )
    time_end = models.TimeField(
        'Время окончания',
        db_index=True
    )
    day = models.DateField(
        'День',
        db_index=True
    )

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
