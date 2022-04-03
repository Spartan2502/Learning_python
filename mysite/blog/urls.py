from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views 
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]


# from django.urls import include, re_path
# from . import views

# app_name = 'blog'
# urlpatterns = [
#     # post views
#     re_path(r'', views.post_list, name='post_list'),
#     re_path(r'<int:year>/<int:month>/<int:day>/<slug:post>/',
#          views.post_detail,
#          name='post_detail'),
# ]