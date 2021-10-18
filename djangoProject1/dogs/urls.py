from django.urls import path
from . import views
app_name = 'dogs'
urlpatterns = [
#     lostpost views
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('stories', views.lostpost_list, name= 'lostpost-list'),
    # uses the ID of the class instance to populate the story detail page dogs/stories/1 or 2
    path('stories/<int:story_id>', views.lostpost_story_detail, name='story-detail'),

#     urls and views for the rest of the web app pages
    path('events', views.events, name='events'),
    path('parkrules', views.parkrules, name='parkrules'),
    path('searchresults', views.searchresults, name='searchresults'),

]