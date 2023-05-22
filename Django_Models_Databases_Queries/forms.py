from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, models


class Review:
    pass


class ReviewForm(ModelForm):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])


