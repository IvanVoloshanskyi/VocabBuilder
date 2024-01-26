from django.urls import path
from vocab.modules.dictionary.views import Dictionary, WordCreateView, WordUpdateView, word_delete

app_name = 'dictionary'

urlpatterns = [
    path('', Dictionary.as_view(), name="main_page"),
    path('add-word/', WordCreateView.as_view(), name='word_create'),
    path('<int:pk>/update/', WordUpdateView.as_view(), name='word_update'),
    path('<int:pk>/delete/', word_delete, name='word_delete'),
]
