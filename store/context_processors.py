from .models import Category


def categories(request):
    top_level_categories = Category.objects.filter(parent=None)  # Categories without a parent
    parent_and_child_categories = Category.objects.exclude(parent=None).exclude(parent__parent=None)
    child_categories = Category.objects.exclude(parent=None).filter(parent__parent=None)

    return {
        'top_level_categories': top_level_categories,
        'parent_and_child_categories': parent_and_child_categories,
        'child_categories': child_categories,
    }

# from .models import Category


# def categories(request):
#     return {"categories": Category.objects.filter(level=0)}


    # categories = Category.objects.filter(level=0)
    # categories1 = Category.objects.filter(level=1)
    # categories2 = Category.objects.filter(level=2)
    # context ={
    #     "categories":categories,
    #     "categories1":categories1, 
    #     "categories2":categories2
    # }
    # return context
