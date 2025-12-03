from aiogram.utils.keyboard import InlineKeyboardBuilder


def work_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Работаю", callback_data="start_working")
    kb.button(text="Отчет", callback_data="submit_report")
    kb.button(text="Назад", callback_data="get_back")

    kb.adjust(2,1)

    return kb.as_markup()
