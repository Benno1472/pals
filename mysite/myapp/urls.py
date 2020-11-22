from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('myapp/', include('friendship.urls')),
    path('', views.index, name='index'),
    path('profile/<slug:name>', views.profile, name="profile"),
    path('create/', views.create_post, name="create_post"),
    path('create/submit/', views.create_post_submit, name="create_post_submit"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create', views.create, name="create"),
    path('accounts/logout', views.logout_page, name="logout"),
    path('friends/show',views.show_friends, name="friends"),
    path('delete/<int:post_key>', views.delete_post, name="delete_post"),
    path('accounts/delete', views.delete_check, name="delete_check"),
    # actual delete url (THIS WILL DELETE YOUR ACCOUNT)
    path('accounts/delete/confirmed', views.delete_user, name="delete_user"),
    path('friends/send',views.send_friend_request, name="send_friend_request"),
    path('image_upload', views.post_image_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
]
