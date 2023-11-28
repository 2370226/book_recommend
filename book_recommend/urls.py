from django.urls import path
from . import views

app_name = "book_recommend"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.CreateBookView.as_view(), name="post"),
    path("post_done/", views.PostSuccessView.as_view(), name="post_done"),
    path("book/<int:category>/", views.CategoryView.as_view(), name="book_cat"),
    path("user-list/<int:user>/", views.UserView.as_view(), name="user_list"),
    path("book-detail/<int:pk>/", views.DetailView.as_view(), name="book_detail"),
    path("mypage/", views.MypageView.as_view(), name="mypage"),
    path("book/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
