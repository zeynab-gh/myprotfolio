import datetime
from django.db import models
from django.core.validators import FileExtensionValidator



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class Project(models.Model):
    titel = models.CharField(max_length=200)  # اصلاح شد: 'title'، نه 'titel'
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    download_file = models.FileField(upload_to='project_files/', blank=True, null=True)
    video = models.FileField(
        upload_to='project_videos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv'])]
    )

    def str(self):
        return self.titel
    

class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    product = models.ForeignKey(Project, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=20, blank= True)
    phone = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.product





class GitHubLink(models.Model):
    project = models.ForeignKey(Project, related_name='github_links', on_delete=models.CASCADE)
    url = models.URLField()