from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import admin_kb as kb
from keyboards import client_kb
from config import hudi_size, t_shirt_size
import json


with open('sizes_data.json', 'r') as file:
    data = json.load(file)
 
admins_id = [336363978, 503386612, 333347544]
admin_t_shirt = t_shirt_size
admin_hudi_size = hudi_size


#==================================Проверка прав пользователя==============================
async def admin_check_handler(message: types.Message):
    count = 0

    for (index, _) in enumerate(admins_id):
        if admins_id[index] == message.from_user.id:
            count+=1
        print(admins_id[index])
    if count == 1:
        await message.answer(text='Вы вошли в бота в режиме модерации.\nЧто будем делать?',
                               reply_markup=kb.admin_items)
    else:
        await message.answer(text='У вас недостаточно прав для выполнения данной команды',
                              reply_markup=client_kb.state2)
    await message.delete()
    
    
#=================================Админские колбеки=============================================

async def admin_quit_call(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Вы вышли из режима модерации',
                           reply_markup=client_kb.state2)
    await callback.message.delete()
    
    
async def admin_back_to_start(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Выберите товар: ', reply_markup=kb.admin_items)
    await callback.message.delete()
    
    
async def admin_choosed_good_call(callback: types.CallbackQuery):
    match callback.data:
        case 'admin_t_shirt':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_t_shirt_to_do)
        case 'admin_hudi':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_hoodie_to_do)
        case 'admin_shopper':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_shopper_to_do)
        case 'admin_pillow':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_pillow_to_do)
        case 'admin_cup':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_cup_to_do)
        case 'admin_canvas':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_canvas_to_do)
        case 'admin_notebook':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_notebook_to_do)
        case 'admin_badges':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_badges_to_do)
        case 'admin_passport':
            await callback.message.answer('Выберите действие: ', reply_markup=kb.admin_pass_to_do)
        case 'admin_mouse_pad':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_mouse_pad_to_do)
        case 'admin_cardholder':
            await callback.message.answer('Выберите действие:', reply_markup=kb.admin_cardholder_to_do)
    await callback.message.delete()
    
#====================================RESIZE===================================================
    
async def admin_resize_call(callback: types.CallbackQuery):
    match callback.data:
        case 'change_t_shirt_size':
            await callback.message.answer('Размеры футболки:', reply_markup=kb.tshirt_size)
            
        case 'change_hoodie_size':
            await callback.message.answer('Размеры худи:', reply_markup=kb.hudi_size_)
    await callback.message.delete()

async def admin_resize_tshirt_call(callback: types.CallbackQuery):
    match callback.data:
        case 'ts_xs_tf':
            if data["t_shirt"]["xs"]:
                data["t_shirt"]['xs'] = False
            else:
                data["t_shirt"]['xs'] = True
            kb.ts_xs_tf.text = str(data["t_shirt"]['xs'])
            
        case 'ts_s_tf':
            if data["t_shirt"]["s"]:
                data["t_shirt"]['s'] = False
            else:
                data["t_shirt"]['s'] = True
            kb.ts_s_tf.text = str(data["t_shirt"]['s'])
            
        case 'ts_m_tf':
            if data["t_shirt"]["m"]:
                data["t_shirt"]['m'] = False
            else:
                data["t_shirt"]['m'] = True
            kb.ts_m_tf.text = str(data["t_shirt"]['m'])
            
        case 'ts_l_tf':
            if data["t_shirt"]["l"]:
                data["t_shirt"]['l'] = False
            else:
                data["t_shirt"]['l'] = True
            kb.ts_l_tf.text = str(data["t_shirt"]['l'])
            
        case 'ts_xl_tf':
            if data["t_shirt"]["xl"]:
                data["t_shirt"]['xl'] = False
            else:
                data["t_shirt"]['xl'] = True
            kb.ts_xl_tf.text = str(data["t_shirt"]['xl'])
            
        case 'ts_xxl_tf':
            if data["t_shirt"]["xxl"]:
                data["t_shirt"]['xxl'] = False
            else:
                data["t_shirt"]['xxl'] = True
            kb.ts_xxl_tf.text = str(data["t_shirt"]['xxl'])
            
        case 'ts_xxxl_tf':
            if data["t_shirt"]["xxxl"]:
                data["t_shirt"]['xxxl'] = False
            else:
                data["t_shirt"]['xxxl'] = True
            kb.ts_xxxl_tf.text = str(data["t_shirt"]['xxxl'])
            
            
    await callback.message.answer('Размеры футболки:', reply_markup=kb.tshirt_size)
    with open('sizes_data.json', 'w') as fh:
        json.dump(data, fh, indent=1)
    await callback.message.delete()
    client_kb.update_state5()
    
    
async def admin_resize_hudi_call(callback: types.CallbackQuery):
    match callback.data:
        case 'hudi_xs_tf':
            if data["hudi"]["xs"]:
                data["hudi"]['xs'] = False
            else:
                data["hudi"]['xs'] = True
            kb.hudi_xs_tf.text = str(data["hudi"]['xs'])
            
        case 'hudi_s_tf':
            if data["hudi"]["s"]:
                data["hudi"]['s'] = False
            else:
                data["hudi"]['s'] = True
            kb.hudi_s_tf.text = str(data["hudi"]['s'])
            
        case 'hudi_m_tf':
            if data["hudi"]["m"]:
                data["hudi"]['m'] = False
            else:
                data["hudi"]['m'] = True
            kb.hudi_m_tf.text = str(data["hudi"]['m'])
            
        case 'hudi_l_tf':
            if data["hudi"]["l"]:
                data["hudi"]['l'] = False
            else:
                data["hudi"]['l'] = True
            kb.hudi_l_tf.text = str(data["hudi"]['l'])
            
        case 'hudi_xl_tf':
            if data["hudi"]["xl"]:
                data["hudi"]['xl'] = False
            else:
                data["hudi"]['xl'] = True
            kb.hudi_xl_tf.text = str(data["hudi"]['xl'])
            
        case 'hudi_xxl_tf':
            if data["hudi"]["xxl"]:
                data["hudi"]['xxl'] = False
            else:
                data["hudi"]['xxl'] = True
            kb.hudi_xxl_tf.text = str(data["hudi"]['xxl'])
            
        case 'hudi_xxxl_tf':
            if data["hudi"]["xxxl"]:
                data["hudi"]['xxxl'] = False
            else:
                data["hudi"]['xxxl'] = True
            kb.hudi_xxxl_tf.text = str(data["hudi"]['xxxl'])
            
        case 'hudi_4xl_tf':
            if data["hudi"]["4xl"]:
                data["hudi"]['4xl'] = False
            else:
                data["hudi"]['4xl'] = True
            kb.hudi_4xl_tf.text = str(data["hudi"]['4xl'])
            
        case 'hudi_4xl_tf':
            if data["hudi"]["5xl"]:
                data["hudi"]['5xl'] = False
            else:
                data["hudi"]['5xl'] = True
            kb.hudi_5xl_tf.text = str(data["hudi"]['5xl'])
            
    await callback.message.answer('Размеры худи:', reply_markup=kb.hudi_size_)
    with open('sizes_data.json', 'w') as fh:
        json.dump(data, fh, indent=1)
    await callback.message.delete()
    client_kb.update_state5_hoodie()
            
            
#====================================RENAME===================================================

async def admin_rename_call(callback: types.CallbackQuery):
    match callback.data:
        case 'change_t_shirt_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.t_shirt_message_call)
        case 'change_hoodie_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.hoodie_message_call)
        case 'change_shopper_messages':
            await callback.message.answer('Выберите сообщение', reply_markup=kb.shopper_message_call)
        case 'change_pillow_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.pillow_message_call)
        case 'change_cup_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.cup_message_call)
        case 'change_canvas_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.canvas_message_call)
        case 'change_canvas_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.notebook_message_call)
        case 'change_badges_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.badges_message_call)
        case 'change_pass_messages':
            await callback.message.answer('Выберите сообщение', reply_markup=kb.passport_message_call)
        case 'change_mouse_pad_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.mouse_pad_message_call)
        case 'change_cardholder_messages':
            await callback.message.answer('Выберите сообщение: ', reply_markup=kb.cardholder_message_call)
    await callback.message.delete()
    
            
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_check_handler, commands=['moderate', 'admin'])
    dp.register_callback_query_handler(admin_quit_call, text='admin_quit')
    dp.register_callback_query_handler(admin_back_to_start, text='admin_back_to_items')
    dp.register_callback_query_handler(admin_choosed_good_call, text=['admin_t_shirt', 'admin_hudi',
                                                                      'admin_shopper', 'admin_pillow',
                                                                      'admin_cup', 'admin_canvas',
                                                                      'admin_notebook', 'admin_badges',
                                                                      'admin_passport', 'admin_mouse_pad',
                                                                      'admin_cardholder'])
    #=========================resize===================
    dp.register_callback_query_handler(admin_resize_call, text=['change_t_shirt_size', 'change_hoodie_size'])
    dp.register_callback_query_handler(admin_resize_tshirt_call, text=['ts_xs_tf', 'ts_s_tf', 'ts_m_tf',
                                                                        'ts_l_tf', 'ts_xl_tf',
                                                                        'ts_xxl_tf', 'ts_xxxl_tf'])
    dp.register_callback_query_handler(admin_resize_hudi_call, text = ['hudi_xs_tf', 'hudi_s_tf',
                                                                       'hudi_m_tf', 'hudi_l_tf',
                                                                       'hudi_xl_tf', 'hudi_xxl_tf',
                                                                       'hudi_xxxl_tf'])
    #=========================rename======================
    dp.register_callback_query_handler(admin_rename_call, text=['change_t_shirt_messages',
                                                                'change_hoodie_messages',
                                                                'change_shopper_messages',
                                                                'change_pillow_messages',
                                                                'change_cup_messages',
                                                                'change_canvas_messages',
                                                                'change_notebook_messages',
                                                                'change_badges_messages',
                                                                'change_pass_messages',
                                                                'change_mouse_pad_messages',
                                                                'changecardholder_messages'])
    