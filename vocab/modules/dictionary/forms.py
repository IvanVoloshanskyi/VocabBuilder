from django import forms
from vocab.models import Word, RecommendWord


class WordCreationForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['en_word', 'ua_word', 'category', ]
        widgets = {
            'en_word': forms.TextInput(attrs={'placeholder': 'Enter your word'}),
            'ua_word': forms.TextInput(attrs={'placeholder': 'Введіть слово'}),
            'category': forms.Select(attrs={'placeholder': 'Choose category'}),
        }

    def __init__(self, *args, **kwargs):
        super(WordCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category"


class WordUpdateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['en_word', 'ua_word']


class WordFilterForm(forms.ModelForm):
    search_input = forms.CharField(
        required=False,
        max_length=30,
        label='',
        help_text='',
        widget=forms.TextInput(attrs={'class': 'vocab_register__form-input',
                                      'placeholder': 'Find the word',
                                      'autocomplete': 'off'}
                               ),
    )

    class Meta:
        model = Word
        fields = ['category', 'search_input']

    def __init__(self, *args, **kwargs):
        super(WordFilterForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['category'].empty_label = "Category"


class RecommendWordFilterForm(forms.ModelForm):
    search_input = forms.CharField(
        required=False,
        max_length=30,
        label='',
        help_text='',
        widget=forms.TextInput(attrs={'class': 'vocab_register__form-input',
                                      'placeholder': 'Find the word',
                                      'autocomplete': 'off'}
                               ),
    )

    class Meta:
        model = RecommendWord
        fields = ['category', 'search_input']

    def __init__(self, *args, **kwargs):
        super(RecommendWordFilterForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['category'].empty_label = "Category"
