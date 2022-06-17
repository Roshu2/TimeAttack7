from django.contrib import admin
from user.models import User as UserModel, UserType as UserTypeModel

admin.site.register(UserModel)
admin.site.register(UserTypeModel)
