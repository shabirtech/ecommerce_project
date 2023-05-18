from django.urls import path
from items.views import detail, new,delete, edit, items

app_name = 'items'
urlpatterns = [
    path("", items, name="items"),
    path("<int:pk>/", detail, name='detail'),
    path("<int:pk>/delete/", delete, name='delete'),
    path("<int:pk>/edit/", edit, name='edit'),
    path("new/", new, name='new'),
]
