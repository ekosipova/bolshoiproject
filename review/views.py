from .forms import FeedbackForm
from .models import Feedbacks
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,FormView


class ReviewPage(FormView):
    form_class = FeedbackForm
    template_name = 'review/review.html'
    success_url = 'done'

    def form_valid(self, form):
        form.save()
        return super(ReviewPage,self).form_valid(form)


class DoneView(TemplateView):
    template_name = 'review/done.html'


