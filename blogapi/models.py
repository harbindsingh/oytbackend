from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    CATEGORY_CHOICES=[
        ('entertainment', 'Entertainment'),
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('sports', 'Sports'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank = True)
    content = RichTextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return (self.title + str(self.id))

class IdeaSubmission(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.EmailField()
    contact_no = models.CharField(max_length=15)
    idea_content = models.TextField()

    def __str__(self):
        return self.name

class queryForm(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    query = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class jobOpening(models.Model):
    title = models.CharField(max_length=150)
    place = models.CharField(max_length=150, help_text="Ex: Jaipur, Rajasthan")
    skills = models.CharField(max_length=500, help_text="Enter skills comma(,) separated")

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.EmailField(max_length=256)
    contact = models.CharField(max_length=15)
    position = models.CharField(max_length=150)
    experience = models.FloatField()
    resume_cv = models.FileField(upload_to='media/', default="")

    def __str__(self):
        return (str(self.id)+self.name + self.position)
        
