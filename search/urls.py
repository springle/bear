from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ... the rest of the urlpatterns ...
    # must be catch-all for pushState to work
    url(r'^', views.FrontendAppView.as_view()),
]
