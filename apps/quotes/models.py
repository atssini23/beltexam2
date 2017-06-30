# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login.models import User


# Create your models here.
class BlogManager(models.Manager):
    def addquote(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['title']) < 1 and len(postData['content']) < 1:
            results['errors'].append('All fields must be filled out')
            results['status'] = False

        user = User.objects.get(id=postData['user_id'])
        if results['status']:

            try:
                blog = Blog.objects.create(
                    title=postData['title'],
                    content=postData['content'],
                    user_id=user,
                )
                blog.save()
            except:
                results['errors'].append('Error: Q not created')

        return results


class QsManager(models.Manager):
    def addquote(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['quote'])<1:
            results['status'] = False
            results['errors'].append('Post a quote')
        user = User.objects.get(id=postData['user_id'])
        blog = Blog.objects.get(id=postData['blog_id'])
        if results['status']:
            try:
                quote = Qs.objects.create(
                    quote=postData['quote'],
                    user_id=user,
                    blog_id=blog
                )

            except:
                results['errors'].append('Error: Quote not created')
        return results
    # 
    # def faves(self,q_id, user_id):
    #     user = User.objects.get(id=user_id)
    #     quote = Q.objects.get(id=q_id)
    #
    #     if user not in quote.blogq.all():
    #         quote.blogq.add(user)
    #     return quote



class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    user_id = models.ForeignKey('login.User', related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()

class Qs(models.Model):
    quote = models.CharField(max_length = 100)
    user_id = models.ForeignKey('login.User', related_name='userq')
    blog_id = models.ForeignKey('Blog', related_name= 'blogq')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QsManager()
