from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


def index(request):
    tl = TL.objects.all()
    context = {'tl': tl}
    return render(request, 'app/index.html', context)


# def routes(request):
#     return render(request, 'app/routes.html')


# def outfit(request):
#     return render(request, 'app/outfit.html')

class RoutesList(ListView):
    # '''Все маршруты'''
    model = Rs
    queryset = Rs.objects.all()
    template_name = 'app/routes.html'

# def detail(request):
#     rs = Rs.objects.all()
#     context = {'rs': rs}
#     return render(request, 'app/detail.html', context)

class RoutesDetail(DetailView):
    # '''Подробно о маршруте'''
    model = Rs
    context_object_name = 'route'
    template_name = 'app/detail.html'

class OutfitDetail(DetailView):
    model = Outfit
    context_object_name = 'outfit'
    template_name = 'app/outfit.html'

# class RubricsList(ListView):
#     # '''Рубрики'''
#     model = Rubrics
#     # model = Outfit
#     queryset = Rubrics.objects.all()
#     template_name = 'app/rubrics.html'

class RubricsView(TemplateView):
    template_name = 'app/rubrics.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['out'] = Outfit.objects.all()
        context['rubrics'] = Rubrics.objects.all()
        return context


class RubricsDetail(ListView):
    # '''Все статьи рубрики'''
    template_name = 'app/rubric_detail.html'
    context_object_name = 'rbs'

    def get_queryset(self):
        return Outfit.objects.filter(rubrics=self.kwargs['rubrics_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubrics.objects.all()
        context['current_rubrics'] = Rubrics.objects.get(pk=self.kwargs['rubrics_id'])
        return context

