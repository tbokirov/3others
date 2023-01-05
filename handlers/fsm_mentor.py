from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    course = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.id.set()
        await message.answer('Введите id студента', reply_markup=client_kb.cancel_markup)
    else:
        await message.answer('Пишите в лс!')


async def load_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Недопустимые символы')
    elif int(len(message.text)) < 9 or int(len(message.text)) > 9:
        await message.answer('Неправильное id!')
    else:
        async with state.proxy() as data:
            data['id'] = message.text
        await FSMAdmin.next()
        await message.answer('Введите имя студента')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Направление студента', reply_markup=client_kb.courses_markup)


async def load_course(message: types.Message, state: FSMContext):
    if message.text.lower() in client_kb.courses_markup:
        await message.answer('Такого направления нет!')
    else:
        async with state.proxy() as data:
            data['course'] = message.text
        await FSMAdmin.next()
        await message.answer('Введите возраст студента')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Введите числа')
    elif int(message.text) < 5 or int(message.text) > 100:
        await message.answer('Возрастное ограничение!')
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Группа студента')


async def load_group(message: types.Message, state: FSMContext):
    if not message.text.isdigit() and message.text.isalnum():
        await message.answer('Введите правильно и только числа!')
    else:
        async with state.proxy() as data:
            data['group'] = message.text
            await message.answer(f"ID: {data['id']} \nИмя: {data['name']} \nНаправление: {data['course']} "
                                 f"\nВозраст: {data['age']} \nГруппа: {data['group']}")
        await FSMAdmin.next()
        await message.answer('Данные верны?', reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await state.finish()
        await message.answer('Ментор зарегистрирован!')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Регистрация отменена!')
    else:
        await message.answer('Введите корректные данные!')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Регистрация отменена')


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['Отменить регистрацию'])
    dp.register_message_handler(cancel_fsm, Text(equals='Отменить регистрацию', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['register'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_course, state=FSMAdmin.course)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
