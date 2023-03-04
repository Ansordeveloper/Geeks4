from django.urls import path

from posts.views import hello, get_index, get_contacts,get_about,delete_post,get_post,update_post 

urlpatterns = [
    path('hello/', hello, name="hello-view"),
    path ("", get_index , name = "index-page"),
    path("about/", get_about, name="about-page"),
    path("contacts/", get_contacts, name="contacts-page"),
    path("get_post/", get_post, name="get_post"),
    path("update_post/", update_post, name="update_post"),
    path("delete_post/", delete_post, name="delete_post"),

]