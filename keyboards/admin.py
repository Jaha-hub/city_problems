from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_menu_kb():
    kb = InlineKeyboardBuilder()

    kb.button(text="Управление пользователями", callback_data="manage_users")
    kb.button(text="Управление ролями", callback_data="manage_roles")
    kb.button(text="Логи действий", callback_data="view_logs")
    kb.button(text="Назад", callback_data="get_back")

    kb.adjust(3,1)

    return kb.as_markup()