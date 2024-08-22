from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_1 = KeyboardButton(text="Каталог")
button_2 = KeyboardButton(text="Оформить заказа")
button_3 = KeyboardButton(text="Оставить отзыв")
button_4 = KeyboardButton(text="Оформить предзаказ")


main_menu = ReplyKeyboardMarkup(keyboard=[[button_1, button_2], [button_3, button_4]],
                                resize_keyboard=True)

