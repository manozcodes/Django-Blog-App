from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import PostShareToEmail, CommentForm
from django.core.mail import send_mail

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
# 	return render(request, 'myblog/blog.html', {'posts' : posts, 'page' : page})

# class PostListView(ListView):
# 	queryset = Post.published.all()
# 	context_object_name = 'posts'
# 	paginate_by = 3
# 	template_name = 'myblog/post/list.html'

# def post_detail(request, year, month, day, post):
# 	post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

# 	return render(request, 'myblog/post/detail.html', {'post': post})


# NEW PART
def index(request):
	return render(request, 'myblog/index.html')

def blogdetail(request, category, post):
	post = get_object_or_404(Post, slug=post, status='published', category=category)

	comments = post.comments.filter(active=True)
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
	else:
		comment_form = CommentForm()
	return render(request, 'myblog/post.html', {'post': post,
												'comments': comments,
												'new_comment': new_comment,
												'comment_form': comment_form})

class Blog(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 4
	template_name = 'myblog/blog.html'

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='published')
	sent = False

	if request.method == 'POST':
		form = PostShareToEmail(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'talk2manoz@gmail.com', [cd['to']])
			sent = True

	else:
		form = PostShareToEmail()
	return render(request, 'myblog/share.html', {'post': post,
												 'form': form,
												 'sent': sent})

