from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.CustomerRegister)
admin.site.register(models.Stock)


