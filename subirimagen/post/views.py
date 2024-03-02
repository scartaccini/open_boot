from django.shortcuts import render, HttpResponse
from .forms import PostForm
from .models import Post

 
def subir_img(request):
   
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES) 
        
        if form.is_valid():
            
            img = request.FILES['imagen']
        
            post = Post(title = request.POST['title'], text = request.POST['text'], imagen = img )
            post.save()
            
        return HttpResponse("ok")
    else:
        form=PostForm()
        return render(request,"subir_img.html",{"form":form})
    
def mostrar(request):
    lista_posts=Post.objects.all()
    return render(request, "inicio.html",{"lista_posts":lista_posts}) 
