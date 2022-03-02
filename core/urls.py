from django.urls import path
from core.views import (WebsiteEssentialCreateView, WebHtmlRetrieveView,
                        TopWordsRetrieveView, WebPageDeleteView,
                        WebPageUpdateView)

urlpatterns = [
    path('create/webpage', WebsiteEssentialCreateView.as_view(), name='create-webpage'),
    path('html/<str:website_name>', WebHtmlRetrieveView.as_view(), name='web-page-html'),
    path('delete/<str:website_name>', WebPageDeleteView.as_view(), name='web-page-delete'),
    path('update/<str:website_name>', WebPageUpdateView.as_view(), name='web-page-update'),
    path('<str:website_name>/words/<int:n>', TopWordsRetrieveView.as_view(), name='n-words')
]
