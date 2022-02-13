from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(Patients)
admin.site.register(Bed_avail)
admin.site.register(Report)
admin.site.register(Test)

