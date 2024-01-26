from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from vocab.models import Word


@login_required
def training(request):
    words_to_train = request.session.get('words_to_train', [])
    current_word_index = request.session.get('current_word_index', 0)
    request.session['current_word_index'] = current_word_index  # Initialize if not present
    request.session['answers'] = request.session.get('answers', [])
    # If not, fetch new random words and store them in the session
    if not words_to_train:
        words_to_train = list(
            Word.objects.filter(owner=request.user, status__lt=100).select_related('owner').order_by("?")[:10])
        request.session['words_to_train'] = [{'pk': word.pk, 'en_word': word.en_word, 'ua_word': word.ua_word} for word
                                             in words_to_train]

    if len(words_to_train) < 10:
        request.session['words_to_train'] = []
        return render(request, 'inc/_zero_words_training.html')

    if current_word_index < len(words_to_train):
        current_en_user_word = request.session['words_to_train'][current_word_index]['en_word']
        current_ua_user_word = request.session['words_to_train'][current_word_index]['ua_word']

        if request.method == "GET":
            total_words = len(words_to_train)

            words_left_amount = len(words_to_train) - current_word_index
            context = {'current_en_user_word': current_en_user_word,
                       'words_left_amount': words_left_amount,
                       'total_words': total_words}
            return render(request, 'vocab_templates/training.html', context)

        if request.method == "POST":
            user_answer = request.POST.get('answer').lower()
            is_correct = user_answer == current_ua_user_word.lower()

            request.session['answers'].append({
                'word_pk': words_to_train[current_word_index]["pk"],
                'user_answer': user_answer,
                'en_word': current_en_user_word,
                'is_correct': is_correct,
            })

            request.session['current_word_index'] += 1
            request.session.save()

            return redirect('vocab:training:training-page')

    else:
        return redirect('vocab:training:show-results')


@login_required
def save_training(request):
    answers = request.session.get('answers', [])

    word_pks = [answer_data['word_pk'] for answer_data in answers]

    words = Word.objects.in_bulk(word_pks)

    for answer_data in answers:
        word_pk = answer_data['word_pk']
        user_answer = answer_data['user_answer']

        word = words.get(word_pk)

        if word:
            if word.ua_word.lower() == user_answer.lower():
                word.status += 10
                word.save()

    request.session['words_to_train'] = []
    request.session['answers'] = []
    request.session['current_word_index'] = 0
    request.session.save()

    context = {'answers': answers}
    return render(request, 'inc/_well_done_modal.html', context)


def make_new_words(request):
    request.session['words_to_train'] = []
    request.session['answers'] = []
    request.session['current_word_index'] = 0
    request.session.save()
    return redirect('vocab:training:training-page')
