from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from Hotel.models import Hotel


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.review_id} by {self.user.username}'
