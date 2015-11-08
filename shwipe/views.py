from django.views.generic.list import ListView
from django.utils import timezone

from .models import Product

class ProductListView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    paginated_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        
        