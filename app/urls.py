from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
path('',views.index,name='home'),
path('login/',views.login,name='login'),
path('signup/',views.signup,name='signup'),
path('logout/',views.logout,name='logout'),
path('movie/<str:pk>/',views.movie,name='movie'),
path('mylist',views.mylist,name='mylist'),
path('addlist/',views.addlist,name='addlist'),
path('remove/',views.remove,name='remove'),
path('genre/<str:pk>/',views.genere,name='genre'),
path('search/',views.search,name='search'),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)