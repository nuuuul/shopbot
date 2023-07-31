from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
with open('sizes_data.json', 'r') as file:
    data = json.load(file)
with open('messages.json', 'r', encoding='utf-8') as fh:
    messages = json.load(fh)
admin_tostart = InlineKeyboardButton(text='Вернуться в начало', callback_data='admin_back_to_start')
admin_quit = InlineKeyboardButton(text='Сохранить и выйти', callback_data='admin_quit')
admin_back_to_items = InlineKeyboardButton(text='Вернуться в гл. меню', callback_data='admin_back_to_items')
admin_resize = InlineKeyboardButton(text='Изменить размер', callback_data='resize')
admin_rename = InlineKeyboardButton(text='Изменить текст', callback_data='rename')
admin_panel = InlineKeyboardMarkup().row(admin_resize).row(admin_rename).row(admin_quit)

admin_menu = InlineKeyboardMarkup().row(admin_back_to_items, admin_quit)

admin_t_shirt = InlineKeyboardButton(text='Футболка', callback_data='admin_t_shirt')
admin_hudi = InlineKeyboardButton(text='Худи ', callback_data='admin_hudi')
admin_shopper = InlineKeyboardButton(text='Шоппер', callback_data='admin_shopper')
admin_pillow = InlineKeyboardButton(text='Подушка', callback_data='admin_pillow')
admin_cup = InlineKeyboardButton(text='Кружка', callback_data='admin_cup')
admin_canvas = InlineKeyboardButton(text='Холст', callback_data='admin_canvas')
admin_notebook = InlineKeyboardButton(text='Блокнот', callback_data='admin_notebook')
admin_badges = InlineKeyboardButton(text='Значки', callback_data='admin_badges')
admin_passport = InlineKeyboardButton(text='Обложка для Паспорта', callback_data='admin_passport')
admin_mouse_pad = InlineKeyboardButton(text='Коврик для мыши', callback_data='admin_mouse_pad')
admin_cardholder = InlineKeyboardButton(text='Картхолдер', callback_data='admin_cardholder')


ts_xs = InlineKeyboardButton(text='XS', callback_data='ts_xs')
ts_s = InlineKeyboardButton(text='S', callback_data='ts_s')
ts_m = InlineKeyboardButton(text='M', callback_data='ts_m')
ts_l = InlineKeyboardButton(text='L', callback_data='ts_l')
ts_xl = InlineKeyboardButton(text='XL', callback_data='ts_xl')
ts_xxl = InlineKeyboardButton(text='XXL', callback_data='ts_xxl')
ts_xxxl = InlineKeyboardButton(text='XXXL', callback_data='ts_xxxl')
ts_xs_tf = InlineKeyboardButton(text=str(data["t_shirt"]['xs']), callback_data='ts_xs_tf')
ts_s_tf = InlineKeyboardButton(text=str(data["t_shirt"]['s']), callback_data='ts_s_tf')
ts_m_tf = InlineKeyboardButton(text=str(data["t_shirt"]['m']), callback_data='ts_m_tf')
ts_l_tf = InlineKeyboardButton(text=str(data["t_shirt"]['l']), callback_data='ts_l_tf')
ts_xl_tf = InlineKeyboardButton(text=str(data["t_shirt"]['xl']), callback_data='ts_xl_tf')
ts_xxl_tf = InlineKeyboardButton(text=str(data["t_shirt"]['xxl']), callback_data='ts_xxl_tf')
ts_xxxl_tf = InlineKeyboardButton(text=str(data["t_shirt"]['xxxl']), callback_data='ts_xxxl_tf')

tshirt_size = InlineKeyboardMarkup()
tshirt_size.row(ts_xs, ts_xs_tf)
tshirt_size.row(ts_s, ts_s_tf)
tshirt_size.row(ts_m, ts_m_tf)
tshirt_size.row(ts_l, ts_l_tf)
tshirt_size.row(ts_xl, ts_xl_tf)
tshirt_size.row(ts_xxl, ts_xxl_tf)
tshirt_size.row(ts_xxxl, ts_xxxl_tf)
tshirt_size.row(admin_back_to_items, admin_tostart)


hudi_xs = InlineKeyboardButton(text='XS', callback_data='hudi_xs')
hudi_s = InlineKeyboardButton(text='S', callback_data='hudi_s')
hudi_m = InlineKeyboardButton(text='M', callback_data='hudi_m')
hudi_l = InlineKeyboardButton(text='L', callback_data='hudi_l')
hudi_xl = InlineKeyboardButton(text='XL', callback_data='hudi_xl')
hudi_xxl = InlineKeyboardButton(text='XXL', callback_data='hudi_xxl')
hudi_xxxl = InlineKeyboardButton(text='XXXL', callback_data='hudi_xxxl')
hudi_4xl = InlineKeyboardButton(text='4XL', callback_data='hudi_4xl')
hudi_5xl = InlineKeyboardButton(text='5XL', callback_data='hudi_5xl')

hudi_xs_tf = InlineKeyboardButton(text=str(data["hudi"]['xs']), callback_data='hudi_xs_tf')
hudi_s_tf = InlineKeyboardButton(text=str(data["hudi"]['s']), callback_data='hudi_s_tf')
hudi_m_tf = InlineKeyboardButton(text=str(data["hudi"]['m']), callback_data='hudi_m_tf')
hudi_l_tf = InlineKeyboardButton(text=str(data["hudi"]['l']), callback_data='hudi_l_tf')
hudi_xl_tf = InlineKeyboardButton(text=str(data["hudi"]['xl']), callback_data='hudi_xl_tf')
hudi_xxl_tf = InlineKeyboardButton(text=str(data["hudi"]['xxl']), callback_data='hudi_xxl_tf')
hudi_xxxl_tf = InlineKeyboardButton(text=str(data["hudi"]['xxxl']), callback_data='hudi_xxxl_tf')
hudi_4xl_tf = InlineKeyboardButton(text=str(data["hudi"]['4xl']), callback_data='hudi_4xl_tf')
hudi_5xl_tf = InlineKeyboardButton(text=str(data["hudi"]['5xl']), callback_data='hudi_5xl_tf')

hudi_size_ = InlineKeyboardMarkup()
hudi_size_.row(hudi_xs, hudi_xs_tf)
hudi_size_.row(hudi_s, hudi_s_tf)
hudi_size_.row(hudi_m, hudi_m_tf)
hudi_size_.row(hudi_l, hudi_l_tf)
hudi_size_.row(hudi_xl, hudi_xl_tf)
hudi_size_.row(hudi_xxl, hudi_xxl_tf)
hudi_size_.row(hudi_xxxl, hudi_xxxl_tf)
hudi_size_.row(hudi_4xl, hudi_4xl_tf)
hudi_size_.row(hudi_5xl, hudi_5xl_tf)
hudi_size_.row(admin_tostart)


admin_items = InlineKeyboardMarkup()
admin_items.row(admin_t_shirt, admin_hudi)
admin_items.row(admin_shopper, admin_pillow)
admin_items.row(admin_cup, admin_notebook)
admin_items.row(admin_badges, admin_canvas)
admin_items.row(admin_cardholder, admin_mouse_pad)
admin_items.row(admin_passport)
admin_items.row(admin_tostart)


messages_kb = InlineKeyboardMarkup(row_width=3)
messages_buttons = []
for i in messages.keys():
    messages_buttons = InlineKeyboardButton(text=str(i), callback_data=str(i))
    messages_kb.insert(messages_buttons)
messages_kb.row(admin_tostart)



t_shirt_message = InlineKeyboardButton(text='t_shirt', callback_data='t_shirt')
t_shirt_message_color = InlineKeyboardButton(text='t_shirt_color', callback_data='t_shirt_color')
t_shirt_message_call = InlineKeyboardMarkup().row(t_shirt_message_color, t_shirt_message).row(admin_back_to_items, admin_quit)
t_size = InlineKeyboardButton(text='Изменить размеры', callback_data='change_t_shirt_size')
t_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_t_shirt_messages')

t_shirt_black = InlineKeyboardButton(text='t_shirt_black', callback_data='goods/Футболки/фут bl.png')
t_shirt_white = InlineKeyboardButton(text='t_shirt_white', callback_data='goods/Футболки/фут wh.png')
t_shirt_mustart = InlineKeyboardButton(text='t_shirt_mustard', callback_data='goods/Футболки/фут  Горчичная.png')
t_shirt_photo_call = InlineKeyboardMarkup().row(t_shirt_black, t_shirt_white).row(t_shirt_mustart).row(admin_back_to_items, admin_quit)
t_shirt_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_t_shirt_photos')

admin_t_shirt_to_do = InlineKeyboardMarkup()
admin_t_shirt_to_do.row(t_size, t_messages, t_shirt_photos)
admin_t_shirt_to_do.row(admin_back_to_items, admin_quit)


hoodie_message_color = InlineKeyboardButton(text='hudi_color', callback_data='hudi_color')
hoodie_message = InlineKeyboardButton(text='hoodie', callback_data='hoodie')
hoodie_message_call = InlineKeyboardMarkup().row(hoodie_message_color, hoodie_message).row(admin_back_to_items, admin_quit)
hoodie_size = InlineKeyboardButton(text='Изменить размер', callback_data='change_hoodie')
hoodie_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_hoodie_messages')

hudi_black = InlineKeyboardButton(text='hudi_bl', callback_data='goods/Худи/Худи bl.png')
hudi_red =InlineKeyboardButton(text='hudi_red', callback_data='goods/Худи/Худи red.png')
hudi_sand = InlineKeyboardButton(text='hudi_sand', callback_data='goods/Худи/Худи Песочный.png')
hudi_photo_call = InlineKeyboardMarkup().row(hudi_black, hudi_red).row(hudi_sand).row(admin_back_to_items, admin_quit)
hudi_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_hudi_photos')
admin_hoodie_to_do = InlineKeyboardMarkup()
admin_hoodie_to_do.row(hoodie_size, hoodie_messages, hudi_photos)
admin_hoodie_to_do.row(admin_back_to_items, admin_quit)


shopper_message_color = InlineKeyboardButton(text='shopper_color', callback_data='shopper_color')
shopper_message = InlineKeyboardButton(text='shopper', callback_data='shopper')
shopper_message_call = InlineKeyboardMarkup().row(shopper_message_color, shopper_message).row(admin_back_to_items, admin_quit)
shopper_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_shopper_messages')

shopper_bl = InlineKeyboardButton(text='shopper_bl', callback_data='goods/Шоппер bl сж.png')
shopper_wh = InlineKeyboardButton(text='shopper_wh', callback_data='goods/Шоппер wh сж.png')
shopper_photo_call = InlineKeyboardMarkup().row(shopper_bl, shopper_wh).row(admin_back_to_items, admin_quit)
shopper_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_shopper_photos')
admin_shopper_to_do = InlineKeyboardMarkup()
admin_shopper_to_do.row(shopper_messages, shopper_photos).row(admin_back_to_items, admin_quit)


pillow_message = InlineKeyboardButton(text='pillow', callback_data='pillow')
pillow_message_call = InlineKeyboardMarkup().row(pillow_message).row(admin_back_to_items, admin_quit)
pillow_messages = InlineKeyboardButton(text = 'Изменить текст', callback_data='change_pillow_messages')

pillow_photo = InlineKeyboardButton(text='pillow', callback_data='goods/Подушки/1.png')
pillow_photo_call = InlineKeyboardMarkup().row(pillow_photo).row(admin_back_to_items, admin_quit)
pillow_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_pillow_photos')

admin_pillow_to_do = InlineKeyboardMarkup()
admin_pillow_to_do.row(pillow_messages, pillow_photos).row(admin_back_to_items, admin_quit)


cup_message = InlineKeyboardButton(text='cup', callback_data='cup')
cup_message_type = InlineKeyboardButton(text='cup_type', callback_data='cup_type')
cup_message_casual_small_color = InlineKeyboardButton(text='cup_casual_small_color', callback_data='cup_casual_small_color')
cup_message_heart_color = InlineKeyboardButton(text='cup_heart_color', callback_data='cup_heart_color')
cup_message_trip = InlineKeyboardButton(text='cup_trip', callback_data='cup_trip')
cup_message_call = InlineKeyboardMarkup().row(cup_message, cup_message_type).row(cup_message_trip, cup_message_heart_color).row(cup_message_casual_small_color).row(admin_back_to_items, admin_quit)
cup_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_cup_messages')

cup_photo_white= InlineKeyboardButton(text='cup_white', callback_data= 'goods/Кружки/Белая (330).png')
cup_photo_burgundy= InlineKeyboardButton(text='cup_burgundy', callback_data= 'goods/Кружки/Бордовая (330).png')
cup_photo_blue= InlineKeyboardButton(text='cup_blue', callback_data= 'goods/Кружки/Голубая (330).png')
cup_photo_yellow = InlineKeyboardButton(text='cup_yellow', callback_data= 'goods/Кружки/Жёлтая (330).png')
cup_photo_toxic = InlineKeyboardButton(text='cup_toxic', callback_data= 'goods/Кружки/Кислотоная снаржи(330).png')
cup_photo_red = InlineKeyboardButton(text='cup_red', callback_data= 'goods/Кружки/Красная (330).png')
cup_photo_pink = InlineKeyboardButton(text='cup_pink', callback_data= 'goods/Кружки/Розовая (330).png')
cup_photo_light_green = InlineKeyboardButton(text='cup_light_green', callback_data= 'goods/Кружки/Светло-зеленый (330).png')
cup_photo_dark_green = InlineKeyboardButton(text='cup_dark_green', callback_data= 'goods/Кружки/Темно-зеленый (330).png')
cup_photo_dark_blue = InlineKeyboardButton(text='cup_dark_blue', callback_data= 'goods/Кружки/Темно-синий (330).png')
cup_photo_black = InlineKeyboardButton(text='cup_black', callback_data= 'goods/Кружки/Чёрная (330).png')
cup_photo_heart_blue = InlineKeyboardButton(text='cup_heart_blue', callback_data= 'goods/Кружки/Кружка голубая с ручкой в виде сердечка (330).png')
cup_photo_heart_pink = InlineKeyboardButton(text='cup_heart_pink', callback_data= 'goods/Кружки/Кружка розовая с ручкой в виде сердечка (330).png')

cup_photo_call = InlineKeyboardMarkup().row(cup_photo_white, cup_photo_burgundy, cup_photo_blue).\
                                row(cup_photo_yellow, cup_photo_toxic, cup_photo_red).\
                                row(cup_photo_pink, cup_photo_light_green, cup_photo_dark_green).\
                                row(cup_photo_dark_blue, cup_photo_black, cup_photo_heart_blue).\
                                row(cup_photo_heart_pink).row(admin_back_to_items, admin_quit)
cup_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_cup_photos')
admin_cup_to_do = InlineKeyboardMarkup()
admin_cup_to_do.row(cup_messages, cup_photos).row(admin_back_to_items, admin_quit)


canvas_message = InlineKeyboardButton(text='canvas', callback_data='canvas')
canvas_size_message = InlineKeyboardButton(text='canvas_size', callback_data='canvas_size')
canvas_message_call = InlineKeyboardMarkup().row(canvas_message, canvas_size_message).row(admin_back_to_items, admin_quit)
canvas_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_canvas_messages')

canvas_photo = InlineKeyboardButton(text='canvas', callback_data='goods/Холсты/холст.png')
canvas_photo_call = InlineKeyboardMarkup().row(canvas_photo).row(admin_back_to_items, admin_quit)
canvas_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_canvas_photos')

admin_canvas_to_do = InlineKeyboardMarkup()
admin_canvas_to_do.row(canvas_messages, canvas_photos).row(admin_back_to_items, admin_quit)


notebook_message = InlineKeyboardButton(text='notebook', callback_data='notebook_message')
notebook_message_call = InlineKeyboardMarkup().row(notebook_message).row(admin_back_to_items, admin_quit)
notebook_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_notebook_messages')

notebook_sharp_photo = InlineKeyboardButton(text='notebook_sharp', callback_data='goods/Блокноты/Блокнот (листы в клетку).png')
notebook_line_photo = InlineKeyboardButton(text='notebook_line', callback_data= 'goods/Блокноты/Блокнот (листы в линейку).png')
notebook_empty_photo = InlineKeyboardButton(text='notebook_empty', callback_data= 'goods/Блокноты/Блокнот (листы пустые).png')
notebook_dot = InlineKeyboardButton(text='notebook_dot', callback_data= 'goods/Блокноты/Блокнот (листы в точку).png')
notebook_photo_call = InlineKeyboardMarkup().row(notebook_sharp_photo, notebook_line_photo).row(notebook_empty_photo, notebook_dot).row(admin_back_to_items, admin_quit)
notebook_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_notebook_photos')

admin_notebook_to_do = InlineKeyboardMarkup()
admin_notebook_to_do.row(notebook_messages, notebook_photos).row(admin_back_to_items, admin_quit)


badges_message = InlineKeyboardButton(text='insignia', callback_data='insignia_')
badges_message_call = InlineKeyboardMarkup().row(badges_message).row(admin_back_to_items, admin_quit)
badges_messages = InlineKeyboardButton(text='Изменить текст', callback_data='change_badges_messages')

badges_photo = InlineKeyboardButton(text='insignia', callback_data='goods/Значки/значки.png')
badges_photo_call = InlineKeyboardMarkup().row(badges_photo).row(admin_back_to_items, admin_quit)
badges_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_badges_photos')

admin_badges_to_do = InlineKeyboardMarkup()
admin_badges_to_do.row(badges_messages, badges_photos).row(admin_back_to_items, admin_quit)


passport_message = InlineKeyboardButton(text='pass', callback_data='pass_message')
passport_type_message = InlineKeyboardButton(text='pass_type', callback_data='pass_type_')
passport_color_sub = InlineKeyboardButton(text='pass_color_sub', callback_data='pass_color_sub_')
passport_color_uf = InlineKeyboardButton(text='pass_color_uf', callback_data='pass_color_uf_')
passport_message_call = InlineKeyboardMarkup().row(passport_message, passport_type_message)\
                                                .row(passport_color_sub, passport_color_uf).row(admin_back_to_items, admin_quit)
passport_messages = InlineKeyboardButton(text='Изменить размер', callback_data='change_pass_messages')

pass_uf_bl_photo = InlineKeyboardButton(text='pass_uf_bl', callback_data='goods/Обложка на паспорт/UF печать/Чёрная.png')
pass_uf_bl_dop_photo = InlineKeyboardButton(text='pass_uf_bl_dop', callback_data='goods/Обложка на паспорт/UF печать/BL ДОП.png')
pass_uf_wh_photo = InlineKeyboardButton(text='pass_uf_wh', callback_data='goods/Обложка на паспорт/UF печать/Белая.png')
pass_uf_wh_dop_photo = InlineKeyboardButton(text='pass_uf_wh_dop', callback_data='goods/Обложка на паспорт/UF печать/WHДОП.png')
pass_sub_red_photo = InlineKeyboardButton(text='pass_sub_red', callback_data='goods/Обложка на паспорт/Сублимационная печать/Красная.png')
pass_sub_red_dop1_photo = InlineKeyboardButton(text='pass_sub_red_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/RD ДОП (1).png')
pass_sub_red_dop2_photo = InlineKeyboardButton(text='pass_sub_red_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/RD ДОП (2).png')
pass_sub_red_dop3_photo = InlineKeyboardButton(text='pass_sub_red_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/RD ДОП (3).png')
pass_sub_orange_photo = InlineKeyboardButton(text='pass_sub_orange', callback_data='goods/Обложка на паспорт/Сублимационная печать/Оранжевый.png')
pass_sub_orange_dop1_photo = InlineKeyboardButton(text='pass_sub_orange_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/OR ДОП (1).png')
pass_sub_orange_dop2_photo = InlineKeyboardButton(text='pass_sub_orange_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/OR ДОП (2).png')
pass_sub_orange_dop3_photo = InlineKeyboardButton(text='pass_sub_orange_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/OR ДОП (3).png')
pass_sub_pink_photo = InlineKeyboardButton(text='pass_sub_pink', callback_data='goods/Обложка на паспорт/Сублимационная печать/Розовая.png')
pass_sub_pink_dop1_photo = InlineKeyboardButton(text='pass_sub_pink_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/PN ДОП (1).png')
pass_sub_pink_dop2_photo = InlineKeyboardButton(text='pass_sub_pink_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/PN ДОП (2).png')
pass_sub_pink_dop3_photo = InlineKeyboardButton(text='pass_sub_pink_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/PN ДОП (3).png')
pass_sub_salad_photo = InlineKeyboardButton(text='pass_sub_salad', callback_data='goods/Обложка на паспорт/Сублимационная печать/Салатовая.png')
pass_sub_salad_dop1_photo = InlineKeyboardButton(text='pass_sub_salad_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/SG ДОП (1).png')
pass_sub_salad_dop2_photo = InlineKeyboardButton(text='pass_sub_salad_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/SG ДОП (2).png')
pass_sub_salad_dop3_photo = InlineKeyboardButton(text='pass_sub_salad_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/SG ДОП (3).png')
pass_sub_blue_photo = InlineKeyboardButton(text='pass_sub_blue', callback_data='goods/Обложка на паспорт/Сублимационная печать/Синяя.png')
pass_sub_blue_dop1_photo = InlineKeyboardButton(text='pass_sub_blue_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/SB ДОП (1).png')
pass_sub_blue_dop2_photo = InlineKeyboardButton(text='pass_sub_blue_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/SB ДОП (2).png')
pass_sub_blue_dop3_photo = InlineKeyboardButton(text='pass_sub_blue_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/SB ДОП (3).png')
pass_sub_black_photo = InlineKeyboardButton(text='pass_sub_black', callback_data='goods/Обложка на паспорт/Сублимационная печать/Чёрная.png')
pass_sub_black_dop1_photo = InlineKeyboardButton(text='pass_sub_black_dop1', callback_data='goods/Обложка на паспорт/Сублимационная печать/BL ДОП (1).png')
pass_sub_black_dop2_photo = InlineKeyboardButton(text='pass_sub_black_dop2', callback_data='goods/Обложка на паспорт/Сублимационная печать/BL ДОП (2).png')
pass_sub_black_dop3_photo = InlineKeyboardButton(text='pass_sub_black_dop3', callback_data='goods/Обложка на паспорт/Сублимационная печать/BL ДОП (3).png')
pass_photo_call = InlineKeyboardMarkup().row(pass_uf_bl_photo, pass_uf_bl_dop_photo, pass_uf_wh_photo, pass_uf_wh_dop_photo)
pass_photo_call.row(pass_sub_red_photo, pass_sub_red_dop1_photo, pass_sub_red_dop2_photo, pass_sub_red_dop3_photo)
pass_photo_call.row(pass_sub_orange_photo, pass_sub_red_dop1_photo, pass_sub_red_dop2_photo, pass_sub_red_dop3_photo)
pass_photo_call.row(pass_sub_pink_photo, pass_sub_pink_dop1_photo, pass_sub_pink_dop2_photo, pass_sub_pink_dop3_photo)
pass_photo_call.row(pass_sub_salad_photo, pass_sub_salad_dop1_photo, pass_sub_salad_dop2_photo, pass_sub_salad_dop3_photo)
pass_photo_call.row(pass_sub_blue_photo, pass_sub_blue_dop1_photo, pass_sub_blue_dop2_photo, pass_sub_blue_dop3_photo)
pass_photo_call.row(pass_sub_black_photo, pass_sub_black_dop1_photo, pass_sub_black_dop2_photo, pass_sub_black_dop3_photo)
pass_photo_call.row(admin_back_to_items, admin_quit)
pass_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_pass_photos')
admin_pass_to_do = InlineKeyboardMarkup()
admin_pass_to_do.row(passport_messages, pass_photos).row(admin_back_to_items, admin_quit)


mouse_pad_message = InlineKeyboardButton(text='mouse_pad_description', callback_data='mouse_pad_description_message')
mouse_pad_message_call = InlineKeyboardMarkup().row(mouse_pad_message).row(admin_back_to_items, admin_quit)
mouse_pad_messages = InlineKeyboardButton(text='Изменить размер', callback_data='change_mouse_pad_messages')

mouse_pad_photo = InlineKeyboardButton(text='mouse_pad', callback_data='goods/Коврик для мышки.png')
mouse_pad_photo_call = InlineKeyboardMarkup().row(mouse_pad_photo).row(admin_back_to_items, admin_quit)
mouse_pad_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_mouse_pad_photos')

admin_mouse_pad_to_do = InlineKeyboardMarkup()
admin_mouse_pad_to_do.row(mouse_pad_messages, mouse_pad_photos).row(admin_back_to_items, admin_quit)


cardholder_message = InlineKeyboardButton(text='cardholder', callback_data='cardholder')
cardholder_type_message = InlineKeyboardButton(text='cardholder_type', callback_data='cardholder_type')
cardholder_color_message = InlineKeyboardButton(text='cardholder_color', callback_data='cardholder_color')
cardholder_message_call = InlineKeyboardMarkup().row(cardholder_message, cardholder_type_message).row(cardholder_color_message).row(admin_back_to_items, admin_quit)
cardholder_messages = InlineKeyboardButton(text='Изменить размер', callback_data='change_cardholder_messages')

cardholder_straight_photo = InlineKeyboardButton(text='cardholder_straight', callback_data='goods/Картхолдер/Картхолдер BL.png')
cardholder_oblique_bg_photo = InlineKeyboardButton(text='cardholder_oblique_bg', callback_data='goods/Картхолдер/Картхолдер косой срез/Картхолдер BG.png')
cardholder_oblique_bl_photo = InlineKeyboardButton(text='cardholder_oblique_bl', callback_data='goods/Картхолдер/Картхолдер косой срез/Картхолдер BL.png')
cardholder_oblique_gr_photo = InlineKeyboardButton(text='cardholder_oblique_gr', callback_data='goods/Картхолдер/Картхолдер косой срез/Картхолдер GR.png')
cardholder_oblique_lg_photo = InlineKeyboardButton(text='cardholder_oblique_lg', callback_data='goods/Картхолдер/Картхолдер косой срез/Картхолдер LG.png')
cardholder_oblique_pn_photo = InlineKeyboardButton(text='cardholder_oblique_pn', callback_data='goods/Картхолдер/Картхолдер косой срез/Картхолдер PN.png')
cardholder_photo_call = InlineKeyboardMarkup().row(cardholder_straight_photo, cardholder_oblique_bg_photo, cardholder_oblique_bl_photo)
cardholder_photo_call.row(cardholder_oblique_gr_photo, cardholder_oblique_lg_photo, cardholder_oblique_pn_photo)
cardholder_photo_call.row(admin_back_to_items, admin_quit)
cardholder_photos = InlineKeyboardButton(text='Изменить фото', callback_data='change_cardholder_photos')

admin_cardholder_to_do = InlineKeyboardMarkup()
admin_cardholder_to_do.row(cardholder_messages, cardholder_photos).row(admin_back_to_items, admin_quit)