from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """strona glowna dla aplikacji learning log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """wyświetlenie wszystkich tematów"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """wyswietla pojedynczy temat i wszystkie powiazane z nim wpisy"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """dodaj nowy temat"""
    if request.method != 'POST':
        #nie przekazano zadnych danych nalezy utworzyc pusty formularz
        form = TopicForm()
    else:
        #przekazano dane za pomoca zodania post  nalezy je przetworzyc
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla okreslonego tematu."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #nie przekazano zadnych danych, nalezy utworzyc pusty formularz
        form = EntryForm()

    else:
        #przekazano wartosci za pomoca zadania POST, trzeba je przetworzyc
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic_id]))
            context = {'topic':topic, 'form':form}
            return render(request, 'learning_logs/new_entry.html', context)
