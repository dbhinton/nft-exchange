from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
# Create your models here.


RATINGS = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five'),
)


class Nft(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    price = models.IntegerField()
    ffile = models.ImageField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})


class Comment(models.Model):
    text = models.CharField(max_length=150)
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )


nft = models.ForeignKey(Nft, on_delete=models.CASCADE)


