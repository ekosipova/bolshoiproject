from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback


def form_review(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = Feedback (
                realm = form.cleaned_data['realm'],
                name = form.cleaned_data['name'],
                rating = form.cleaned_data['rating'],
                feedback = form.cleaned_data['feedback']
            )
            feed.save()
            return HttpResponseRedirect('done')
    else:
        form = FeedbackForm()
    return render(request,'review/form.html',context={'form':form})

def done(request):
    return render(request,'review/done.html' )