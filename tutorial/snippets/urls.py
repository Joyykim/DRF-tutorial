from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import UserList, UserDetail, SnippetDetail, SnippetList

# router = DefaultRouter()
# router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path('', include(router.urls)),
    # url(r'^', include(router.urls, namespace="myapp")),
]
