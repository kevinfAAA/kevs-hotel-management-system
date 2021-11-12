from django.urls import path
from . import views
urlpatterns=&#91;
    path('',views.dashboard,name='user_dashboard'),
    path('details/&lt;int:id&gt;/&lt;int:booking_id&gt;',views.details,name='user_details')
]