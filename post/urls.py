from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from post import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/update/', views.update),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
