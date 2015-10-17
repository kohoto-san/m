from django.db import models


class Person(models.Model):

    email = models.EmailField(max_length=254)
    fisrt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    your_role = models.CharField(max_length=50)

    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
