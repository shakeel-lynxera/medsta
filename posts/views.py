from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from posts.models import Post

# Create your views here.

def upload_post(request):
    if request.method == "POST":
        Post.objects.create(user=request.user, description = request.POST['description'])
        return redirect('/')
    else:
        return redirect("/")