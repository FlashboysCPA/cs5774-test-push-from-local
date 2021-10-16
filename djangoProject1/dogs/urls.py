from django.urls import path
from . import views
app_name = 'dogs'
urlpatterns = [
#     lostpost views
    path('', views.lostpost_list, name= 'lostpost_list'),
    path('<int:story_id>', views.lostpost_story_detail, name='story-detail'),

]