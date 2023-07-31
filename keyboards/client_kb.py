from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
                          ReplyKeyboardMarkup, KeyboardButton
import json
with open('sizes_data.json', 'r') as file:
    data = json.load(file)



back = InlineKeyboardButton(text='В начало 🔄', callback_data='back_to_start')

button_start = InlineKeyboardButton(text='Начать', callback_data='start!')

button_yes = InlineKeyboardButton(text='Да 🛒', callback_data='yes')
button_no = InlineKeyboardButton(text='Нет ❌', callback_data='no')

t_shirt = InlineKeyboardButton(text='Футболка', callback_data='client_t_shirt')
hudi = InlineKeyboardButton(text='Худи ', callback_data='client_hudi')
shopper = InlineKeyboardButton(text='Шоппер', callback_data='client_shopper')
pillow = InlineKeyboardButton(text='Подушка', callback_data='client_pillow')
cup = InlineKeyboardButton(text='Кружка', callback_data='client_cup')
canvas = InlineKeyboardButton(text='Холст', callback_data='client_canvas')
notebook = InlineKeyboardButton(text='Блокнот', callback_data='client_notebook')
badges = InlineKeyboardButton(text='Значки', callback_data='client_badges')
passport = InlineKeyboardButton(text='Обложка для Паспорта', callback_data='client_passport')
mouse_pad = InlineKeyboardButton(text='Коврик для мыши', callback_data='client_mouse_pad')
cardholder = InlineKeyboardButton(text='Картхолдер', callback_data='client_cardholder')

black = InlineKeyboardButton(text='Черный ⚫️', callback_data='black')
white = InlineKeyboardButton(text='Белый ⚪️', callback_data='white')
mustard = InlineKeyboardButton(text='Горчичный 🟠', callback_data='mustard')
back_to_goods = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_goods')
back_to_t_shirt_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_t_shirt_color')
back_to_hudi_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_hudi_color')
back_to_shopper_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_shopper_color')

size_xs = InlineKeyboardButton(text='XS', callback_data='size_xs')
size_s = InlineKeyboardButton(text='S', callback_data='size_s')
size_m = InlineKeyboardButton(text='M', callback_data='size_m')
size_l = InlineKeyboardButton(text='L', callback_data='size_l')
size_xl = InlineKeyboardButton(text='XL', callback_data='size_xl')
size_xxl = InlineKeyboardButton(text='XXL', callback_data='size_xxl')
size_xxxl = InlineKeyboardButton(text='XXXL', callback_data='size_xxxl')
size_4xl = InlineKeyboardButton(text='4XL', callback_data='size_4xl')
size_5xl = InlineKeyboardButton(text='5XL', callback_data='size_5xl')

hudi_size_xs = InlineKeyboardButton(text='XS', callback_data='hudi_size_xs')
hudi_size_s = InlineKeyboardButton(text='S', callback_data='hudi_size_s')
hudi_size_m = InlineKeyboardButton(text='M', callback_data='hudi_size_m')
hudi_size_l = InlineKeyboardButton(text='L', callback_data='hudi_size_l')
hudi_size_xl = InlineKeyboardButton(text='XL', callback_data='hudi_size_xl')
hudi_size_xxl = InlineKeyboardButton(text='XXL', callback_data='hudi_size_xxl')
hudi_size_xxxl = InlineKeyboardButton(text='XXXL', callback_data='hudi_size_xxxl')
hudi_size_4xl = InlineKeyboardButton(text='4XL', callback_data='hudi_size_4xl')
hudi_size_5xl = InlineKeyboardButton(text='5XL', callback_data='hudi_size_5xl')

type_casual = InlineKeyboardButton(text='Обычная', callback_data='type_casual')
type_latte = InlineKeyboardButton(text='Латте', callback_data='type_latte')

cup_330_black = InlineKeyboardButton(text='Черный ⚫️', callback_data='cup_330_black')
cup_330_pink = InlineKeyboardButton(text='Розовый 🟣', callback_data='cup_330_pink')
cup_330_red = InlineKeyboardButton(text='Красный 🔴', callback_data='cup_330_red')
cup_330_vi = InlineKeyboardButton(text='Красно-белый 🔴⚪️', callback_data='cup_330_vi')
cup_330_white = InlineKeyboardButton(text='Белый ⚪️', callback_data='cup_330_white')
cup_330_zi = InlineKeyboardButton(text='Зелено-белая 🟢⚪️', callback_data='cup_330_zi')
cup_330_blue = InlineKeyboardButton(text='Голубой 🔵', callback_data='cup_330_blue')
cup_330_yellow = InlineKeyboardButton(text='Желтый 🟡', callback_data='cup_330_yellow')
cup_330_green = InlineKeyboardButton(text='Зеленый 🟢', callback_data='cup_330_green')
cup_330_dark_blue = InlineKeyboardButton(text='Темно-синий 🔵', callback_data='cup_330_dark_blue')

hudi_color_black = InlineKeyboardButton(text='Черный ⚫️', callback_data='hudi_color_black')
hudi_color_red = InlineKeyboardButton(text='Красный 🔴', callback_data='hudi_color_red')
hudi_color_sand = InlineKeyboardButton(text='Песочный 🟠', callback_data='hudi_color_sand')

hudi_color = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
hudi_color.insert(hudi_color_black)
hudi_color.insert(hudi_color_red)
hudi_color.insert(hudi_color_sand)
hudi_color.row(back_to_goods, back)

state1 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_start)

state2 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_yes, button_no)

state3 = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
state3.row(t_shirt, hudi)
state3.row(shopper, pillow)
state3.row(cup, notebook)
state3.row(badges, canvas)
state3.row(cardholder, mouse_pad)
state3.row(passport)
state3.row(back)

state4 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(black, white, mustard)
state4.row(back_to_goods, back)

shopper_black = InlineKeyboardButton(text='Черный ⚫️', callback_data='shopper_color_black')
shopper_white = InlineKeyboardButton(text='Белый ⚪️', callback_data='shopper_color_white')

shopper_color = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(shopper_black, shopper_white)
shopper_color.row(back_to_goods, back)

shopper_back_to_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='shopper_back_to_color')
shopper_back = InlineKeyboardMarkup().row(shopper_back_to_color, back)
def update_state5():
    with open('sizes_data.json', 'r') as file:
        data = json.load(file)
    state5 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    t_s = []
    if data["t_shirt"]['xs']:
        t_s.append(size_xs)
    if data["t_shirt"]['s']:
        t_s.append(size_s)
    if data["t_shirt"]['m']:
        t_s.append(size_m)
    if data["t_shirt"]['l']:
        t_s.append(size_l)
    if data["t_shirt"]['xl']:
        t_s.append(size_xl)
    if data["t_shirt"]['xxl']:
        t_s.append(size_xxl)
    if data["t_shirt"]['xxxl']:
        t_s.append(size_xxxl)
    for i in t_s:
        state5.insert(i)
    state5.row(back_to_t_shirt_color, back)
    return state5

def update_state5_hoodie():
    with open('sizes_data.json', 'r') as file:
        data = json.load(file)
    state5_hoodie = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    t_s = []
    if data["hudi"]['xs']:
        t_s.append(hudi_size_xs)
    if data["hudi"]['s']:
        t_s.append(hudi_size_s)
    if data["hudi"]['m']:
        t_s.append(hudi_size_m)
    if data["hudi"]['l']:
        t_s.append(hudi_size_l)
    if data["hudi"]['xl']:
        t_s.append(hudi_size_xl)
    if data["hudi"]['xxl']:
        t_s.append(hudi_size_xxl)
    if data["hudi"]['xxxl']:
        t_s.append(hudi_size_xxxl)
    if data["hudi"]['4xl']:
        t_s.append(hudi_size_4xl)
    if data["hudi"]['5xl']:
        t_s.append(hudi_size_5xl)

    for i in t_s:
        state5_hoodie.insert(i)
    state5_hoodie.row(back_to_hudi_color, back)
    return state5_hoodie

a4 = InlineKeyboardButton(text='а4', callback_data='a4')
a5 = InlineKeyboardButton(text='а5', callback_data='a5')
notebook_size_back_to_type = InlineKeyboardButton(text='Назад ⬅️', callback_data='notebook_back_to_type')
notebook_size = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
notebook_size.row(a4, a5)
notebook_size.row(notebook_size_back_to_type, back)

notebook_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='notebook_back_to_size')
notebook_back_to_size_kb = InlineKeyboardMarkup().row(notebook_back_to_size, back)

sharp = InlineKeyboardButton(text='В клетку', callback_data='sharp')
line = InlineKeyboardButton(text='В линейку', callback_data='line')
dot = InlineKeyboardButton(text='В точку', callback_data='dot')
empty = InlineKeyboardButton(text='Пустой', callback_data='empty')
notebook_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
notebook_type.row(sharp, line)
notebook_type.row(dot, empty)
notebook_type.row(back_to_goods, back)

straight = InlineKeyboardButton(text='Прямой', callback_data='straight')
oblique = InlineKeyboardButton(text='Косой', callback_data='oblique')
cardholder_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cardholder_type.row(straight, oblique)
cardholder_type.row(back_to_goods, back)

cardholder_back = InlineKeyboardButton(text='Назад ⬅️', callback_data='cardholder_back')
cardholder_back_kb = InlineKeyboardMarkup().row(cardholder_back, back)

cardholder_bg = InlineKeyboardButton(text='Коричневый', callback_data='cardholder_bg')
cardholder_bl = InlineKeyboardButton(text='Черный', callback_data='cardholder_bl')
cardholder_gr = InlineKeyboardButton(text='Зеленый', callback_data='cardholder_gr')
cardholder_lg = InlineKeyboardButton(text='Серый', callback_data='cardholder_lg')
cardholder_pn = InlineKeyboardButton(text='Розовый', callback_data='cardholder_pn')

cardholder_color = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cardholder_color.insert(cardholder_bg)
cardholder_color.insert(cardholder_bl)
cardholder_color.insert(cardholder_gr)
cardholder_color.insert(cardholder_lg)
cardholder_color.insert(cardholder_pn)
cardholder_color.row(cardholder_back, back)

cardholder_oblique_back = InlineKeyboardButton(text='Назад ⬅️', callback_data='cardholder_oblique_back')
cardholder_oblique_back_kb = InlineKeyboardMarkup().row(cardholder_oblique_back, back)

canvas_size_30_40 = InlineKeyboardButton(text='30x40', callback_data='canvas_size_30_40')
canvas_size_40_60 = InlineKeyboardButton(text='40x60', callback_data='canvas_size_40_60')
canvas_back_to_desc = InlineKeyboardButton(text='Назад ⬅️', callback_data='canvas_back_to_desc')
canvas_size = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
canvas_size.row(canvas_size_30_40, canvas_size_40_60)
canvas_size.row(back_to_goods, back)

canvas_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='canvas_back_to_size')
canvas_back = InlineKeyboardMarkup().row(canvas_back_to_size, back)

badges_next = InlineKeyboardButton(text='Далее ➡️', callback_data='badges_next')
badges_info = InlineKeyboardMarkup()
badges_info.row(badges_next). \
    row(back_to_goods, back)

badges_size_37 = InlineKeyboardButton(text='37', callback_data='badges_37')
badges_size_54 = InlineKeyboardButton(text='54', callback_data='badges_54')
badges_size = InlineKeyboardMarkup()
badges_size.row(badges_size_37, badges_size_54). \
    row(back_to_goods, back)
    
badges_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='badges_back_to_size')
badges_back = InlineKeyboardMarkup().row(badges_back_to_size, back)

pillow_info = InlineKeyboardMarkup()
pillow_info.row(back_to_goods, back)

#mouse_pad_next = InlineKeyboardButton(text='Далее ➡️', callback_data='mousepad_next')
mouse_pad_info = InlineKeyboardMarkup()
mouse_pad_info.row(back_to_goods, back)

pass_uf = InlineKeyboardButton(text='UF', callback_data='pass_uf')
pass_sub = InlineKeyboardButton(text='Сублимационная', callback_data='pass_sub')
pass_back_to_type = InlineKeyboardButton(text='Назад ⬅️', callback_data='pass_back_to_type')
pass_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pass_type.row(pass_uf, pass_sub)
pass_type.row(back_to_goods, back)

pass_uf_bl = InlineKeyboardButton(text='Черный ⚫️', callback_data='pass_uf_bl')
pass_uf_wh = InlineKeyboardButton(text='Белый ⚪️', callback_data='pass_uf_wh')
pass_uf_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pass_uf_type.row(pass_uf_wh, pass_uf_bl)
pass_uf_type.row(pass_back_to_type, back)

pass_uf_colors_back = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_uf_colors')
pass_uf_color_left = InlineKeyboardButton(text='◀️️', callback_data='left_uf')
pass_uf_color_right = InlineKeyboardButton(text='▶️', callback_data='right_uf')
pass_uf_color_kb = InlineKeyboardMarkup().row(pass_uf_color_left, pass_uf_color_right).row(pass_uf_colors_back, back)

pass_sub_red = InlineKeyboardButton(text='Красный 🔴', callback_data='pass_sub_red')
pass_sub_orange = InlineKeyboardButton(text='Оранжевый 🟠', callback_data='pass_sub_orange')
pass_sub_pink = InlineKeyboardButton(text='Розовый 🟣', callback_data='pass_sub_pink')
pass_sub_salad = InlineKeyboardButton(text='Салатовый 🟢', callback_data='pass_sub_salad')
pass_sub_blue = InlineKeyboardButton(text='Синий 🔵', callback_data='pass_sub_blue')
pass_sub_black = InlineKeyboardButton(text='Черный ⚫️', callback_data='pass_sub_black')
pass_sub_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pass_sub_type.insert(pass_sub_red)
pass_sub_type.insert(pass_sub_orange)
pass_sub_type.insert(pass_sub_pink)
pass_sub_type.insert(pass_sub_salad)
pass_sub_type.insert(pass_sub_blue)
pass_sub_type.insert(pass_sub_black)
pass_sub_type.row(pass_back_to_type, back)

pass_sub_colors_back = InlineKeyboardButton(text='Назад ⬅️', callback_data='back_to_sub_colors')
pass_sub_color_left = InlineKeyboardButton(text='◀️️', callback_data='left_sub')
pass_sub_color_right = InlineKeyboardButton(text='▶️', callback_data='right_sub')
pass_sub_color_kb = InlineKeyboardMarkup().row(pass_sub_color_left, pass_sub_color_right).row(pass_sub_colors_back,
                                                                                              back)

casual = InlineKeyboardButton(text='Обычная', callback_data='casual')
trip = InlineKeyboardButton(text='Походная', callback_data='trip')
latte = InlineKeyboardButton(text='Латте', callback_data='latte')
heart = InlineKeyboardButton(text='С ручкой в виде сердца', callback_data='heart')
cup_back_to_type = InlineKeyboardButton(text='Назад', callback_data='cup_back_to_type')
cup_type = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cup_type.row(casual, latte).row(trip, heart)
cup_type.row(back_to_goods, back)

cup_white = InlineKeyboardButton(text='Белый', callback_data='cup_white')
cup_blue = InlineKeyboardButton(text='Голубой', callback_data='cup_blue')
cup_yellow = InlineKeyboardButton(text='Желтый ', callback_data='cup_yellow')
cup_toxic = InlineKeyboardButton(text='Кислотный снаружи', callback_data='cup_toxic')
cup_red = InlineKeyboardButton(text='Красный', callback_data='cup_red')
cup_pink = InlineKeyboardButton(text='Розовый', callback_data='cup_pink')
cup_light_green = InlineKeyboardButton(text='Светло-зеленый', callback_data='cup_light_green')
cup_dark_green = InlineKeyboardButton(text='Темно-зеленый', callback_data='cup_dark_green')
cup_dark_blue = InlineKeyboardButton(text='Темно-синий', callback_data='cup_dark_blue')
cup_black = InlineKeyboardButton(text='Черный', callback_data='cup_black')
cup_back_to_casual_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='cup_back_to_casual_size')
cup_casual_small_color = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cup_casual_small_color.insert(cup_white)
cup_casual_small_color.insert(cup_blue)
cup_casual_small_color.insert(cup_yellow)
cup_casual_small_color.insert(cup_red)
cup_casual_small_color.insert(cup_pink)
cup_casual_small_color.insert(cup_light_green)
cup_casual_small_color.insert(cup_dark_green)
cup_casual_small_color.insert(cup_dark_blue)
cup_casual_small_color.row(cup_black, cup_toxic)
cup_casual_small_color.row(cup_back_to_casual_size, back)

cup_casual_back_to_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='cup_casual_back_to_color')
cup_casual_back_to_color_kb = InlineKeyboardMarkup().row(cup_casual_back_to_color, back)


cup_heart_blue = InlineKeyboardButton(text='Голубой', callback_data='cup_heart_blue')
cup_heart_pink = InlineKeyboardButton(text='Розовый', callback_data='cup_heart_pink')
cup_heart_color = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cup_heart_color.insert(cup_heart_blue)
cup_heart_color.insert(cup_heart_pink)
cup_heart_color.row(cup_back_to_type, back)

cup_heart_back_to_color = InlineKeyboardButton(text='Назад ⬅️', callback_data='heart_back_to_color')
cup_heart_back_to_color_kb = InlineKeyboardMarkup().row(cup_heart_back_to_color, back)

cup_size_330 = InlineKeyboardButton(text='330 мл', callback_data='cup_size_330')
cup_size_480 = InlineKeyboardButton(text='480 мл', callback_data='cup_size_480')
cup_size = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cup_size.insert(cup_size_330)
cup_size.insert(cup_size_480)
cup_size.row(cup_back_to_type, back)

big_casual_cup_back = InlineKeyboardButton(text='Назад ⬅️', callback_data='big_casual_cup_back')
big_casual_cup_back_kb = InlineKeyboardMarkup().row(big_casual_cup_back, back)

size_latte_big = InlineKeyboardButton(text='Большая', callback_data='size_latte_big')
size_latte_small = InlineKeyboardButton(text='Маленькая', callback_data='size_latte_small')

latte_size = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
latte_size.row(size_latte_big, size_latte_small)
latte_size.row(cup_back_to_type, back)

latte_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='latte_back_to_size')
latte_back_to_size_kb = InlineKeyboardMarkup().row(latte_back_to_size, back)

cup_trip = InlineKeyboardMarkup()
cup_trip.row(cup_back_to_type, back)


t_shirt_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='t_shirt_back_to_size')
t_shirt_size_kb = InlineKeyboardMarkup().row(t_shirt_back_to_size, back)

hudi_back_to_size = InlineKeyboardButton(text='Назад ⬅️', callback_data='hudi_back_to_size')
hudi_size_kb = InlineKeyboardMarkup().row(hudi_back_to_size, back)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
)