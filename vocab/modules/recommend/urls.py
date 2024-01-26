from django.urls import path
from vocab.modules.recommend.views import RecommendPage, add_word_to_dictionary

app_name = 'recommend'

urlpatterns = [
    path('recommend/', RecommendPage.as_view(), name='recommend-page'),
    path('add-word-to-dictionary/<int:pk>/', add_word_to_dictionary, name='add-word-to-dictionary'),
]
