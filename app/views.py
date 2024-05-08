
from django.views.generic import TemplateView
from catalog.models import Slider
import logging
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO)

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        logging.info('Current server time: %s', datetime.now())
        return context