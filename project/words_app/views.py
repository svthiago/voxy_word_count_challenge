from django.http import HttpResponse
from django.shortcuts import render
from .forms import TextForm
from .utils import count_words

def index(request):

    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['text'])
            number_of_words = count_words(form.cleaned_data['text'])

            return render(request, 'success.html', {'number_of_words': number_of_words})

    else:
        form = TextForm()
    return render(request, 'text.html', {'form': form})
