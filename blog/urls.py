from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.postListView.as_view(), name ='post_list'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('post/<int:pk>',views.postDetailView.as_view(), name= 'post_detail'),
    path('post/new/', views.cratePostView.as_view(),name = 'post_new'),
    path('post/<int:pk>/edit', views.postUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name = 'post_remove'),
    path('drafts/',views.DraftView.as_view(), name = 'post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name = 'add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.commentApprove,name = 'commentApprove'),
    path('commnet/<int:pk>/remove/', views.comment_remove, name= 'comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name = 'post_publish')
]
