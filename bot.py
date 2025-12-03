from aiogram import Bot, Dispatcher
from config import TOKEN
from middlewares.logging import LoggingMiddleware
from middlewares.auth import AuthMiddleware
from middlewares.role_check import RoleCheckMiddleware
from middlewares.ban_check import BanCheckMiddleware
from routers.start import router as start
from routers.order import router as order
from routers.settings import router as settings

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.middlewares.setup(LoggingMiddleware())
dp.middlewares.setup(AuthMiddleware())
dp.middlewares.setup(RoleCheckMiddleware())
dp.middlewares.setup(BanCheckMiddleware())

dp.include_router(start)
dp.include_router(order)
dp.include_router(settings)

async def on_start():
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
