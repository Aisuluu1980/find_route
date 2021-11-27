from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView',
)

def home(request, pk=None):
    # if pk:
        # city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk)
        # city = get_object_or_404(City, id=pk)
        # context = {'object':city}
        # return render(request, 'cities/detail.html', context)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form':form}
    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    # если success_url не указываю обязаьельно в model py прописываем функцию absolute_url
    success_url = reverse_lazy('cities:home')

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

class CityDeleteView(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    # если удаление без подтверждения, сразу удаляет, template  тогда не указываю
    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)
