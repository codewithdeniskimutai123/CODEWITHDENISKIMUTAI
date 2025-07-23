from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path("register_user/", views.register_user, name="register_user" ),
    path("update_user/", views.update_user_profile, name="update_user" ),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('blog_list/', views.blog_list, name="blog_list"),
    path('blogs/<slug:slug>/', views.get_blog, name="get_blog"),
    path('update_blog/<str:pk>/', views.update_blog, name="update_blog"),
    path('delete_blog/<str:pk>/', views.delete_blog, name="delete_blog"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


