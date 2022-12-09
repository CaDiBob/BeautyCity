from django.contrib import admin

from .models import (
    Order,
    Salon,
    Schedule,
    Category,
    Worker,
    Service
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ProcedureAdmin(admin.ModelAdmin):
    pass
