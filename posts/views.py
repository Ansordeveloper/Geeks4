from django.shortcuts import render

from django.http import HttpResponse

from posts.models import Post

from django.views import generic
from django.urls import reverse_lazy

def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """"
    # <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Page Title</title>
    #     </head>
    #     <body>
    #         <h1>My First Heading</h1>
    #         <p>My first paragraph.</p>
    
    #     </body>
    #     </html>
    # """
    headers = {"name":"ansor"}
    return HttpResponse(body, headers=headers, status=200)

def get_index(request):
    posts = Post.objects.filter(status=True)
    context = {
        "title": "Main page",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)

class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    # model = Post
    template_name = "posts/index.html"

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
    


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }
# def get_about(request):
#     context = {
#         "title": "Страница о нас",
#     }
#     return render(request, "posts/about.html", context=context)


def get_contacts(request):
    context = {
        "title": "Контакная страница",
    }
    return render(request, "posts/contact.html", context=context)


def get_post(request):
    context = {
        "title": "Post"
    }
    return render(request, "posts/post_detail.html", context=context)

def update_post(request):
    contex = {
        "title": "Update"
    }
    return render(request, "posts/post_update.html", context=contex)


def delete_post(request):
    contex = {
        "title": "delite"
    }
    return render(request, "posts/post_create.html", context=contex)
