from django import forms
from django.contrib import admin
from .models import GitHubLink, Project,Category,Customer,Order



admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(GitHubLink)



