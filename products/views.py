from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib import messages

from .models import Product, Category
from cart.contexts import cart_contents

import json
import math


def check_product_in(the_list, key):
    """ Function to check if a product exists in a list """

    for item in the_list:
        if item['product_id'] == str(key):
            return True


def create_review_stars(rating):
    """ Generate the HTML to show the rating stars """

    rated_out_of = 5
    star_yellow = star_half = star_grey = 0

    if float(rating).is_integer():
        star_yellow = int(rating)
        star_half = 0
        star_grey = 5 - int(rating)
    else:
        rating_floor = math.floor(rating)
        star_yellow = int(rating_floor)
        star_half = 1
        star_grey = (rated_out_of - 1) - int(rating_floor)

    html = ''.join('<i class="fas fa-star rating__star"></i>' * star_yellow)
    if star_half > 0:
        html += '<span class="fa-stack">'
        html += '<i class="fas fa-star-half-alt rating__none fa-stack-1x"></i>'
        html += '<i class="fas fa-star-half rating__star fa-stack-2x"></i>'
        html += '</span>'
    html += ''.join('<i class="far fa-star rating__none"></i>' * star_grey)

    return html


def products(request):
    """ A view to show all the products """

    default_sort = 'date_created'
    main_title = 'all products'
    categories = None
    show = None
    search_text = None

    if 'show' in request.GET:
        show = request.GET['show']

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = Product.objects.filter(
                category__name__in=categories).order_by(
                    'category', default_sort)
            categories = Category.objects.filter(name__in=categories)

            if len(categories) == 1:
                main_title = categories[0].display_name
            else:
                main_title = show

            if main_title == 'invitations':
                for cat in categories:
                    cat.display_name = cat.display_name.rpartition(' ')[0]

        elif show == 'featured':
            products = Product.objects.filter(
                featured=True).order_by('category', default_sort)
            main_title = 'featured products'

        elif show == 'new':
            products = Product.objects.order_by('-date_created')[:4]
            main_title = 'new products'

        elif 'search-text' in request.GET:
            search_text = request.GET['search-text']
            if not search_text:
                return redirect(reverse('products'))

            text_query = Q(
                name__icontains=search_text) | Q(
                    description__icontains=search_text)

            products = Product.objects.all().filter(
                text_query).order_by(default_sort)

    else:
        products = Product.objects.all().order_by(default_sort)

    context = {
        'products': products,
        'main_title': main_title,
        'search_text': search_text,
        'categories': categories,
        'opts': Product.ProductAdminOpts(),
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """ A view to show a products details """

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request,
                       'Sorry that product cannot be found',
                       extra_tags='product error')

        return redirect('products')

    else:
        context = {
                'product': product,
                'rating_html': create_review_stars(product.average_rating),
                'opts': Product.ProductAdminOpts(),
        }

        current_shopping_cart = cart_contents(request)
        original_cart = current_shopping_cart['cart_items']
        if check_product_in(original_cart, product_id):
            context['exists_in_cart'] = True

        if product.customizable:
            invite_data = list(product.customlines.all().values(
                'name', 'text', 'y_pos', 'font',
                'raw_size', 'color', 'stroke_fill', 'stroke_width'))
            context['invite_data'] = json.dumps(invite_data)

        return render(request, 'products/product_info.html', context)
