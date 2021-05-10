from django.db.models import Q
from django.views.generic import ListView, DetailView

from posts.models import NewsModel


class NewsView(ListView):
    template_name = 'index.html'
    model = NewsModel
    paginate_by = 3

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        q = self.request.GET.get('q', '')
        if q:
            return NewsModel.objects.filter(Q(title__icontains=q) |
                                            Q(comment__icontains=q)
                                            )
        if pk:
            return NewsModel.objects.filter(category_id=pk).order_by('-pk')
        else:
            return NewsModel.objects.order_by('-pk')


class DetailView(DetailView):
    template_name = 'detail.html'
    model = NewsModel
