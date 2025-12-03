from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.moderator import review_requests_kb, assign_executor_kb

moderator_router = Router()


@moderator_router.callback_query(F.data == "review_requests")
async def review_requests(callback: CallbackQuery):
    await callback.message.answer(
        "Заявки на проверке.",
        reply_markup=review_requests_kb()
    )


@moderator_router.callback_query(F.data == "assign_executor")
async def assign_executor(callback: CallbackQuery):
    await callback.message.answer(
        "Назначьте исполнителя для этой задачи.",
        reply_markup=assign_executor_kb()
    )
