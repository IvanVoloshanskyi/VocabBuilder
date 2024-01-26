from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib import messages
from vocab.modules.dictionary.forms import WordUpdateForm, WordCreationForm, WordFilterForm
from vocab.models import Word, RecommendWord


class Dictionary(LoginRequiredMixin, ListView):
    template_name = "vocab_templates/dictionary.html"
    context_object_name = "words"
    paginate_by = 5
    form_class = WordFilterForm

    @staticmethod
    def set_queryset(query):
        return query

    def get_queryset(self):
        queryset = self.set_queryset(Word.objects.filter(owner=self.request.user).prefetch_related('category'))
        form = self.form_class(self.request.GET)

        if form.is_valid():
            category = form.cleaned_data['category']
            search_term = form.cleaned_data['search_input']

            if category:
                queryset = queryset.filter(category=category)
            if search_term:
                queryset = queryset.filter(Q(ua_word__icontains=search_term) | Q(en_word__icontains=search_term))

        return queryset

    def get_study_words(self):
        count = Word.objects.filter(owner=self.request.user, status__lt=100).count()
        return count

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        context['get_study_words'] = self.get_study_words()
        return context


class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    form_class = WordCreationForm
    template_name = 'inc/_add_word.html'
    success_url = reverse_lazy('vocab:dictionary:main_page')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class WordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Word
    context_object_name = 'word'
    form_class = WordUpdateForm
    template_name = 'inc/_edit_word.html'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(request, "Error")
            return redirect("vocab:dictionary:main_page")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f"{self.object.en_word} edited successfully")
        redirect_to = self.request.POST.get('value')  # get num of page and redirect to it
        print(redirect_to)
        return redirect_to


def word_delete(request, pk):
    try:
        word = get_object_or_404(Word, id=pk, owner=request.user)

        # Try to get the corresponding RecommendWord object
        try:
            rec_word = RecommendWord.objects.get(
                en_word=word.en_word,
                ua_word=word.ua_word,
                category=word.category
            )

            # Remove the user from the added_to_dictionary field
            if request.user in rec_word.added_to_dictionary.all():
                rec_word.added_to_dictionary.remove(request.user)
        except RecommendWord.DoesNotExist:
            # Handle the case when RecommendWord does not exist
            pass

        # Delete the Word object
        word.delete()

        messages.success(request, f"{word.en_word} deleted successfully")
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('vocab:dictionary:main_page')
