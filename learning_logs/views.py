from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """strona glowna dla aplikacji learning log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """wyświetlenie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
