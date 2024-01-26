from django.shortcuts import redirect
from django.contrib import messages
from vocab.models import RecommendWord, Word
from vocab.modules.dictionary.forms import RecommendWordFilterForm
from vocab.modules.dictionary.views import Dictionary


class RecommendPage(Dictionary):
    template_name = "vocab_templates/recommend.html"
    context_object_name = "rec_words"
    paginate_by = 5
    form_class = RecommendWordFilterForm

    def set_queryset(self, query):
        user_added_words_ids = self.request.user.added_words.values_list('id', flat=True)
        return RecommendWord.objects.exclude(id__in=user_added_words_ids).prefetch_related('category')


def add_word_to_dictionary(request, pk):
    rec_word = RecommendWord.objects.get(pk=pk)

    dict_word = Word.objects.create(
        en_word=rec_word.en_word,
        ua_word=rec_word.ua_word,
        category=rec_word.category,
        status=0,
        owner=request.user
    )
    rec_word.added_to_dictionary.add(request.user.id)
    messages.success(request, f"Successfully added '{dict_word.en_word}'")
    return redirect(request.META.get('HTTP_REFERER'))
