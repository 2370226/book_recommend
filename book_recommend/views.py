from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import BookPostForm, ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import BookPost
from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(ListView):
    template_name = "index.html"
    queryset = BookPost.objects.order_by("-posted_at")
    paginate_by = 9

@method_decorator(login_required, name="dispatch")
class CreateBookView(CreateView):
    form_class = BookPostForm
    template_name = "post_book.html"
    success_url = reverse_lazy("book_recommend:post_done")

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = "post_success.html"

class CategoryView(ListView):
    template_name = "index.html"
    paginate_by = 9
    
    def get_queryset(self) :
        category_id = self.kwargs["category"]
        categories = BookPost.objects.filter(category=category_id).order_by("-posted_at")
        return categories

class UserView(ListView):
    template_name = "index.html"
    paginate_by = 9

    def get_queryset(self) :
        user_id = self.kwargs["user"]
        user_list = BookPost.objects.filter(user=user_id).order_by("-posted_at")
        return user_list

class DetailView(DetailView):
    template_name = "detail.html"
    model = BookPost

class MypageView(ListView):
    template_name = "mypage.html"
    paginate_by = 9

    def get_queryset(self) :
        queryset = BookPost.objects.filter(user=self.request.user).order_by("-posted_at")
        return queryset

class BookDeleteView(DeleteView):
    model = BookPost
    template_name = "book_delete.html"
    success_url = reverse_lazy("book_recommend:mypage")

    def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().delete(request, *args, **kwargs)

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("book_recommend:contact")

    def form_valid(self, form: Any) -> HttpResponse:
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        title = form.cleaned_data["title"]
        message = form.cleaned_data["message"]
        subject = f"お問い合わせ: {title}"
        message = f"送信者名 {name}\n メールアドレス {email}\n タイトル {title}\n メッセージ\n{message}"
        from_email = "2370226.django@gmail.com"
        to_list = ["2370226.django@gmail.com"]
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        message.send()
        messages.success(self.request, "お問い合わせは正常に送信されました。")
        return super().form_valid(form)
