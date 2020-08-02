from django.urls import (
    include, 
    path
)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_frameworks.urls', namespace='rest_framework'))
]