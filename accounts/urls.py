from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

from . import views
from . import views_home
from . import views_profile
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
                  path('login/', views_home.login_view, name='index'),
                  path('setup/', views_home.setup_view, name='setup'),
                  path('register/', views_home.register_view, name='register'),
                  path('logout/', views_home.logout_view, name='logout'),
                  path('profile/', views_profile.profile_view, name='profile'),
                  path('profile/update/', views_profile.profile_update, name='profile/update'),
                  path('profile/password/', views_profile.password_view, name='profile/password'),
                  path('profile/apply', views_profile.apply, name='profile/apply')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
