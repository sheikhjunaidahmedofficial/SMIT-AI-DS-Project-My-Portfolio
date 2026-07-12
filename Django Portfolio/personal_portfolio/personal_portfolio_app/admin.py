from django.contrib import admin
from .models import (
    Profile,
    About,
    Education,
    Skill,
    CareerGoal,
    Project,
    Contact,
)

# Register your models here.

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(CareerGoal)
admin.site.register(Project)
admin.site.register(Contact)