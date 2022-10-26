from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from about.forms import ContactForm

from .models import Contact


class AboutAuthorView(TemplateView):
    success_url = reverse_lazy('games:index')
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    success_url = reverse_lazy('games:index')
    template_name = 'about/tech.html'


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('games:index')
    form_class = ContactForm

    def form_valid(self, form):
        return super().form_valid(form)
