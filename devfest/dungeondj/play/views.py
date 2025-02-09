from django.shortcuts import render

# Create your views here.
def play_list(request):
    return render(request,'play/play_list.html')