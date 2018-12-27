from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .tokens import account_activation_token
from .forms import SignupForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account!'
            message = render_to_string('email_account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': user.pk,
                'token': account_activation_token.make_token(user)
            })
            to_mail = form.cleaned_data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_mail]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete your registration.')
    else:
        form = SignupForm()
    return render(request, 'email_account/signup.html', {'form': form})


def activate(request, uid, token):
    print("uid", uid)
    print("token", token)
    try:
        uid = uid
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('articles:list')
    else:
        return HttpResponse("Activation link is invalid!")
