from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.citizen import new_request_kb, my_requests_kb

citizen_router = Router()


@citizen_router.callback_query(F.data == "new_request")
async def new_request(callback: CallbackQuery):
    await callback.message.answer(
        "Опишите проблему и прикрепите фото.",
        reply_markup=new_request_kb()
    )


@citizen_router.callback_query(F.data == "my_requests")
async def my_requests(callback: CallbackQuery):
    await callback.message.answer(
        "Ваши заявки:",
        reply_markup=my_requests_kb()
    )
