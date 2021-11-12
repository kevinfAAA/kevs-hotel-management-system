from django.urls import path
from . import views
urlpatterns = &#91;
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_room,name="add_room"),
    path('update/&lt;int:room_no&gt;/',views.update_room,name="update_room"),
 
]