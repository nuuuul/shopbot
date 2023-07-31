from aiogram import types, Dispatcher
from create_bot import bot, dp
from config import t_shirt_size, hudi_size, goods_photo
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentTypes
import drive_manager as dm
import sheet_management as sm
from keyboards import client_kb as kb
from utils import TestStates
import data_base as db
import json

photos_sub = ['', '', '', '']
photos_uf = ['', '']
index = 0
photo_data = ''

def update_messagesjson():
    with open('messages.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    MESSAGES = data
    return MESSAGES

# ========================================= Хендлер обработки команды /start====================
async def command_start(message: types.Message):
    #db.delete_id(message.from_user.id)
    await bot.send_message(message.from_user.id, update_messagesjson()['start'], reply_markup=kb.state2)
    print(message.from_user.id)


# ----------------КОЛБЕКИ СТАРТА----------------------
async def start_call(callback: types.CallbackQuery):
    db.delete_id(callback.from_user.id)
    await callback.message.answer(text=update_messagesjson()['start'], reply_markup=kb.state2)
    await callback.message.delete()


async def show_goods_call(callback: types.CallbackQuery):
    db.insert_id(callback.from_user.id)
    db.insert_name(callback.from_user.id, callback.from_user.username)
    await callback.message.answer(text=update_messagesjson()['goods_list'], reply_markup=kb.state3)
    await callback.message.delete()


async def no_call(callback: types.CallbackQuery):
    await callback.message.answer(text=update_messagesjson()['goodbye'], reply_markup=kb.state1)
    await callback.message.delete()


async def shopper_back_to_goods_call(callback: types.CallbackQuery):
    await callback.message.answer(text=update_messagesjson()['t_shirt_color'], reply_markup=kb.shopper_color)
    await callback.message.delete()


async def back_to_shopper_color_call(callback: types.CallbackQuery):
    await callback.message.answer(text=update_messagesjson()['t_shirt_color'], reply_markup=kb.shopper_color)
    await callback.message.delete()


async def cup_back_to_type_call(callback: types.CallbackQuery):
    await callback.message.answer(text=update_messagesjson()['cup_type'], reply_markup=kb.cup_type)
    await callback.message.delete()




async def back_to_pass_type_call(callback: types.CallbackQuery):
    await callback.message.answer(text=update_messagesjson()['pass_type'], reply_markup=kb.pass_type)
    await callback.message.delete()


async def back_to_pass_sub_color_call(callback: types.CallbackQuery):
    global index
    index = 0
    await callback.message.answer(text=update_messagesjson()['pass_color_sub'], reply_markup=kb.pass_sub_type)
    await callback.message.delete()


async def back_to_pass_uf_color_call(callback: types.CallbackQuery):
    global index
    index = 0
    await callback.message.answer(text=update_messagesjson()['pass_color_uf'], reply_markup=kb.pass_uf_type)
    await callback.message.delete()


async def back_to_t_shirt_size(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'), caption=update_messagesjson()['t_shirt'], reply_markup=kb.state5)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async  def back_to_notebook_size(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'),
                         caption=update_messagesjson()['notebook'] + '\n'
                                 + 'Выберите размер:', reply_markup=kb.notebook_size)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)

# ---------------------------------------------------------------------------------------------
# =============================================================================================   


# меню вещей:
async def t_shirt_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Футболка')
    await callback.message.answer(text=update_messagesjson()['t_shirt_color'], reply_markup=kb.state4)
    await callback.message.delete()


async def notebook_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Блокнот')
    await callback.message.answer(text=update_messagesjson()['notebook_type'], reply_markup=kb.notebook_type)
    await callback.message.delete()


async def passport_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Обложка для паспорта')
    await callback.message.answer(text=update_messagesjson()['pass_type'], reply_markup=kb.pass_type)
    await callback.message.delete()


async def cardholder_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Картхолдер')
    await callback.message.answer(text=update_messagesjson()['cardholder_type'], reply_markup=kb.cardholder_type)
    await callback.message.delete()


async def hudi_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Худи')
    await callback.message.answer(text=update_messagesjson()['hudi_color'], reply_markup=kb.hudi_color)
    await callback.message.delete()


async def shopper_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Шоппер')
    await callback.message.answer(text=update_messagesjson()['shopper_color'], reply_markup=kb.shopper_color)
    await callback.message.delete()


async def shopper_back_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'), caption=update_messagesjson()['shopper'] +
                                                               '\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.shopper_back)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cup_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Кружка')
    await callback.message.answer(text=update_messagesjson()['cup_type'], reply_markup=kb.cup_type)
    await callback.message.delete()


async def canvas_photo_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Холст')
    photo = open(goods_photo['canvas'], 'rb')
    await bot.send_photo(callback.from_user.id, photo, caption=update_messagesjson()['canvas'] + '\n' + update_messagesjson()['canvas_size'],
                         reply_markup=kb.canvas_size)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def badges_photo_call(callback: types.CallbackQuery):
    db.insert_goods(callback.from_user.id, 'Значки')
    photo = open(goods_photo['insignia'], 'rb')
    await bot.send_photo(callback.from_user.id, photo, caption=update_messagesjson()['insignia'], reply_markup=kb.badges_size)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def pillow_photo_call(callback: types.CallbackQuery):
    photo = open(goods_photo['pillow'], 'rb')
    await bot.send_photo(callback.from_user.id, photo, caption=update_messagesjson()['pillow'] + '\n\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.pillow_info)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def mousepad_photo_call(callback: types.CallbackQuery):
    photo = open(goods_photo['mouse_pad'], 'rb')
    await bot.send_photo(callback.from_user.id, photo,
                         caption=update_messagesjson()['mouse_pad_description'] + '\n\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.mouse_pad_info)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


# ===============================================Выбор цвета/типа===========================================================================================

async def t_shirt_color_call(callback: types.CallbackQuery):
    global photo_data
    match callback.data:
        case 'black':
            db.insert_color(callback.from_user.id, 'Черный')
            photo_data = 't_shirt_black'

        case 'white':
            db.insert_color(callback.from_user.id, 'Белый')
            photo_data = 't_shirt_white'

        case 'mustard':
            db.insert_color(callback.from_user.id, 'Горчичный')
            photo_data = 't_shirt_mustard'

    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'), caption=update_messagesjson()['t_shirt'],
                         reply_markup=kb.update_state5())
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def hudi_color_call(callback: types.CallbackQuery):
    global photo_data
    match callback.data:
        case 'hudi_color_black':
            db.insert_color(callback.from_user.id, 'Черный')
            photo_data = 'hudi_bl'

        case 'hudi_color_red':
            db.insert_color(callback.from_user.id, 'Красный')
            photo_data = 'hudi_red'

        case 'hudi_color_sand':
            db.insert_color(callback.from_user.id, 'Песочный')
            photo_data = 'hudi_sand'

    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'), caption=update_messagesjson()['hoodie'],
                         reply_markup=kb.update_state5_hoodie())
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def shopper_color_call(callback: types.CallbackQuery):
    match callback.data:
        case 'shopper_color_black':
            db.insert_color(callback.from_user.id, 'Черный')
            photo = open(goods_photo['shopper_bl'], 'rb')

        case 'shopper_color_white':
            db.insert_color(callback.from_user.id, 'Белый')
            photo = open(goods_photo['shopper_wh'], 'rb')

    await bot.send_photo(callback.from_user.id, photo, caption=update_messagesjson()['shopper'] +
                                                               '\n\n\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.shopper_back)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cup_type_call(callback: types.CallbackQuery):
    match callback.data:
        case 'casual' | 'cup_back_to_casual_size' | 'big_casual_cup_back':
            db.insert_type(callback.from_user.id, 'Обычная')
            await callback.message.answer(text='Выберите размер:', reply_markup=kb.cup_size)

        case 'latte' | 'latte_back_to_size':
            db.insert_type(callback.from_user.id, 'Латте')
            await callback.message.answer(text='Выберите размер', reply_markup=kb.latte_size)

        case 'trip':
            db.insert_type(callback.from_user.id, 'Походная')
            photo = open(goods_photo['cup_trip'], 'rb')
            await bot.send_photo(callback.from_user.id, photo,
                                 caption=update_messagesjson()['cup_trip'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.cup_trip)

        case 'heart' | 'heart_back_to_color':
            db.insert_type(callback.from_user.id, 'С ручкой в виде сердца')
            await callback.message.answer(text=update_messagesjson()['cup_heart_color'], reply_markup=kb.cup_heart_color)

    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def canvas_size_call(callback: types.CallbackQuery):
    match callback.data:
        case 'canvas_size_30_40':
            db.insert_size(callback.from_user.id, '30x40')

        case 'canvas_size_40_60':
            db.insert_size(callback.from_user.id, '40x60')

    await bot.send_message(callback.from_user.id, update_messagesjson()['send_photo'], reply_markup=kb.canvas_back)
    await callback.message.delete()


async def notebook_type_call(callback: types.CallbackQuery):
    global photo_data
    match callback.data:
        case 'sharp':
            db.insert_type(callback.from_user.id, 'В клетку')
            photo_data = 'notebook_sharp'

        case 'line':
            db.insert_type(callback.from_user.id, 'В линейку')
            photo_data = 'notebook_line'

        case 'dot':
            db.insert_type(callback.from_user.id, 'В точку')
            photo_data = 'notebook_dot'

        case 'empty':
            db.insert_type(callback.from_user.id, 'Пустой')
            photo_data = 'notebook_empty'

    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'),
                         caption=update_messagesjson()['notebook'] + '\n'
                                 + 'Выберите размер:', reply_markup=kb.notebook_size)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cardholder_type_call(callback: types.CallbackQuery):
    match callback.data:
        case 'straight':
            db.insert_type(callback.from_user.id, 'Прямой')
            db.insert_color(callback.from_user.id, 'Черный')
            await bot.send_photo(callback.from_user.id, open(goods_photo['cardholder_straight'], 'rb'),
                                 update_messagesjson()['cardholder'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.cardholder_back_kb)
        case 'oblique' | 'cardholder_oblique_back':
            db.insert_type(callback.from_user.id, 'Косой')
            await bot.send_message(callback.from_user.id, update_messagesjson()['cardholder_color'],
                                   reply_markup=kb.cardholder_color)

    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cardholder_oblique_color_call(callback: types.CallbackQuery):
    global photo_data
    match callback.data:
        case 'cardholder_bg':
            db.insert_color(callback.from_user.id, 'Коричневый')
            photo_data = 'cardholder_oblique_bg'

        case 'cardholder_bl':
            db.insert_color(callback.from_user.id, 'Черный')
            photo_data = 'cardholder_oblique_bl'

        case 'cardholder_gr':
            db.insert_color(callback.from_user.id, 'Зеленый')
            photo_data = 'cardholder_oblique_gr'

        case 'cardholder_lg':
            db.insert_color(callback.from_user.id, 'Серый')
            photo_data = 'cardholder_oblique_lg'

        case 'cardholder_pn':
            db.insert_color(callback.from_user.id, 'Розовый')
            photo_data = 'cardholder_oblique_pn'

    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'),
                         update_messagesjson()['cardholder'] + '\n\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.cardholder_oblique_back_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def pass_type_call(callback: types.CallbackQuery):
    if callback.data == 'pass_uf':
        db.insert_type(callback.from_user.id, 'UF')
        await callback.message.answer(text=update_messagesjson()['pass_color_uf'], reply_markup=kb.pass_uf_type)

    elif callback.data == 'pass_sub':
        db.insert_type(callback.from_user.id, 'Сублимационная')
        await callback.message.answer(text=update_messagesjson()['pass_color_sub'], reply_markup=kb.pass_sub_type)

    await callback.message.delete()


async def pass_color_sub(callback: types.CallbackQuery):
    global index
    match callback.data:
        case 'pass_sub_red':
            db.insert_color(callback.from_user.id, 'Красный')
            photos_sub[0] = 'pass_sub_red'
            photos_sub[1] = 'pass_sub_red_dop1'
            photos_sub[2] = 'pass_sub_red_dop2'
            photos_sub[3] = 'pass_sub_red_dop3'

        case 'pass_sub_orange':
            db.insert_color(callback.from_user.id, 'Оранжевый')
            photos_sub[0] = 'pass_sub_orange'
            photos_sub[1] = 'pass_sub_orange_dop1'
            photos_sub[2] = 'pass_sub_orange_dop2'
            photos_sub[3] = 'pass_sub_orange_dop3'

        case 'pass_sub_pink':
            db.insert_color(callback.from_user.id, 'Розовый')
            photos_sub[0] = 'pass_sub_pink'
            photos_sub[1] = 'pass_sub_pink_dop1'
            photos_sub[2] = 'pass_sub_pink_dop2'
            photos_sub[3] = 'pass_sub_pink_dop3'

        case 'pass_sub_salad':
            db.insert_color(callback.from_user.id, 'Салатовый')
            photos_sub[0] = 'pass_sub_salad'
            photos_sub[1] = 'pass_sub_salad_dop1'
            photos_sub[2] = 'pass_sub_salad_dop2'
            photos_sub[3] = 'pass_sub_salad_dop3'

        case 'pass_sub_blue':
            db.insert_color(callback.from_user.id, 'Синий')
            photos_sub[0] = 'pass_sub_blue'
            photos_sub[1] = 'pass_sub_blue_dop1'
            photos_sub[2] = 'pass_sub_blue_dop2'
            photos_sub[3] = 'pass_sub_blue_dop3'

        case 'pass_sub_black':
            db.insert_color(callback.from_user.id, 'Черный')
            photos_sub[0] = 'pass_sub_black'
            photos_sub[1] = 'pass_sub_black_dop1'
            photos_sub[2] = 'pass_sub_black_dop2'
            photos_sub[3] = 'pass_sub_black_dop3'

    match callback.data:
        case 'right_sub':
            if index == 3:
                index = 0
            else:
                index += 1

        case 'left_sub':
            if index == 0:
                index = 3
            else:
                index -= 1

    await bot.send_photo(callback.from_user.id, open(goods_photo[photos_sub[index]], 'rb'),
                         caption=update_messagesjson()['pass'] + '\n\n' + update_messagesjson()['send_photo'], reply_markup=kb.pass_sub_color_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def pass_color_uf(callback: types.CallbackQuery):
    global index
    match callback.data:
        case 'pass_uf_bl':
            db.insert_color(callback.from_user.id, 'Черный')
            photos_uf[0] = 'pass_uf_bl'
            photos_uf[1] = 'pass_uf_bl_dop'

        case 'pass_uf_wh':
            db.insert_color(callback.from_user.id, 'Белый')
            photos_uf[0] = 'pass_uf_wh'
            photos_uf[1] = 'pass_uf_wh_dop'

    if (callback.data == 'right_uf') | (callback.data == 'letf_uf'):
        if index != 1:
            index += 1
        else:
            index -= 1

    await bot.send_photo(callback.from_user.id, open(goods_photo[photos_uf[index]], 'rb'),
                         caption=update_messagesjson()['pass'] + '\n\n' + update_messagesjson()['send_photo'], reply_markup=kb.pass_uf_color_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cup_casual_color_call(callback: types.CallbackQuery):
    global photo_data
    MESSAGES = update_messagesjson()
    match callback.data:
        case 'cup_white':
            db.insert_color(callback.from_user.id, 'Белый')
            photo_data = 'cup_white'
        case 'cup_blue':
            db.insert_color(callback.from_user.id, 'Голубой')
            photo_data = 'cup_blue'
        case 'cup_yellow':
            db.insert_color(callback.from_user.id, 'Желтый')
            photo_data = 'cup_yellow'

        case 'cup_toxic':
            db.insert_color(callback.from_user.id, 'Кислотный снаружи')
            photo_data = 'cup_toxic'

        case 'cup_red':
            db.insert_color(callback.from_user.id, 'Красный')
            photo_data = 'cup_red'

        case 'cup_pink':
            db.insert_color(callback.from_user.id, 'Розовый')
            photo_data = 'cup_pink'

        case 'cup_light_green':
            db.insert_color(callback.from_user.id, 'Светло-зеленый')
            photo_data = 'cup_light_green'

        case 'cup_dark_green':
            db.insert_color(callback.from_user.id, 'Темно-зеленый')
            photo_data = 'cup_dark_green'

        case 'cup_dark_blue':
            db.insert_color(callback.from_user.id, 'Темно-синий')
            photo_data = 'cup_dark_blue'

        case 'cup_black':
            db.insert_color(callback.from_user.id, 'Черный')
            photo_data = 'cup_black'
            
        case 'cup_heart_pink':
            db.insert_color(callback.from_user.id, 'Розовый')
            photo_data = 'cup_heart_pink'
            
        case 'cup_heart_blue':
            db.insert_color(callback.from_user.id, 'Голубой')
            photo_data = 'cup_heart_blue'
    await bot.send_photo(callback.from_user.id, open(goods_photo[photo_data], 'rb'),
                         MESSAGES['cup'] + '\n\n' + MESSAGES['send_photo'],
                         reply_markup=kb.cup_casual_back_to_color_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


# =======================================================выбор размера==================================================


async def t_shirt_size_call(callback: types.CallbackQuery):
    test = True
    match callback.data:
        case 'size_xs':
            if t_shirt_size['xs']:
                db.insert_size(callback.from_user.id, 'XS')
                test = False
        case 'size_s':
            if t_shirt_size['s']:
                db.insert_size(callback.from_user.id, 'S')
                test = False
        case 'size_m':
            if t_shirt_size['m']:
                db.insert_size(callback.from_user.id, 'M')
                test = False
        case 'size_l':
            if t_shirt_size['l']:
                db.insert_size(callback.from_user.id, 'L')
                test = False
        case 'size_xl':
            if t_shirt_size['xl']:
                db.insert_size(callback.from_user.id, 'XL')
                test = False
        case 'size_xxl':
            if t_shirt_size['xxl']:
                db.insert_size(callback.from_user.id, 'XXL')
                test = False
        case 'size_xxxl':
            if t_shirt_size['xxxl']:
                db.insert_size(callback.from_user.id, 'XXXL')
            test = False
    if test:
        await bot.send_message(callback.from_user.id, update_messagesjson()['unknown5'], reply_markup=kb.state5)
    else:
        await bot.send_message(callback.from_user.id, update_messagesjson()['send_photo'], reply_markup=kb.t_shirt_size_kb)
    await callback.message.delete()


async def hudi_size_call(callback: types.CallbackQuery):
    test = True
    match callback.data:
        case 'hudi_size_xs':
            if hudi_size['xs']:
                db.insert_size(callback.from_user.id, 'XS')
                test = False
        case 'hudi_size_s':
            if hudi_size['s']:
                db.insert_size(callback.from_user.id, 'S')
                test = False
        case 'hudi_size_m':
            if hudi_size['m']:
                db.insert_size(callback.from_user.id, 'M')
                test = False
        case 'hudi_size_l':
            if hudi_size['l']:
                db.insert_size(callback.from_user.id, 'L')
                test = False
        case 'hudi_size_xl':
            if hudi_size['xl']:
                db.insert_size(callback.from_user.id, 'XL')
                test = False
        case 'hudi_size_xxl':
            if hudi_size['xxl']:
                db.insert_size(callback.from_user.id, 'XXL')
                test = False
        case 'hudi_size_xxxl':
            if hudi_size['xxxl']:
                db.insert_size(callback.from_user.id, 'XXXL')
            test = False
    if test:
        await bot.send_message(callback.from_user.id, update_messagesjson()['unknown5'], reply_markup=kb.hudi_size)
    else:
        await bot.send_message(callback.from_user.id, update_messagesjson()['send_photo'], reply_markup=kb.hudi_size_kb)
    await callback.message.delete()


async def cup_casual_size_call(callback: types.CallbackQuery):
    match callback.data:
        case 'cup_size_330' | 'cup_casual_back_to_color':
            db.insert_size(callback.from_user.id, '330 мл')
            await bot.send_message(callback.from_user.id, update_messagesjson()['cup_casual_small_color'],
                                   reply_markup=kb.cup_casual_small_color)
        case 'cup_size_480':
            db.insert_size(callback.from_user.id, '480 мл')
            db.insert_color(callback.from_user.id, 'Белый')
            await bot.send_photo(callback.from_user.id, open(goods_photo['cup_big'], 'rb'),
                                 caption=update_messagesjson()['cup'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.big_casual_cup_back_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def cup_latte_size_call(callback: types.CallbackQuery):
    match callback.data:
        case 'size_latte_small':
            db.insert_size(callback.from_user.id, 'Маленькая')
            await bot.send_photo(callback.from_user.id, photo=open(goods_photo['latte_small'], 'rb'),
                                 caption=update_messagesjson()['cup'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.latte_back_to_size_kb)

        case 'size_latte_big':
            db.insert_size(callback.from_user.id, 'Большая')
            await bot.send_photo(callback.from_user.id, photo=open(goods_photo['latte_big'], 'rb'),
                                 caption=update_messagesjson()['cup'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.latte_back_to_size_kb)

    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def heart_color_call(callback: types.CallbackQuery):
    match callback.data:
        case 'cup_heart_blue':
            db.insert_color(callback.from_user.id, 'Голубой')
            await bot.send_photo(callback.from_user.id, open(goods_photo['cup_heart_blue'], 'rb'),
                                 caption=update_messagesjson()['cup'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.cup_heart_back_to_color_kb)
        case 'cup_heart_pink':
            db.insert_color(callback.from_user.id, 'Розовый')
            await bot.send_photo(callback.from_user.id, open(goods_photo['cup_heart_pink'], 'rb'),
                                 caption=update_messagesjson()['cup'] + '\n\n' + update_messagesjson()['send_photo'],
                                 reply_markup=kb.cup_heart_back_to_color_kb)

    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def notebook_size_call(callback: types.CallbackQuery):
    match callback.data:
        case 'a4':
            db.insert_type(callback.from_user.id, 'A4')

        case 'a5':
            db.insert_type(callback.from_user.id, 'A5')

    await bot.send_message(callback.from_user.id, update_messagesjson()['send_photo'], reply_markup=kb.notebook_back_to_size_kb)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)


async def insignia_size_call(callback: types.CallbackQuery):
    match callback.data:
        case 'badges_37':
            db.insert_goods(callback.from_user.id, 'Значки')
            db.insert_size(callback.from_user.id, '37')

        case 'badges_54':
            db.insert_goods(callback.from_user.id, 'Значки')
            db.insert_size(callback.from_user.id, '54')

    await bot.send_photo(callback.from_user.id, open(goods_photo['insignia'], 'rb'), 
                         update_messagesjson()['insignia'] + '\n\n' + update_messagesjson()['send_photo'],
                         reply_markup=kb.badges_back)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)

#=============================Обработка информации клиента============================================


async def doc_handler(message: types.Message):
    document = message.document
    df = 'photos/photo' + str(message.from_user.id) + '.jpg'
    await document.download(destination_file=df)
    link = dm.upload_basic(df)
    db.insert_photo(message.from_user.id, link)
    
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestStates.W_SEND_CONTACT[0])
    await bot.send_message(message.from_user.id, update_messagesjson()['send_contact'], 
                           reply_markup=kb.markup_request)


async def contact_handler(message: types.Message):
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    if first_name is None:
        first_name = "None"
    if last_name is None:
        last_name = 'None'
    db.insert_contact(message.from_user.id, first_name + ' ' + last_name + ' ' + message.contact.phone_number)
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestStates.TEST_STATE_7[0])
    await bot.send_message(message.from_user.id, update_messagesjson()['comment'])


async def photo_exactly_handler(message: types.Message):
    await bot.send_message(message.from_user.id, update_messagesjson()['send_photo_exactly'])


async def insert_sm_handler(message: types.Message, state: FSMContext):
    db.insert_comment(message.from_user.id, message.text)
    sm.insert_all(message.from_user.id)
    sm.empty_row +=1

    await bot.send_message(message.from_user.id, update_messagesjson()['created'], reply_markup=kb.state1)
    print('создано')
    await state.finish()
    


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'Start', 'начать', 'Начать'])
    dp.register_callback_query_handler(show_goods_call, text=['yes', 'back_to_goods', 'start!'])
    dp.register_callback_query_handler(no_call, text='no')
    dp.register_callback_query_handler(start_call, text=['back_to_start'])
    dp.register_callback_query_handler(shopper_back_to_goods_call, text='back_to_shopper_color')
    dp.register_callback_query_handler(back_to_shopper_color_call, text='shopper_back_to_color')
    dp.register_callback_query_handler(back_to_notebook_size, text='notebook_back_to_size')

    dp.register_callback_query_handler(cup_back_to_type_call, text=['cup_back_to_type'])

    dp.register_callback_query_handler(back_to_pass_type_call, text='pass_back_to_type')
    dp.register_callback_query_handler(back_to_pass_sub_color_call, text='back_to_sub_colors')
    dp.register_callback_query_handler(back_to_pass_uf_color_call, text='back_to_uf_colors')

    dp.register_callback_query_handler(t_shirt_call, text=['client_t_shirt', 'back_to_t_shirt_color'])
    dp.register_callback_query_handler(notebook_call, text=['client_notebook', 'notebook_back_to_type'])
    dp.register_callback_query_handler(passport_call, text='client_passport')
    dp.register_callback_query_handler(cardholder_call, text=['client_cardholder', 'cardholder_back'])
    dp.register_callback_query_handler(hudi_call, text=['client_hudi', 'back_to_hudi_color'])
    dp.register_callback_query_handler(shopper_call, text='client_shopper')
    dp.register_callback_query_handler(shopper_color_call, text=['client_shopper_color_black',
                                                                 'client_shopper_color_white'])
    dp.register_callback_query_handler(cup_call, text='client_cup')

    dp.register_callback_query_handler(canvas_photo_call, text=['client_canvas', 'canvas_back_to_size'])

    dp.register_callback_query_handler(badges_photo_call, text=['client_badges', 'badges_back_to_size'])

    dp.register_callback_query_handler(pillow_photo_call, text='client_pillow')

    dp.register_callback_query_handler(mousepad_photo_call, text='client_mouse_pad')

    dp.register_callback_query_handler(t_shirt_color_call, text=['black', 'white', 'mustard', 't_shirt_back_to_size'])
    dp.register_callback_query_handler(hudi_color_call, text=['hudi_color_black', 'hudi_color_red',
                                                              'hudi_color_sand', 'hudi_back_to_size'])
    dp.register_callback_query_handler(shopper_color_call, text=['shopper_color_black',
                                                                 'shopper_color_white'])
    dp.register_callback_query_handler(cup_type_call, text=['casual', 'latte', 'trip', 'heart',
                                                            'cup_back_to_casual_size', 'big_casual_cup_back',
                                                            'latte_back_to_size', 'heart_back_to_color'])
    dp.register_callback_query_handler(canvas_size_call, text=['canvas_size_30_40', 'canvas_size_40_60'])
    dp.register_callback_query_handler(notebook_type_call, text=['sharp', 'line', 'dot', 'empty'])
    dp.register_callback_query_handler(cardholder_type_call, text=['straight', 'oblique', 'cardholder_oblique_back'])
    dp.register_callback_query_handler(cardholder_oblique_color_call, text=['cardholder_bg', 'cardholder_bl',
                                                                            'cardholder_gr', 'cardholder_lg',
                                                                            'cardholder_pn'])
    dp.register_callback_query_handler(pass_type_call, text=['pass_uf', 'pass_sub'])
    dp.register_callback_query_handler(pass_color_sub, text=['pass_sub_red', 'pass_sub_orange',
                                                             'pass_sub_pink', 'pass_sub_salad',
                                                             'pass_sub_blue', 'pass_sub_black',
                                                             'left_sub', 'right_sub'])
    dp.register_callback_query_handler(pass_color_uf, text=['pass_uf_bl', 'pass_uf_wh',
                                                            'left_uf', 'right_uf'])
    dp.register_callback_query_handler(cup_casual_color_call, text=['cup_white', 'cup_blue', 'cup_yellow',
                                                                    'cup_toxic', 'cup_red', 'cup_pink',
                                                                    'cup_light_green', 'cup_dark_green',
                                                                    'cup_dark_blue', 'cup_black',])

    dp.register_callback_query_handler(t_shirt_size_call, text=['size_xs', 'size_s', 'size_m', 'size_l',
                                                                'size_xl', 'size_xxl', 'size_xxxl'])
    dp.register_callback_query_handler(hudi_size_call, text=['hudi_size_xs', 'hudi_size_s', 'hudi_size_m',
                                                             'hudi_size_l', 'hudi_size_xl', 'hudi_size_xxl',
                                                             'hudi_size_xxxl', 'hudi_size_4xl', 'hudi_size_5xl'])
    dp.register_callback_query_handler(cup_casual_size_call, text=['cup_size_330', 'cup_size_480',
                                                                   'cup_casual_back_to_color'])
    dp.register_callback_query_handler(cup_latte_size_call, text=['size_latte_small', 'size_latte_big'])
    dp.register_callback_query_handler(heart_color_call, text=['cup_heart_blue', 'cup_heart_pink'])
    dp.register_callback_query_handler(notebook_size_call, text=['a4', 'a5'])
    dp.register_callback_query_handler(insignia_size_call, text=['badges_37', 'badges_54'])

    dp.register_message_handler(doc_handler, content_types=ContentTypes.DOCUMENT)
    dp.register_message_handler(contact_handler,state=TestStates.W_SEND_CONTACT, content_types=ContentTypes.CONTACT)
    dp.register_message_handler(photo_exactly_handler, content_types=ContentTypes.PHOTO)
    dp.register_message_handler(insert_sm_handler, state=TestStates.TEST_STATE_7)






#TODO:
#fix HUDI, SHOPPER, CUP, 