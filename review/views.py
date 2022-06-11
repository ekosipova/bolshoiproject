from django.shortcuts import render
from django.http import HttpResponseRedirect


def form_review(request):
    if request.method == 'POST':
        name = request.POST['name']
        feedback = request.POST['feedback']
        print(name,feedback)
        return HttpResponseRedirect('done')
    return render(request,'review/form.html')

def done(request):
    return render(request,'review/done.html' )