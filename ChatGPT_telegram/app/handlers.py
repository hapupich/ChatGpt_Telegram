from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from app.generators import gpt4
from aiogram.fsm.context import FSMContext

router = Router()

class Generate(StatesGroup):
    text = State()

#/start
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("hi! Type ur request")
    await state.clear()

# Message handler for text messages
@router.message(F.text)
async def generate(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4(message.text)
    await message.answer(response.choices[0].message.content)
    await state.clear()

@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer("wait until bot answer u")
