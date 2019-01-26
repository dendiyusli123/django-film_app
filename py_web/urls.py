# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import film_app.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(
        film_app.urls, namespace = 'film_app'
    )),

]
