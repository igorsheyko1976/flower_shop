from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Bouquet, Order
from .telegram_bot import send_order_to_telegram


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bouquets/register.html', {'form': form})


def bouquet_list(request):
    bouquets = Bouquet.objects.filter(available=True)
    return render(request, 'bouquets/bouquet_list.html', {'bouquets': bouquets})


@login_required
def order_bouquet(request, bouquet_id):
    bouquet = get_object_or_404(Bouquet, id=bouquet_id)
    if request.method == 'POST':
        delivery_address = request.POST['delivery_address']
        delivery_date = request.POST['delivery_date']
        comment = request.POST.get('comment', '')

        order = Order.objects.create(
            user=request.user,
            bouquet=bouquet,
            delivery_address=delivery_address,
            delivery_date=delivery_date,
            comment=comment
        )

        send_order_to_telegram(order.id)
        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'bouquets/order_form.html', {'bouquet': bouquet})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'bouquets/order_confirmation.html', {'order': order})
