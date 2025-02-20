# import asyncio
# import os
# from distutils.dep_util import newer
#
# from aiogram.filters import CommandStart, Command
# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,FSInputFile
# from dotenv import load_dotenv
# from aiogram import Bot, Dispatcher, types, F
#
#
# load_dotenv()
#
# BOT_TOKEN = os.getenv("BOT_TOKEN")
#
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher()
#
# keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
#     [
#         KeyboardButton(text="Button1"),
#         KeyboardButton(text="Button2"),
#         KeyboardButton(text="Button3"),
#         ],
#         [
#         KeyboardButton(text="Button4"),
#         KeyboardButton(text="Button5"),
#         KeyboardButton(text="Button6"),
#     ]
# ])
#
# inline_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Obuna bo'ling", callback_data="Text", url="t.me/stories_770_N01"),
#          InlineKeyboardButton(text="Obuna bo'ling ", callback_data="Button1", url="https://www.instagram.com/yuldashevvv_770?igsh=MTg3ajc1YzdlenZmbg=="),],
#         [InlineKeyboardButton(text="Obuna bo'ling", callback_data="Text", url="https://t.me/+HuPmHBfg3aliZWE6"),
#
#          InlineKeyboardButton(text="Help", callback_data="Help"),],
#         # [InlineKeyboardButton(text="Inline Keyboard5", callback_data="Text"),
#         #  InlineKeyboardButton(text="Inline Keyboard6", callback_data="Button3"),],
#         # [InlineKeyboardButton(text="Inline Keyboard7", callback_data="Text"),
#         #  InlineKeyboardButton(text="Inline Keyboard8", callback_data="Button4"),],
#         # [InlineKeyboardButton(text="Inline Keyboard9", callback_data="Text"),
#         #  InlineKeyboardButton(text="Inline Keyboard10", callback_data="Button5"),],
#     ]
# )
#
# @dp.message(CommandStart())
# async def Start(message: types.Message):
#     await message.answer("Do'konimizga Xush kelibsiz !""/Menu")
#
# @dp.message(Command("Menu"))
# async def _Menu(message: types.Message):
#     await message.answer("/Help /Lichkam /Kanalim /Instagram_Akauntim /Musiqalar /Rasmlar")
#
# @dp.message(Command("Help"))
# async def _Help(massage: types.Message):
#     await massage.answer(f"Sizga qanaqa yordam kerak, yoki +998947104552 manashu raqamga murojat qiling!", reply_markup=inline_keyboard)
#
# @dp.message(Command("Lichkam"))
# async def _Lichkam(message: types.Message):
#     await message.answer("@yuldashevvv_770")
#
# @dp.message(Command("Kanalim"))
# async def _Kanalim(message: types.Message):
#     await message.answer("t.me/stories_770_N01")
#
# @dp.message(Command("Instagram_Akauntim"))
# async def _Instagram_Akauntim (message: types.Message):
#     await message.answer("https://www.instagram.com/yuldashevvv_770?igsh=MTg3ajc1YzdlenZmbg==")
#
# @dp.message(Command("Musiqalar"))
# async def _Musiqalar(message: types.Message):
#     await message.answer("https://open.spotify.com/")
#
# @dp.message(Command("Rasmlar"))
# async def _Rasmlar(message: types.Message):
#     await message.answer("www.pinterest.ru/homefeed/")
#
# #rasm yasaw
# @dp.message(F.photo)
# async  def get_image(msg: types.Message):
#
#     await msg.answer_photo(msg.photo[-1].file_id, caption="Bu qanaqa rasm")
#
# @dp.message(F.text == "Yordam")
# async def _filter(massage: types.Message):
#     await massage.answer(f"Nima yordam kerak")
#
# @dp.callback_query(F.data == "Help")
# async def get_callback_query(callback: types.CallbackQuery):
#     await callback.answer(f"nima yordam kerak")
# #rasm yasaw
# @dp.message(Command("images"))
# async def get_image(msg: types.Message):
#      img = FSInputFile("images/img.png")
#      await msg.answer_photo(img, caption = "Bu screenshot")
# #video yasaw
# @dp.message(Command("video"))
# async def get_image(msg: types.Message):
#      vid = FSInputFile("videos/vid.mp4")
#      await msg.answer_video(vid, caption = "Bu screenshot")
#
#
#
# async def main():
#     print("Starts...")
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
import os

from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from keyboards import register_inl_btn, get_phone_btn
from states import UserRegisterState

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()




@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Do'konimizga xush kelibsiz!\n"
                         "Ro'yxatdan o'ting!", reply_markup=register_inl_btn)



@dp.message(Command("help"))
async def _help(message: types.Message):
    await message.answer("Help")


@dp.message(Command("images"))
async def get_image(msg: types.Message):
    img = FSInputFile("images/img.png")
    await msg.answer_photo(img, caption="Bu screenshot")


@dp.message(Command("videos"))
async def get_video(msg: types.Message):
    video = FSInputFile("videos/20250218-0428-29.7812879.mp4")
    await msg.answer_video(video, caption="Bu screenrecorder")


@dp.message(F.video)
async def get_video(msg: types.Message):
    await msg.answer("Video uchun rahmat")


@dp.callback_query(F.data == "/register")
async def user_register(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserRegisterState.full_name)
    await call.message.answer("Ismingizni kiriting:")

@dp.message(UserRegisterState.full_name)
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await state.set_state(UserRegisterState.phone_number)
    await msg.answer("Telefon raqamingizni kiriting: ", reply_markup=get_phone_btn)

@dp.message(UserRegisterState.phone_number)
async def get_phone_number(msg: types.Message, state: FSMContext):
    if msg.text:
        await state.update_data(phone_number=msg.text)
    elif msg.contact.phone_number:
        await state.update_data(phone_number=msg.contact.phone_number)
    await state.set_state(UserRegisterState.age)
    await msg.answer("Yoshingizni kiriting:")


@dp.message(UserRegisterState.age)
async def get_age(msg: types.Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await state.set_state(UserRegisterState.address)
    await msg.answer("Addresingizni kiriting:")

@dp.message(UserRegisterState.address)
async def get_address(msg: types.Message, state: FSMContext):
        await state.update_data(address=msg.text)
        data = await state.get_data()
        await msg.answer(f"Ism: {data['full_name']}\n"
                         f"Telefon: {data['phone_number']}\n"
                         f"age: {data['age']}\n"
                         f"address: {data['address']}")


async def main():
    print("Starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


