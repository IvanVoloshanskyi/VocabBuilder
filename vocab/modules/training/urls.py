from django.urls import path
from vocab.modules.training.views import training, save_training, make_new_words

app_name = 'training'

urlpatterns = [
    path('training/', training, name='training-page'),
    path('show-results/', save_training, name='show-results'),
    path('make_new_words/', make_new_words, name='make_new_words'),
]
