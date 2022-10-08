from django.db import models
from django.forms import CharField



class Student_Data(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Email_id = models.EmailField(max_length=254)
    Courses = models.CharField(max_length=30)


class Employee(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Reporter_add(models.Model):
    name = models.CharField(max_length=30)
    job= models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class City(models.Model):
    city_name = models.CharField(max_length=30)


class Task(models.Model):
    Task_title = models.CharField(max_length=30)
    Description = models.TextField(max_length=30)
