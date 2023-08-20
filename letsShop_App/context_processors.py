from .models import *

def cat_context(request):
    cat = Category.objects.prefetch_related('subcategory_set__super_subcategory_set').all()
    return {'cat_menu': cat}