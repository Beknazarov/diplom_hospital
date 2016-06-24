from django.db.models import Q
from django.http.response import Http404
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from news.models import News, CategoryNews


class CategoryListView(ListView):
    model = CategoryNews
    queryset = CategoryNews.objects.all()
    template_name = "category_list.html"


class CategoryDetailView(DetailView):
    model = CategoryNews
    template_name = "index.html"


class AllNewsView(ListView):
    model = News
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(AllNewsView, self).get_context_data(**kwargs)
        count = News.objects.count()
        context['all_news'] = News.objects.all()[count - 4:count]
        return context


class DetailNews(ListView):
    model = News
    template_name = 'news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailNews, self).get_context_data(**kwargs)
        count = News.objects.count()
        try:
            detail_news = News.objects.get(id=self.kwargs['pk'])
        except News.DoesNotExist:
            raise Http404
        context['detail_news'] = detail_news
        context['other_news'] = News.objects.filter(~Q(id=self.kwargs['pk']))[count - 4:count]
        return context


class HeadNewsOne(ListView):
    model = News
    template_name = 'detail_head_news.html'

    def get_context_data(self, **kwargs):
        context = super(HeadNewsOne, self).get_context_data(**kwargs)

        context['detail_news'] = News.objects.get(Q(id=6))

        return context


class HeadNewsTwo(ListView):
    model = News
    template_name = 'detail_head_news.html'

    def get_context_data(self, **kwargs):
        context = super(HeadNewsTwo, self).get_context_data(**kwargs)

        context['detail_news'] = News.objects.get(Q(id=7))

        return context


class PageNotFound(TemplateView):
    template_name = "404.html"
