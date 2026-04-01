from django.urls import path
from .views import NewsListAPIView, NewsRetrieveAPIView

urlpatterns = [
    path('', NewsListAPIView.as_view(), name="main_page"),
    path('<int:pk>/', NewsRetrieveAPIView.as_view(), name="news_detail_page"),
]
