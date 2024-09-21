from django.shortcuts import render
from .models import Topic, Category
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import TopicSearchForm

# Create your views here.
def home(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'topics': topics, 'categories': categories})

def detail(request, id):
    topic = get_object_or_404(Topic, id=id)

    data = {
        'topic': topic
    }

    return render(request, 'detail.html', data)

def search(request):
    search_form = TopicSearchForm(request.GET or None)
    topics = Topic.objects.all()

    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        topics = topics.filter(name__icontains=query)

    # Pagination logic
    paginator = Paginator(topics, 1)
    page_number = request.GET.get('page')
    topics_page = paginator.get_page(page_number)

    return render(request, 'search.html', {
        'topics': topics_page,
        'search_form': search_form,
    })
