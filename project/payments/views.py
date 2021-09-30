from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
# run command pip instal stripe
#create account in stripe
#add secret key and publish key in setting.py
class HomePageView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge=stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gatway',
            source=request.POST['stripeToken']

        )