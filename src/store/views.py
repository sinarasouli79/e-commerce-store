from django.shortcuts import render

# Create your views here.
def print_message(request):

    context = {'message' : 'Hello World'}

    return render(request, 'helloworld.html', context)