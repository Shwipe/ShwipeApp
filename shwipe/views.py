from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from .models import Shwipe
from .forms import ShwipeForm

def shwipe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShwipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/checkout/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShwipeForm()

    return render(request, 'products/index.html', {'form': form})

class SimplifyCharge(TemplateView):
    template_name = 'paymentForm.html'
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        import simplify
 
        import os
        os.getenv('SIMPLIFY_API_PUBLIC_KEY') # get env var in python: http://stackoverflow.com/questions/4906977/how-to-access-environment-variables-from-python
        os.getenv('SIMPLIFY_API_PRIVATE_KEY')
        
        # there is two type of payment by token or by Credit Card details
        # which one you gonna use?
        payment = simplify.Payment.create({
                "amount" : "1000",
                "token" : "[TOKEN ID]",
                "description" : "payment description",
                "reference" : "7a6ef6be31",
                "currency" : "USD"
         
        })
         
        if payment.paymentStatus == 'APPROVED':
            print "Payment approved"
        
        return self.render_to_response(context)


class GetShwipeView(TemplateView):
    template_name = 'shwipe.html'
    model = Shwipe

class ProductListView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    paginated_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        
        