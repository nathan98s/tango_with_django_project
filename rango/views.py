from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def show_category(request, category_name_slug):
        
        context_dict = {}
        try:
               
                category = Category.objects.get(slug=category_name_slug)
                
                pages = Page.objects.filter(category=category)
                
                context_dict['pages'] = pages
                
                context_dict['category'] = category
                
        except Category.DoesNotExist:

               
                
                context_dict['category'] = None
                context_dict['pages'] = None
                
        return render(request, 'rango/category.html', context_dict)


def most_viewed(request, page_name_slug):
        
        context_dict = {}

        try:
                pages = Page.objects.get(slug=page_name_slug)

                context_dict['pages'] = pages
                context_dict['views'] = view
        except: Page/DoesNotExist:
                context_dict['pages'] = None
                context_dict['views'] = None

        return render(request, 'rango
def index(request):

        
        
        category_list = Category.objects.order_by('-likes')[:5]
        context_dict = {'categories':category_list}


        mostViewed_list = Page.objects.order_by('-views')[:5]
        mostViewed_dict = {'mostViewed':mostViewed_list}



        return render(request, 'rango/index.html', context_dict, mostViewed_dict)

def about(request):

        return render(request, 'rango/about.html')




