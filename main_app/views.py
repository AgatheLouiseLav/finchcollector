from django.shortcuts import render

# Create your views here.

finches = [
  {'name': 'Cactus', 'breed': 'Hawfinch', 'scientific_name': 'Coccothraustes coccothraustes', 'age': 3},
  {'name': 'Mochi', 'breed': 'Purple Finch', 'scientific_name': 'Haemorhous purpureus', 'age': 0},
]

def home(request):
    return render(request, 'home.html')
	

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
	})