from django.contrib import admin

# Register your models here.
#to add stuff in adminpage
from.models import Question, Choice  

admin.site.register(Question)
admin.site.register(Choice)
#even when the server is running we can make changes in the admin page

