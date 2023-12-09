from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.mail import send_mail


def index(request):
    """View function for home page of site."""
    num_category = Category.objects.all().count()
    num_product = Product.objects.all().count()

    # Number of visits to this view, as counted in the session variable.

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_category': num_category,
        'num_product': num_product,
        'num_visits': num_visits,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


subject = '{}, the email subject’.format(“this can be a form field value or user info”)'
message = 'this is the message "{}".format(“this is any message you want to send”)'


def user(request):
    user = request.user  # request was passed to the method as a parameter for the view
    user_email = user.email  # pull user’s email out of the user record
    # try to send the e-mail – note you can send to multiple users – this just sends
    # to one user.
    try:
        send_mail(subject, message, 'yourEmailAddress@gmail.com', [user_email])
        sent = True
    except:
        print("Error sending e-mail")
