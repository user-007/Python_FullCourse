from django.urls import path, include

import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classroom', include('classroom.urls'))
]
