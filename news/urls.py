from django.conf.urls import url

from news.views import AllNewsView, DetailNews, CategoryListView, CategoryDetailView, HeadNewsTwo, HeadNewsOne

urlpatterns = [
    url(r'^$', AllNewsView.as_view(), name='all-news'),
    url(r'^head/1/$', HeadNewsOne.as_view(), name='head-news-1'),
    url(r'^head/2/$', HeadNewsTwo.as_view(), name='head-news-2'),
    url(r'^(?P<pk>\d+)/$', DetailNews.as_view(), name='all-detail-news'),
    url(r'^category/$', CategoryListView.as_view(), name='categories'),
    url(r'^(?P<slug>[\w\-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^(?P<slug>[\w\-]+)/(?P<pk>\d+)/$', DetailNews.as_view(), name='news_detail'),
]
