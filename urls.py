from os import path
from .import views

urlpatterns = [
    path('my_app/', views.index, name='index')
    path('admin/', admin.site.urls)
]

