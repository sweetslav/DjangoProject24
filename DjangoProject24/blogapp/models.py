from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return (f'Name: {self.first_name},\n'
                f'Last name: {self.last_name},\n'
                f'Email: {self.email},\n'
                f'Birthday: {self.birthday}')
