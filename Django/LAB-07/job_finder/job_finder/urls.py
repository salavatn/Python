from django.contrib import admin
from django.urls import path, include
# from app_webscrapping.views import scraping   #, page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('scraping/', scraping, name='scraping'),
    # path('page/', page, name='page'),
]


