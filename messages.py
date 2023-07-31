from aiogram.utils.markdown import text, bold, italic, code, pre


start_message = 'Добро пожаловать!\n' \
                'Здесь Вы можете заказать широкий ассортимент товаров с Вашим изображением из нашего широкого ассортимента.\n' \
                'Хотите увидеть все доступные товары?'

goodbye = 'Всего хорошего, возвращайтесь! ;('

goods = 'Вот все доступные товары:\n• Футболка\n• Худи\n• Шоппер\n• Подушка\n' \
        '• Кружка\n• Холст\n• Блокнот\n• Значки\n• Обложка для Паспорта\n' \
        '• Коврик для мыши\n• Картхолдер\n'

t_shirt_color = 'Выберите цвет:\n• Черный\n• Белый'
t_shirt = 'Футболка\n100% хлопок и т.д'

unknown1 = 'Не понял(\nХотите начать?'
unknown2 = 'Не понял(\nХотите увидеть все доступные товары?'
unknown3 = 'Не понял(\nВыберите товар'
unknown4 = 'Не понял(\nВыберите цвет:'

MESSAGES = {
    'start': start_message,
    'goodbye': goodbye,
    #'help': help_message,
    'goods_list': goods,
    't_shirt_color': t_shirt_color,
    't_shirt': t_shirt,
    'unknown1': unknown1,
    'unknown2': unknown2,
    'unknown3': unknown3,
    'unknown4': unknown4
}
