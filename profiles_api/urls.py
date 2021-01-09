from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
# because the router will create all of the four URLs for us, we don't ned to specify a forward slash
#base_name='hello-viewset' is used for retrieving the URLs in our router. If we ever need to do that using the URL retrieving function provided by Django

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
#as you register new routes with the router, it generates a list of URLs that are associated for our ViewSet. It figures out the URLs that are required for all of the functions that we add to our ViewSet, and then it generates the 'urls' list available at router.urls.
#The reason the above path is '' is because we don't want to add a prefix to the 'urls'