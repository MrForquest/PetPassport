import django.contrib.admin
from django.contrib.auth.admin import UserAdmin

import users.models

django.contrib.admin.site.register(users.models.User, UserAdmin)
