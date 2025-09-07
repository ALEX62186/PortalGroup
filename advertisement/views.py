from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertisement
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AdvertForm
# Create your views here.

def advert_view(request):
    advert = Advertisement.objects.all()
    return render(request, 'advertisement/advertisement.html', {'advert': advert})

class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertForm
    template_name = 'advertisement/advertisement_create.html'
    success_url = reverse_lazy('advert:advert')

def delete_advert_view(request, topic_id):
    advert = get_object_or_404(Advertisement, pk=topic_id)
    if request.user == advert.created_by:
        advert.delete()
    return redirect('advert:advert')