from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list

class Employee(models.Model):
    """
    Model representing a employee
    """
    name = models.CharField(max_length=200, help_text="Enter name")

    def get_absolute_url(self):

        return reverse('employee-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Group(models.Model):

    employee_list = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
    creation_date = models.DateTimeField('date created')
    expiration_date = models.DateTimeField(null=True, blank=True)
    runtime = models.ForeignKey('History', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):

        return reverse('group-detail', args=[str(self.id)])


class History(models.Model):

    runtime = models.DateTimeField('date created')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):

        return reverse('group-detail', args=[str(self.id)])

