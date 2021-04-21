from django.shortcuts import render

# Create your views here.
def removesame(request):
    return render(request, 'tools/removeSame.html')

