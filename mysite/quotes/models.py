from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200, default='NA')

    def __str__(self):
        return self.name

class Quote(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateField('date created')

    def __str__(self):
        return f"{self.text} - {self.person}, {self.date}"
