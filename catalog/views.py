from django.shortcuts import render, redirect
#from django.http import HttpResponse
from . import models
from . import handlers

# Create your views here.
def mainpage(request):
    #получаем все данные из БД
    all_categories=models.Category.objects.all()
    all_products=models.Product.objects.all()

    #получит переменную из фронт части, если оно есть
    search_value_from_front=request.GET.get('search')
    if search_value_from_front:
        all_products=models.Product.objects.filter(name__contains=search_value_from_front)


    context={'all_categories':  all_categories, 'all_products': all_products}
    return render(request, 'index.html', context)


#получит продукты из конкретной котегории
def get_category_product(request, pk):
    #получить все товары из конкретной категории
    exact_product=models.Product.objects.filter(id=pk)

    #передача из бека на фронт
    context={'category_products':exact_product}
    return render(request, 'category.html', context)

def get_exact_product(request, name, pk):
    exact_product=models.Product.objects.get(name= name, id=pk)

    context={'product': exact_product}
    return render(request, 'product.html', context)

def add_pr_to_cart(request, pk):
    quantity = request.POST.get("pr_count")
    # найти сам продукт
    product_to_add = models.Product.objects.get(id=pk)
    models.Usercart.objects.create(user_id=request.user.id, user_pr=product_to_add, user_pr_quantity=quantity)
    return redirect("/")

def user_cart(request):
    user_id=request.user.id
    product = models.Usercart.objects.filter(user_id=user_id)

    # передача из бека на фронт
    context = {'cart_products': product}
    return render(request, 'user_cart.html', context)

def delete_from_cart(request, pk):
    product_to_delete=models.Product.objects.get(id=pk)
    models.Usercart.objects.filter(user_id=request.user.id, user_pr=product_to_delete).delete()

    return redirect('/cart')

    # user_cart=models.Usercart.objects.filter(user_id=request.user.id, user_pr=pk)
    # user_cart.delete()
    # return redirect('/cart')




def complete_order(request):
    user_cart=models.Usercart.objects.filter(user_id=request.user.id)

    if request.method=='POST':
        result_message = 'Новый Заказ (Из сайта)\n\n'
        total=0
        for cart in user_cart:
            result_message+=f'Название товара__: {cart.user_pr}\n '\
                            f'Количество__: {cart.user_pr_quantity}'
            total+=cart.user_pr.price*cart.user_pr_quantity

        result_message+=f'\n\nИтог__: {total}'
        handlers.bot.send_message(652535864, result_message)
        user_cart.delete()

        return redirect('/')
    return render(request, 'user_cart.html', {'user_cart': user_cart})







