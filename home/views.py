from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from django.http import JsonResponse
import re
from .models import SubscribedUsers
from .forms import ReviewForm, NewsletterSubscriptionForm
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)@\w+([-.]\w+)\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res   



def index(request):
    reviews = Review.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            
            # Get the selected product, if any
            product_id = request.POST.get('product')
            if product_id:
                product = Product.objects.get(id=product_id)
                review.product = product
            
            review.save()
            form.save_m2m()  # Save many-to-many relationships
            form = ReviewForm(user=request.user)
    else:
        form = ReviewForm(user=request.user)
    context = {'reviews': reviews, 'form': form, 'products': products}
    return render(request, 'home/index.html', context)


@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user

            # Get the selected product, if any
            product_id = request.POST.get('product')
            if product_id:
                product = Product.objects.get(id=product_id)
                review.product = product
            
            review.save()
            form.save_m2m()
            
            return redirect('home')
    else:
        form = ReviewForm(user=request.user)

    reviews = Review.objects.all()
    return render(request, 'home/index.html', {'reviews': reviews, 'form': form})


@login_required
def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user

            # Get the selected product, if any
            product_id = request.POST.get('product')
            if product_id:
                product = Product.objects.get(id=product_id)
                review.product = product

            review.save()
            form.save_m2m()
            
            return redirect('home')
    else:
        form = ReviewForm(instance=review, user=request.user)

    context = {'form': form}
    return render(request, 'home/index.html', context)


@login_required
def delete_review(request, review_id):
    review_obj = get_object_or_404(Review, id=review_id)
    if review_obj.user != request.user:
        raise Http404
    review_obj.delete()
    return redirect('home')


@login_required
def subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'home/subscribe.html', {'form': form})
