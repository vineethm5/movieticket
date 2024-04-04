from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Basemodel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now_add=True)

class Meta:
    abstract= True

#Important
""" In Django, when you set abstract = True within the class Meta of a model, you're creating an abstract base class. 
Abstract base classes are used when you want to define a model's fields and methods that you don't intend to create database tables for. 
Instead, you'll use this base class to inherit from in other models to share common fields and methods."""


""" We define a CommonInfo abstract base class with name and age fields.
abstract = True in the class Meta indicates that CommonInfo is an abstract class, and it will not create a database table for it.
We then create concrete models Student and Teacher, both of which inherit from CommonInfo.
The Student and Teacher models automatically inherit the fields name and age from the CommonInfo base class.
When migrations are run, only tables for the Student and Teacher models will be created in the database, not for the CommonInfo abstract base class. """

class moviecategory(Basemodel):
    moviecat=models.CharField(max_length=100)

class movie(Basemodel):
    category=models.ForeignKey(moviecategory,on_delete=models.CASCADE)
    moviename=models.CharField(max_length=200)
    price=models.IntegerField(default=100)
    images=models.CharField(max_length=400) 

""" In Django, the on_delete argument is used in ForeignKey fields to specify the behavior to adopt when the referenced object is deleted. 
It's used to handle cascading deletes, ensuring data integrity when related objects are deleted.The on_delete argument accepts several options, including:
CASCADE: When the referenced object is deleted, also delete the objects that have a ForeignKey pointing to it."""