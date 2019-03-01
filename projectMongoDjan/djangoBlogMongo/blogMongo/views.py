from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse 
from django.template import loader 
from blogMongo.models import Blog
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.db import models
import datetime

#Se define index donde recibe como argumento request
@csrf_exempt
def index(request):
    #SI el metodo es un post, se toma los datos del formulario y se guarda en 
    #mongodb
    if request.method == 'POST':
       # nuevo post
       title = request.POST['title']
       content = request.POST['content']
       post = Blog()
       post.title = title
       post.last_update = datetime.datetime.now()
       post.content = content
       post.save()
   #Si el metodo es get entonces se está cargando la página inicialmente, así que se publican 
   #los posts
    # se obtiene todos los posts de la base de datos
    posts = Blog.objects.all()
    return render_to_response('index.html', {'Blog': posts}, RequestContext(request))


#Actualizar un post
@ensure_csrf_cookie
def update(request):
    #Captura el id del post
    #id = eval("request." + request.method + "['id']")
    allblogs = Blog.objects.all()
    if(allblogs.count()==0):
        template = 'update.html'
        params = {'post':Blog.objects}
        return render_to_response(template, params, RequestContext(request))

    post = Blog.objects.all()[0]
    #Si el metodo es post, se está actualizando la información del formulario
    if request.method == 'POST':
       
        # se actualiza los valores y se salva en mongodb
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Blog.objects}
    #Si el metodo es GET se muestra la página incial update.html
    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}

    return render_to_response(template, params, RequestContext(request))

#Para borrar un posts
@ensure_csrf_cookie
def delete(request):
    #Se toma el id del post
    id = eval("request." + request.method + "['id']")
    #Se pregunta si es POST, se le pasa el id del posts y se borra, se va a la página index.html
    if request.method == 'POST':
        post = Blog.objects(id=id)[0]
        post.delete()
        template = 'index.html'
        params = {'Posts': Blog.objects}
    #Si es un metodo get entonces se muestra la página delete.html
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id }

    return render_to_response(template, params, RequestContext(request))