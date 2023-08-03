from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Seed
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')
	
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
	})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    id_list = finch.seeds.all().values_list('id')
    seeds_finch_doesnt_have = Seed.objects.exclude(id__in=id_list)
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'seeds': seeds_finch_doesnt_have
    })

class FinchCreate(CreateView):
    model = Finch
    fields = ['name','breed', 'scientific_name']

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'scientific_name']
  success_url = '/finches/{finch_id}'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class SeedList(ListView):
  model = Seed

class SeedDetail(DetailView):
  model = Seed

class SeedCreate(CreateView):
  model = Seed
  fields = '__all__'

class SeedUpdate(UpdateView):
  model = Seed
  fields = ['name', 'color']

class SeedDelete(DeleteView):
  model = Seed
  success_url = '/seeds'

def assoc_seed(request, finch_id, seed_id):
  Finch.objects.get(id=finch_id).seeds.add(seed_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_seed(request, finch_id, seed_id):
  Finch.objects.get(id=finch_id).seeds.remove(seed_id)
  return redirect('detail', finch_id=finch_id)
