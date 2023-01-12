from django.contrib.auth.models import User
from django.db import models
from news.resources import KIND
from django.db.models import Sum


class Author(models.Model):
    rating = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        rating_posts = self.post_set.aggregate(posts_rating=Sum('rating'))
        count_rating_posts = 0
        count_rating_posts += rating_posts.get('posts_rating')
        rating_comments = self.user.comment_set.aggregate(comments_rating=Sum('rating'))
        count_rating_comments = 0
        count_rating_comments += rating_comments.get('comments_rating')

        self.rating = count_rating_posts * 3 + count_rating_comments
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, default='unnamed', unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    kind = models.CharField(max_length=2, choices=KIND, default=news)
    date_posting = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=255, default='none')
    text = models.TextField(default='none')
    rating = models.IntegerField(default=0)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='PostCategory')

    def __str__(self):
        return str(self.header + ' | ' + self.preview())

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:123] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(default='none')
    date_posting = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
