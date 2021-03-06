from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import ProfileForm


def user_profile(request):
    """ Show users profile, order history and reviews made """

    try:
        profile = User.objects.get(username=request.user)
    except User.DoesNotExist:
        messages.error(request, 'Cannot display user profile: Not logged-in \
                                or User not found',
                                extra_tags='user')
        return redirect('home')

    else:
        if request.POST:
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your user profile was successfully \
                                          updated',
                                          extra_tags='user')
            else:
                messages.error(request, 'Profile update failed,  please \
                                        double-check your form and retry.',
                                        extra_tags='user')
        else:
            form = ProfileForm(instance=profile)

        order_history = profile.order_history.all()
        product_reviews = profile.user_reviews.all()
        context = {
            'form': form,
            'order_history': order_history,
            'product_reviews': product_reviews,
        }

        return render(request, 'profiles/profile.html', context)
