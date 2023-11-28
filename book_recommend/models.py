from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name="カテゴリ",
        max_length=20
    )

    def __str__(self):
        return self.title

class BookPost(models.Model) :
    user = models.ForeignKey(
        CustomUser,
        verbose_name="ユーザー",
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリ",
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name="タイトル",
        max_length=200
    )
    author =models.CharField(
        verbose_name="著者",
        max_length=50,
        null=True
    )
    publisher =models.CharField(
        verbose_name="出版社",
        max_length=50,
        null=True
    )
    comment = models.TextField(verbose_name="コメント")
    image = models.ImageField(
        verbose_name="書影",
        upload_to="photos"
    )
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )

    def __str__(self):
        return self.title
