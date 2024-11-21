from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg


def index(request):
    return render(request, 'accueil/index.html')

@csrf_exempt
def Connect(request):
    if request.method == 'POST':
        # Récupérer les données envoyées avec le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username) #Vérifier si l'identifiant et le mot de passe sont corrects
        if user.check_password(password):
            login(request, user)
            return HttpResponse("success")
        else:
            return HttpResponse("error")
        
    return redirect('accueil')     #Si ça ne fonctionne pas

@csrf_exempt
def Register(request):
    if request.method == 'POST':
        # Récupérer les données envoyées avec le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).count() ==1:
            return HttpResponse("Username déjà pris")
        else:
            try : 
                user = User.objects.create_user(username=username, password=password) # Créé un nouvel utilisateur
                return HttpResponse("success")
            except Exception as e:
                return HttpResponse("error"+str(e))
    return redirect('accueil')     #Si ça ne fonctionne pas