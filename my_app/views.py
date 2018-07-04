from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext as _

from my_app.forms import DemoCreateForm
from my_app.models import Demo


class DemoMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Demo


class DemoCreateView(DemoMixin, CreateView):
    success_message = _('Successfully created')
    success_url = reverse_lazy('home')
    template_name = 'demo/create.html'
    form_class = DemoCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DemoListView(DemoMixin, ListView):
    context_object_name = 'demos'
    template_name = 'demo/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Demo.objects.filter(owner=self.request.user)

