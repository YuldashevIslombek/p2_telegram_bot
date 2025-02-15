import asyncio
import os

from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [
        KeyboardButton(text="Button1"),
        KeyboardButton(text="Button2"),
        KeyboardButton(text="Button3"),
        ],
        [
        KeyboardButton(text="Button4"),
        KeyboardButton(text="Button5"),
        KeyboardButton(text="Button6"),
    ]
])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Obuna bo'ling", callback_data="Text", url="t.me/stories_770_N01"),
         InlineKeyboardButton(text="Obuna bo'ling ", callback_data="Button1", url="https://www.instagram.com/yuldashevvv_770?igsh=MTg3ajc1YzdlenZmbg=="),],
        [InlineKeyboardButton(text="Obuna bo'ling", callback_data="Text", url="https://t.me/+HuPmHBfg3aliZWE6"),
         InlineKeyboardButton(text="Inline Keyboard4", callback_data="Button2"),],
        [InlineKeyboardButton(text="Inline Keyboard5", callback_data="Text"),
         InlineKeyboardButton(text="Inline Keyboard6", callback_data="Button3"),],
        [InlineKeyboardButton(text="Inline Keyboard7", callback_data="Text"),
         InlineKeyboardButton(text="Inline Keyboard8", callback_data="Button4"),],
        [InlineKeyboardButton(text="Inline Keyboard9", callback_data="Text"),
         InlineKeyboardButton(text="Inline Keyboard10", callback_data="Button5"),],
    ]
)

@dp.message(CommandStart())
async def Start(message: types.Message):
    await message.answer("Assalomu alekum!""/Menu")

@dp.message(Command("Menu"))
async def _Menu(message: types.Message):
    await message.answer("/Help /Lichkam /Kanalim /Instagram_Akauntim /Musiqalar /Rasmlar")

@dp.message(Command("Help"))
async def _Help(massage: types.Message):
    await massage.answer(f"Sizga qanaqa yordam kerak, yoki +998947104552 manashu raqamga murojat qiling!", reply_markup=inline_keyboard)

@dp.message(Command("Lichkam"))
async def _Lichkam(message: types.Message):
    await message.answer("@yuldashevvv_770")

@dp.message(Command("Kanalim"))
async def _Kanalim(message: types.Message):
    await message.answer("t.me/stories_770_N01")

@dp.message(Command("Instagram_Akauntim"))
async def _Instagram_Akauntim (message: types.Message):
    await message.answer("https://www.instagram.com/yuldashevvv_770?igsh=MTg3ajc1YzdlenZmbg==")

@dp.message(Command("Musiqalar"))
async def _Musiqalar(message: types.Message):
    await message.answer("https://open.spotify.com/")

@dp.message(Command("Rasmlar"))
async def _Rasmlar(message: types.Message):
    await message.answer("www.pinterest.ru/homefeed/")

async def main():
    print("Starts...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


