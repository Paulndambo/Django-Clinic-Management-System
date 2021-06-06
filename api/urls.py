from django.urls import path, include
#from .views import articles, article_details
from rest_framework.routers import DefaultRouter
from . views import ArticleViewSet #, ArticleList, ArticleDetails

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path("", include(router.urls)),
    #path("articles/", ArticleList.as_view()),
    #path("articles/<int:id>/", ArticleDetails.as_view()),
]
