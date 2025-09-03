from django.shortcuts import render
from .forms import SentimentForm
from .models import SentimentResult
from .sentiment import analyze_sentiment

def predict_sentiment(request):
    result = None
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            sentiment = analyze_sentiment(text)
            SentimentResult.objects.create(text=text, sentiment=sentiment)
            result = sentiment
    else:
        form = SentimentForm()

    return render(request, 'sentiment_app/index.html', {'form': form, 'result': result})
