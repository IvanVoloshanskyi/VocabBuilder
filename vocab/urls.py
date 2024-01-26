from django.urls import path, include

# Powered by Ivan Voloshanskyi

app_name = 'vocab'

urlpatterns = [
    path('', include('vocab.modules.dictionary.urls')),
    path('', include('vocab.modules.recommend.urls')),
    path('', include('vocab.modules.training.urls')),
]
