from django.urls import path
from . import views
app_name = 'dogs'
urlpatterns = [
#     lostpost views
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('logout2', views.logout2, name="logout2"),

    path('posts', views.lostpost_list, name= 'lostpost-list'),
    # uses the ID of the class instance to populate the story detail page dogs/stories/1 or 2
    path('postdetail/<int:story_id>', views.lostpost_story_detail, name='story-detail'),

#     urls and views for the rest of the web app pages
    path('events', views.events, name='events'),
    path('parkrules', views.parkrules, name='parkrules'),
    path('searchresults', views.searchresults, name='searchresults'),
    path('searchresultsblank', views.searchresultsblank, name='searchresultsblank'),

    # urls and views for editing and deleting the DETAILS of a post
    path('add', views.add, name='add'),
    # path('edit', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),

    path('edit/<int:story_id>', views.lostpost_story_detail_edit, name='story-edit'),
    path('delete/<int:story_id>', views.lostpost_story_detail_delete, name='story-delete'),


#     PROJECT 5 URLS ADDED USING AJAX FROM VIEWS PY
    path('posts/upvote', views.lostpost_upvote, name='story-upvote'),

]