from django.urls import path
from . import views
app_name = 'dogs'
urlpatterns = [
#     lostpost views
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('logout2', views.logout2, name="logout2"),




#     urls and views for the rest of the web app pages
    path('events', views.events, name='events'),
    path('parkrules', views.parkrules, name='parkrules'),
    path('searchresults', views.searchresults, name='searchresults'),
    path('searchresultsblank', views.searchresultsblank, name='searchresultsblank'),

    # PROJECT5 updates made
    path('posts', views.lostpost_list, name='lostpost-list'),
    path('posts_date', views.lostpost_list_date, name='lostpost-list-date'),
    path('posts_date2', views.lostpost_list_date2, name='lostpost-list-date2'),
    # uses the ID of the class instance to populate the story detail page dogs/stories/1 or 2
    path('postdetail/<int:story_id>', views.lostpost_story_detail, name='story-detail'),

    # urls and views for editing and deleting the DETAILS of a post
    path('add', views.add, name='add'),

    path('edit/<int:story_id>', views.lostpost_story_detail_edit, name='story-edit'),
    path('delete/<int:story_id>', views.lostpost_story_detail_delete, name='story-delete'),


#     PROJECT 5 URLS ADDED USING AJAX FROM VIEWS PY
    path('posts/delete', views.lostpost_delete, name='story-deletefromdatabase'),
    path('posts/edit', views.lostpost_edit, name='story-editfromdatabase'),

    # PROJECT5 SORT
    path('posts/sort', views.list_sort_ajax, name='list_sort_ajax'),

# PROJECT5 AJAX USED IN LIST.JS
    path('posts/upvote', views.lostpost_upvote, name='story-upvote'),
    path('posts/downvote', views.lostpost_downvote, name='story-downvote'),

    path('posts/contact', views.view_contact_ajax, name='view-contact-ajax'),
    path('posts/follow', views.view_follow_ajax, name='view-follow-ajax'),
]