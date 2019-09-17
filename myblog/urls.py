from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
	# path('', views.post_list, name='post_list')
	# path('', views.PostListView.as_view(), name='post_list'),
	path('', views.Blog.as_view(), name='blog'),
	path('index/', views.index, name='index'),
	path('<category>/<slug:post>/', views.blogdetail, name='blogdetail'),
	# path('blog/', views.blog, name='index'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]