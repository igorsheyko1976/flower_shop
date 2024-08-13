import telegram
from django.conf import settings
from .models import Order


# Создаем экземпляр бота
bot = telegram.Bot(token='7141584173:AAGTxT7xVELkhpmCGYUWGmtz4t2dRz8m8hg')

def send_order_to_telegram(order_id):
    order = Order.objects.get(id=order_id)
    bouquet = order.bouquet

    message = (
        f"Новый заказ!\n\n"
        f"Букет: {bouquet.name}\n"
        f"Цена: {bouquet.price} руб.\n"
        f"Адрес доставки: {order.delivery_address}\n"
        f"Дата и время доставки: {order.delivery_date}\n"
        f"Комментарий: {order.comment}"
    )

    # Отправляем сообщение в Telegram
    bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

    # Отправляем изображение букета
    if bouquet.image:
        bot.send_photo(chat_id='YOUR_CHAT_ID', photo=open(bouquet.image.path, 'rb'))
