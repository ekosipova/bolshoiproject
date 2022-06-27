from .forms import FeedbackForm
from .models import Feedback
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView

class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'review/form.html'
    success_url = 'done'

class DoneView(TemplateView):
    template_name = 'review/done.html'


class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'review/form.html'
    success_url = 'done'


class ListFeedBack(ListView):
    template_name = 'review/list.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        quryset = super().get_queryset()
        return quryset

