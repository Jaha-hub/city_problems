from aiogram.utils.keyboard import InlineKeyboardBuilder


def review_requests_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Просмотреть заявки", callback_data="review_requests")
    kb.button(text="Назад", callback_data="get_back")

    kb.adjust(1, 1)

    return kb.as_markup()


def assign_executor_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Назначить исполнителя", callback_data="assign_executor")
    kb.button(text="Назад", callback_data="get_back")

    kb.adjust(1, 1)

    return kb.as_markup()
