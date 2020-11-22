from django.urls import path, include
from . import views

urlpatterns = [
    path('myapp/', include('friendship.urls')),
    path('', views.index, name='index'),
    path('profile/<slug:name>', views.profile, name="profile"),
    path('create/', views.create_post, name="create_post"),
    path('create/submit/', views.create_post_submit, name="create_post_submit"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create', views.create, name="create"),
    path('accounts/logout', views.logout_page, name="logout"),
<<<<<<< Updated upstream
    path('friends/show',views.show_friends, name="friends")

]
=======

    # delete confirmation url
    path('accounts/delete', views.delete_check, name="delete_check"),
    # actual delete url (this will delete your account, be careful)
    path('accounts/delete/confirmed', views.delete_user, name="delete_user")
]
>>>>>>> Stashed changes
