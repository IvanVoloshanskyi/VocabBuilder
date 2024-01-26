from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class Word(models.Model):
    en_word = models.CharField(max_length=20, blank=False, null=False)
    ua_word = models.CharField(max_length=20, blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} + {self.ua_word} + {self.en_word}'

    def get_absolute_url(self):
        return reverse('vocab:dictionary:word_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('vocab:dictionary:word_delete', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']


class RecommendWord(models.Model):
    en_word = models.CharField(max_length=20, blank=False, null=False)
    ua_word = models.CharField(max_length=20, blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    is_added = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    added_to_dictionary = models.ManyToManyField(User, related_name='added_words', blank=True)

    def get_absolute_url(self):
        return reverse('vocab:recommend:add-word-to-dictionary', kwargs={'pk': self.pk})

    def __str__(self):
        return self.en_word

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
