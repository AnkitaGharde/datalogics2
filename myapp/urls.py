from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    path('python', views.python, name='python'),

    path('ML', views.ML, name='ML'),

    path('data', views.data, name='data'),
    path('courses', views.courses, name='courses'),

    path('blog', views.blog, name='blog'),

    path('contact', views.contact, name='contact'),

]
