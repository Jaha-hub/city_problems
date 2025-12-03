from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.admin import admin_menu_kb

admin_router = Router()

@admin_router.callback_query(F.data == "manage_users")
async def manage_users(callback: CallbackQuery):
    await callback.message.answer(
        "Управление пользователями.",
        reply_markup=admin_menu_kb()
    )

@admin_router.callback_query(F.data == "manage_roles")
async def manage_roles(callback: CallbackQuery):
    await callback.message.answer(
        "Управление ролями пользователей.",
        reply_markup=admin_menu_kb()
    )

@admin_router.callback_query(F.data == "view_logs")
async def view_logs(callback: CallbackQuery):
    await callback.message.answer(
        "Последние логи системы.",
        reply_markup=admin_menu_kb()
    )