from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery


from text import TEXT_START, TEXT_INFO, DEPOSIT_TEXT
from keyboards import (kb_start, kb_place_categoty,
                       kb_to_menu, kb_buy)
from database.requests import set_user


router_handler = Router()

@router_handler.message(Command('start'))
async def start_handler(message: types.Message):
    await set_user(message.from_user.id)
    await message.answer(text=TEXT_START,
                         reply_markup=kb_start,
                         disable_web_page_preview=True)

@router_handler.callback_query(F.data == 'info')
async def info_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text=TEXT_INFO,
                                  reply_markup=kb_to_menu)

@router_handler.callback_query(F.data == 'place_ads')
async def place_ads_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text='Выберите категорию:',
                                  reply_markup=kb_place_categoty)

@router_handler.callback_query(F.data == 'to_menu')
async def to_menu_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text=TEXT_START,
                                  reply_markup=kb_start,
                                  disable_web_page_preview=True)

@router_handler.callback_query(F.data == 'my_buy')
async def my_buy_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text='Воспользуйтесь меню:',
                                  reply_markup=kb_buy)

@router_handler.callback_query(F.data == 'deposit')
async def deposit_handler(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer(text=DEPOSIT_TEXT,
                                  reply_markup=kb_to_menu)