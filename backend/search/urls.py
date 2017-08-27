from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from search import views

router = routers.DefaultRouter()
router.register(r'berkeley-classes', views.BerkeleyClassViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Bear Search API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
