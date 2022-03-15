from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('newprofile/',views.profile,name ='profile'),
    re_path('showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
    path('image', views.add_image, name='upload_image'),
    path('search',views.search, name='search'),
    path('comment/<int:image_id>', views.comment, name='comment'),
    path('like/<int:image_id>', views.like, name='like'),
    path('follow/<int:user_id>', views.follow, name='follow'),

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)