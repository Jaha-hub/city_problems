from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.executor import work_kb

executor_router = Router()


@executor_router.callback_query(F.data == "start_working")
async def start_working(callback: CallbackQuery):
    await callback.message.answer(
        "Вы начали работу.",
        reply_markup=work_kb()
    )


@executor_router.callback_query(F.data == "submit_report")
async def submit_report(callback: CallbackQuery):
    await callback.message.answer(
        "Прикрепите отчёт по выполненной задаче.",
        reply_markup=work_kb()
    )
