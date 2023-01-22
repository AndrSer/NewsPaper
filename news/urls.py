from django.urls import path
from .views import NewsList, PostDetail, SearchNewsList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', NewsList.as_view(), name='news'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('search', SearchNewsList.as_view(), name='search_news'),
   path('create', PostCreate.as_view(), name='create_post'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='update_post'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='delete_post')
]
