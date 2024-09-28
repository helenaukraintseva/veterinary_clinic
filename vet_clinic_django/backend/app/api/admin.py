from django.contrib import admin

from .models import Client, User, MedicalHistory, Pet, Species, Breed, Service, Specialist


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "phone_number"]
    search_fields = ["username", "first_name", "last_name", "email", "phone_number"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number"]
    search_fields = ["name", "phone_number"]


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ["first_name", "second_name", "experience", "position"]
    search_fields = ["first_name", "second_name", "experience", "position"]



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "cost"]
    search_fields = ["title", "description", "cost"]



@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "age"]
    search_fields = ["name", "gender", "age"]


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ["diagnosis", "visit_date"]
    search_fields = ["diagnosis", "visit_date"]

