import os
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from clothing_store_bot.keyboards.main_menu_kb import main_menu

router = Router()


class Feedback(StatesGroup):
    waiting_for_feedback = State()


@router.message(lambda message: message.text == "Оставить отзыв")
async def ask_for_feedback(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста, напишите ваш отзыв.")
    await state.set_state(Feedback.waiting_for_feedback)


@router.message(Feedback.waiting_for_feedback)
async def receive_feedback(message: types.Message, state: FSMContext):
    feedback_text = message.text
    feedback_dir = 'feedbacks'
    if not os.path.exists(feedback_dir):
        os.makedirs(feedback_dir)

    with open(os.path.join(feedback_dir, 'feedback.txt'), 'a', encoding='utf-8') as file:
        file.write(f"{message.from_user.username}: {feedback_text}\n")

    await message.answer("Спасибо за ваш отзыв!", reply_markup=main_menu)
    await state.clear()
