from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
		STATUS_CHOICE = (('draft', 'Draft'),('published', 'Published'))
		CATEGORY_CHOICE = (('datascience', 'Data Science'),('machinelearning', 'Machine Learning'))
		title 		  = models.CharField(max_length=250)
		slug 		  = models.SlugField(max_length=100, unique_for_date='publish')
		author 		  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
		image         = models.ImageField(upload_to='blog_images/', default='/blog_images/default.jpg')
		body 		  = models.TextField()
		category	  = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default='datascience')
		publish 	  = models.DateTimeField(default=timezone.now)
		created 	  = models.DateTimeField(auto_now_add=True)
		updated 	  = models.DateTimeField(auto_now=True)
		status 	      = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
		tags		  = TaggableManager()

		objects = models.Manager()
		published = PublishedManager()

		# def get_absolute_url(self):
		# 	return reverse('myblog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

		def get_absolute_url(self):
			return reverse('myblog:blogdetail', args=[self.category, self.slug])

		class Meta:
			ordering = ('-publish',)

		def __str__(self):
				return self.title

class Comment(models.Model):
		post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
		name = models.CharField(max_length=75)
		email = models.EmailField()
		body = models.TextField()
		created = models.DateTimeField(auto_now_add=True)
		updated = models.DateTimeField(auto_now=True)
		active = models.BooleanField(default=True)

		class Meta:
			ordering = ('created',)

		def __str__(self):
			return 'Comment by {} on {}'.format(self.name, self.post)