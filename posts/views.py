from django.shortcuts import redirect, render

from django.http import HttpResponse
from posts.forms import CommentForm, PostForm

from posts.models import Post, Comment

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

    def get_context_data(self, *, object_name=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context  
        

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"

    def post(self, request, pk):
        post = Post.objects.get(pk=pk) # ИЛИ post_id ЕСЛИ БЫ НЕ БЫЛО pk, НУЖЕН input hidden
        form = CommentForm(request.POST)


        # name = request.POST.get("name", None)
        # text = request.POST.get("text", None)
        
        # if name and text:
        #     comment = Comment.objects.create(name=name, text=text, post=post)
        #     comment.save()

        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()

        return redirect("post-detail", pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['title'] = 'Просмотр поста'
        return context   

    
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm
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


 