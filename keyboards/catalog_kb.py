from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_skirts = KeyboardButton(text="Юбки и саронги")
button_dresses = KeyboardButton(text="Платья и сарафаны")
button_blouses = KeyboardButton(text="Блузы, лонгсливы и топы")
button_pants = KeyboardButton(text="Брюки и джинсы")
button_outerwear = KeyboardButton(text="Верхняя одежда")
button_bags = KeyboardButton(text="Сумки")
button_accessories = KeyboardButton(text="Аксессуары")
button_back = KeyboardButton(text="Назад")


catalog_menu = ReplyKeyboardMarkup(keyboard=[
    [button_skirts, button_dresses],
    [button_blouses, button_pants],
    [button_outerwear, button_bags],
    [button_accessories, button_back],
], resize_keyboard=True)
