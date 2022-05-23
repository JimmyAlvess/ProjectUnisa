from django.contrib import admin

from .models import Categoria, Medico, Paciente

# Register your models here.


class MedicoAdmin(admin.ModelAdmin):
    pass


class CategoriaAdmin(admin.ModelAdmin):
    pass


class PacienteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Paciente, PacienteAdmin)
