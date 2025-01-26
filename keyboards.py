from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📚 Информация',
                          callback_data='info')],
    [InlineKeyboardButton(text='🪧 Разместить рекламный пост',
                          callback_data='place_ads')],
    [InlineKeyboardButton(text='🛍 Мои покупки/💲 Баланс',
                          callback_data='my_buy')],
    [InlineKeyboardButton(text='💳 Пополнить баланс',
                          callback_data='deposit')],
    [InlineKeyboardButton(text='🎉 Активировать купон',
                          callback_data='activate_cup')],
    [InlineKeyboardButton(text='💎 Активировать VIP💎',
                          callback_data='acivate_vip')],
    [InlineKeyboardButton(text='🎲 Выиграть 200 ₽',
                          callback_data='dice')]
])

kb_place_categoty = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💰 Продажа рекламы',
                          callback_data='sale_ads')],
    [InlineKeyboardButton(text='💼 Продажа канала',
                          callback_data='sale_chanel')],
    [InlineKeyboardButton(text='🎨 Услуги дизайнера',
                          callback_data='designer')],
    [InlineKeyboardButton(text='🏠 В главное меню',
                          callback_data='to_menu')]
])

kb_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏠 В главное меню',
                          callback_data='to_menu')]
])

kb_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💸 Пополнение баланса',
                          callback_data='to_buy')],
    [InlineKeyboardButton(text='🛒 Покупка постов',
                          callback_data='buy_post')],
    [InlineKeyboardButton(text='🏠 В главное меню',
                          callback_data='to_menu')]
])