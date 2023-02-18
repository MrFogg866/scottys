from django.shortcuts import render, redirect
from newsletter.forms import NewsletterSubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.save()
            return redirect('thank_you')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})


def thank_you(request):
    return render(request, 'newsletter/thank_you.html')
