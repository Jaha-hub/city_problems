from aiogram.utils.keyboard import InlineKeyboardBuilder


def new_request_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Создать заявку", callback_data="new_request")
    kb.button(text="Мои заявки", callback_data="my_requests")

    kb.adjust(1,1)

    return kb.as_markup()


def my_requests_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Обновить", callback_data="refresh_my_requests")
    kb.button(text="Назад", callback_data="get_back")

    kb.adjust(1,1)

    return kb.as_markup()
