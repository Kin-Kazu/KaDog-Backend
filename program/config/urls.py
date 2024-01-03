
from django.contrib import admin
from django.urls import path, include
from .views import activate_account
from events.views import EventsAPIView
from events.views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('activation/<uidb64>/<token>/',
         activate_account, name='activate_account'),
    path('api/v1/events/', EventsAPIView.as_view(), name='events'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
]
