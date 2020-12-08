from django.shortcuts import render
from .models import Jokes 

# Create your views here.
def index(request):
    return render(request, "JokeBot/index.html")
    
def checkInput(request):
    if request.method == 'POST':
        usrInput = request.POST
        empty = Jokes.objects.all()
    
        if empty.exists():
            return_joke = Jokes.objects.filter(name__iexact=usrInput).get()          
        else:
            init_question = 'Hey JokeBot, tell me a joke'
            result = 'I don’t know any jokes yet, but I would love to learn one from you, can you tell me a Knock knock joke?'
            joke = Jokes.objects.create(question=init_question,response=result)
            joke.save()
        
    return render(request, "JokeBot/index.html", {'returnJoke':return_joke})