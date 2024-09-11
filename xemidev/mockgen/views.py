from django.shortcuts import render

# Create your views here.

def mock_gen(request):
    return render(request, 'mockgen/generator.html')