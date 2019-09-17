from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# def post_list(request):
# 	posts = Post.published.all()
	# paginator = Paginator(posts, 3)
	# page = request.GET.get('page')
	# try:
	# 	posts = paginator.page(page)
	# except PageNotAnInteger:
	# 	posts = paginator.page(1)
	# except EmptyPage:
	# 	posts = paginator.page(paginator.num_pages)
# 	return render(request, 'myblog/post/list.html', {'posts' : posts, 'page' : page})

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'myblog/post/list.html'

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

	return render(request, 'myblog/post/detail.html', {'post': post})


# NEW PART

def index(request):
	return render(request, 'myblog/index.html')

def blogdetail(request, category, post):
	post = get_object_or_404(Post, slug=post, status='published', category=category)
	return render(request, 'myblog/post.html', {'post': post})

class Blog(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 4
	template_name = 'myblog/blog.html'