from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer,Worker

admin.site.register(Customer)

admin.site.register(Worker)

#password 12345
#username isyraf