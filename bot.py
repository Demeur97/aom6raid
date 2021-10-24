import telebot
import config
from telebot import TeleBot, types

bot = telebot.TeleBot(config.TOKEN)

# меню start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)  
    url_button1 = types.InlineKeyboardButton(text="Google таблица для заметок", url="https://docs.google.com/spreadsheets/d/193WbaCyefgRWNGf4lpQ0pOojkB7AhzV5XmpqSqMihy8/edit?usp=sharing")
    url_button2 = types.InlineKeyboardButton(text="Канал с видео", url="https://t.me/aom6raid")
    url_button3 = types.InlineKeyboardButton(text="Беседа", url="https://t.me/aom6raidchat")
    url_button4 = types.InlineKeyboardButton(text="Бот AoM с другой полезной информацией", url="https://t.me/AmadeusAOM_bot")
    url_button5 = types.InlineKeyboardButton(text="Автор бота", url="https://t.me/demeur97")
    photo = open ('Инфо/1.jpg', 'rb')
    keyboard.add(url_button1, url_button2, url_button3, url_button4, url_button5)
    bot.send_photo(message.chat.id, photo, "Данный бот создан для хранения информации по 6 рейду Age of Magic.\nДля вызова меню бота направьте сообщение с текстом: <strong>Меню</strong>\n\nЕсли Вы хотите поучаствовать в развитии бота, ниже расположена ссылка на Google таблицу, где Вы можете оставить свои комментарии, а также другие полезные ресурсы:", parse_mode="html",  reply_markup=keyboard)

# 1 страница меню
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('1 линия')
        item2 = types.KeyboardButton('2 линия')
        item3 = types.KeyboardButton('3 линия')
        item4 = types.KeyboardButton('4 линия')
        item5 = types.KeyboardButton('5 линия')
        item6 = types.KeyboardButton('6 линия')
        item7 = types.KeyboardButton('7 линия')
        item8 = types.KeyboardButton('8 линия')
        boss = types.KeyboardButton('Боссы')
        info = types.KeyboardButton('❗Информация❗')
        
        markup.add(item1, item2, item3, item4, item5, item6, item7,item8,boss, info)
        photo = open ('Рейд/Рейд.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = "Выберите линию, согласно схеме выше:", reply_markup = markup)

#меню
    elif message.text == '⬅️ Меню':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('1 линия')
        item2 = types.KeyboardButton('2 линия')
        item3 = types.KeyboardButton('3 линия')
        item4 = types.KeyboardButton('4 линия')
        item5 = types.KeyboardButton('5 линия')
        item6 = types.KeyboardButton('6 линия')
        item7 = types.KeyboardButton('7 линия')
        item8 = types.KeyboardButton('8 линия')
        boss = types.KeyboardButton('Боссы')
        info = types.KeyboardButton('❗Информация❗')
        
        markup.add(item1, item2, item3, item4, item5, item6, item7,item8,boss, info)
        photo = open ('Рейд/Рейд.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = "Выберите линию, согласно схеме выше:", reply_markup = markup)

#информация
    elif message.text == '❗Информация❗':
        keyboard = types.InlineKeyboardMarkup(row_width=1)  
        url_button1 = types.InlineKeyboardButton(text="Google таблица для заметок", url="https://docs.google.com/spreadsheets/d/193WbaCyefgRWNGf4lpQ0pOojkB7AhzV5XmpqSqMihy8/edit?usp=sharing")
        url_button2 = types.InlineKeyboardButton(text="Канал с видео", url="https://t.me/aom6raid")
        url_button3 = types.InlineKeyboardButton(text="Беседа", url="https://t.me/aom6raidchat")
        url_button4 = types.InlineKeyboardButton(text="Бот AoM с другой полезной информацией", url="https://t.me/AmadeusAOM_bot")
        url_button5 = types.InlineKeyboardButton(text="Автор бота", url="https://t.me/demeur97")
        photo = open ('Инфо/1.jpg', 'rb')
        keyboard.add(url_button1, url_button2, url_button3, url_button4, url_button5)
        bot.send_photo(message.chat.id, photo, "Данный бот создан для хранения информации по 6 рейду Age of Magic.\nДля вызова меню бота направьте сообщение с текстом: <strong>Меню</strong>\n\nЕсли Вы хотите поучаствовать в развитии бота, ниже расположена ссылка на Google таблицу, где Вы можете оставить свои комментарии, а также другие полезные ресурсы:", parse_mode="html",  reply_markup=keyboard)

#1 линия
    elif message.text == '1 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('1/1')
        item2 = types.KeyboardButton('1/2')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

    #1 линия 1 точка
    elif message.text == '1/1':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nМожно на авто")
    #1 линия 2 точка
    elif message.text == '1/2':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nМожно на авто")
    #1 линия 3 точка
    #1 линия 4 точка
    #1 линия 5 точка
    #1 линия 6 точка

#2 линия  
    elif message.text == '2 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('2/1')
        item2 = types.KeyboardButton('2/2')
        item3 = types.KeyboardButton('2/3')
        item4 = types.KeyboardButton('2/4 (Суккуба)')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item3, item4, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)
    #2 линия 1 точка 
    elif message.text == '2/1':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #2 линия 2 точка 
    elif message.text == '2/2':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\n3 волны проходятся без проблем. На 4 волне, если пак слабый, есть риск потерять Сакриф/Тироса")
    #2 линия 3 точка 
    elif message.text == '2/3':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/Дикие1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто. Эффект: Массовое лечение/Неубиваемость")
        bot.send_photo(message.chat.id, photo2, caption = "№2. Глориана Тилеана Кернуол Маэглин Идриль\n\nКомментарий:\nМожно на авто. Эффект: Воскрешение через 4 хода")

    #2 линия 4 точка 
    elif message.text == '2/4 (Суккуба)':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусТилеана.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nВ конце 3 волны должны быть фулл фул щиты, откат скиллов. Юзаем 2 скилл Сакриф, Магнусом 3 скиллом добиваем перса на 3 волне. На 4 волне Тиросом сначала 2 скилл, далее можно на авто. В случае, если не добили - второй заход варварами: Дэнайа, Семь ножей (3 скилл наносит хороший дамаг), Беллара, Мэдб, Азариэль")
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Тилеана\n\nКомментарий:\nПеред 4 волной нужно кинуть 2 скилл сакриф и откатить скиллы остальных героев.\nСсылка: https://youtu.be/cOvr4lKJbng")        
    #2 линия 5 точка
    #2 линия 6 точка
    #2 линия 7 точка
    #2 линия 8 точка
    #2 линия 9 точка
    #2 линия 10 точка
    #2 линия 11 точка

#3 линия 
    elif message.text == '3 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('3/1')
        item2 = types.KeyboardButton('3/2')
        item3 = types.KeyboardButton('3/3')
        item12 = types.KeyboardButton('3/12 (Камень)')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item3, item12, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)
        #3 линия 1 точка 
    elif message.text == '3/1':
        photo1 = open ('Пачки/Дикие1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "Глориана Тилеана Кернуол Маэглин Идриль\n\nКомментарий:\nАвто, в конце 2/3 линии если персонаж умер стараться его поднять\n\nСсылка: https://youtu.be/aSq_Au3movs")

    #3 линия 2 точка 
    elif message.text == '3/2':
        photo1 = open ('Пачки/Дикие1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Глориана Тилеана Кернуол Маэглин Идриль\n\nКомментарий:\nАвто, в конце 2/3 линии если персонаж умер стараться его поднять\n\nСсылка: https://youtu.be/HYNMnbGql80")

    #3 линия 3 точка 
    elif message.text == '3/3':
        photo1 = open ('Пачки/Дикие1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Глориана Тилеана Кернуол Маэглин Идриль\n\nКомментарий:\nАвто, в конце 2/3 линии если персонаж умер стараться его поднять\n\nСсылка: https://youtu.be/rp8FmNgBRnM")
    #3 линия 4 точка
    #3 линия 5 точка
    #3 линия 6 точка
    #3 линия 7 точка
    #3 линия 8 точка
    #3 линия 9 точка
    #3 линия 10 точка
    #3 линия 11 точка
    #3 линия 12 точка
    elif message.text == '3/12 (Камень)':
        photo1 = open ('Пачки/ГоблиныТирос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Гоблинус Тирос Пронырникс Шустр Гоблушка Верзила Крипс\n\nКомментарий:\nГоблушка - 4 скилл(наносит по противнику не гоблину урон, равный 25% от текущего здоровья цели, игнорирующий доспех и сопротивление магическому урону), Тирос - 2 скилл(с шансом 100% критический удар также нанесёт дополнительный урон в размере 9% от максимального запаса здоровья цели).\n\nСсылка: https://youtu.be/8ysB-0t3aOw")
#4 линия
    elif message.text == '4 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('4/1')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

    #4 линия 1 точка 
    elif message.text == '4/1':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #4 линия 2 точка 
    #4 линия 3 точка 
    #4 линия 4 точка 
    #4 линия 5 точка 
    #4 линия 6 точка 
    #4 линия 7 точка 
    #4 линия 8 точка 
    #4 линия 9 точка 
    #4 линия 10 точка 
    #4 линия 11 точка 

#5 линия 
    elif message.text == '5 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('5/1')
        item2 = types.KeyboardButton('5/2')
        item3 = types.KeyboardButton('5/3 (Драконир)')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item3, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)
    #5 линия 1 точка 
    elif message.text == '5/1':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #5 линия 2 точка 
    elif message.text == '5/2':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #5 линия 3 точка (Драконир)
    elif message.text == '5/3 (Драконир)':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто, с слабым паком могут возникнуть проблеме на 4 волне, где Драконир. На 4 волне можно использовать Диких эльфов") 
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна полуавто. Может не хватить времени")   
    #5 линия 4 точка 
    #5 линия 5 точка 
    #5 линия 6 точка 
    #5 линия 7 точка 
    #5 линия 8 точка 
    #5 линия 9 точка 

#6 линия
    elif message.text == '6 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('6/1')
        item2 = types.KeyboardButton('6/2')
        item3 = types.KeyboardButton('6/3')
        item4 = types.KeyboardButton('6/4')
        item5 = types.KeyboardButton('6/5')
        item6 = types.KeyboardButton('6/6')
        item7 = types.KeyboardButton('6/7')
        item8 = types.KeyboardButton('6/8 (Трорин)')
        item9 = types.KeyboardButton('6/9')
        item10 = types.KeyboardButton('6/10')

        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

        #6 линия 1 точка
    elif message.text == '6/1':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 2 точка
    elif message.text == '6/2':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 3 точка
    elif message.text == '6/3':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 4 точка
    elif message.text == '6/4':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар")
        #6 линия 5 точка
    elif message.text == '6/5':
        photo1 = open ('Пачки/АртусЛакки.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Лакки")   
        #6 линия 6 точка
    elif message.text == '6/6':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 7 точка
    elif message.text == '6/7':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 8 точка (Трорин)
    elif message.text == '6/8 (Трорин)':
        photo1 = open ('Пачки/ТроринАзариэль.jpg', 'rb')
        photo2 = open ('Пачки/ТроринГномы.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Трорин, Троддар, Велундар, Харгрим, Азариэль (4 волна)\n\n Комментарий: Используем 2 скилл Трорина, Азариэль и Харгримом кидаем хил. Босс бьет 3 скиллом и получает ответ урона.") 
        bot.send_photo(message.chat.id, photo2, caption = "№2. Трорин, Троддар, Велундар, Харгрим, Ангрим (4 волна)\n\n Комментарий: Используем 2 скилл Трорина, Харгримом кидаем хил. Босс бьет 3 скиллом и получает ответ урона.")  
        #6 линия 9 точка
    elif message.text == '6/9':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос\n\n Комментарий:\nНа 3 волне когда остаются только Мидрины и Мэдб нужно руками. Если не успеваете по времени можно добить Гоблинами. Эффект: Кража здоровья")
        #6 линия 10 точка
    elif message.text == '6/10':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос")
        #6 линия 11 точка
    
#7 линия
    elif message.text == '7 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('7/1')
        item2 = types.KeyboardButton('7/2')
        item4 = types.KeyboardButton('7/4 (Азариэль)')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item4, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

    #7 линия 1 группа
    elif message.text == '7/1':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #7 линия 2 группа
    elif message.text == '7/2':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #7 линия 3 группа
    #7 линия 4 группа (Азариэль)
    elif message.text == '7/4 (Азариэль)':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна руками.")
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна руками.")
    #7 линия 5 группа
    #7 линия 6 группа

#8 линия
    elif message.text == '8 линия':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('8/1')
        item3 = types.KeyboardButton('8/3')
        item4 = types.KeyboardButton('8/4')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item3, item4, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

    #8 линия 1 группа
    elif message.text == '8/1':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто")
    #8 линия 2 группа
    #8 линия 3 группа
    elif message.text == '8/3':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nМожно на авто")
    #8 линия 4 группа
    elif message.text == '8/4':
        photo1 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nМожно на авто")

#Боссы
    elif message.text == 'Боссы':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        item1 = types.KeyboardButton('Азариэль')
        item4 = types.KeyboardButton('Драконир')
        item5 = types.KeyboardButton('Суккуба')
        item7 = types.KeyboardButton('Трорин')
        item12 = types.KeyboardButton('Камень')
        menu = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item4, item5, item7, item12, menu) 
        bot.send_message(message.chat.id, "Выберите точку:", reply_markup = markup)

    #Азариэль
    elif message.text == 'Азариэль':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна руками.")
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна руками.")
    #Болотная убийца
    #Дайме
    #Драконир 
    elif message.text == 'Драконир':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусЭлиос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nМожно на авто, с слабым паком могут возникнуть проблеме на 4 волне, где Драконир. На 4 волне можно использовать Диких эльфов") 
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Элиос\n\nКомментарий:\nК 4 волне необходимо нарастить щиты, в конце 3 волны желательно сбросить откат скиллов. 1-3 волна авто, 4 волна полуавто. Может не хватить времени")   
    
    #Cуккуба
    elif message.text == 'Суккуба':
        photo1 = open ('Пачки/АртусРойнар.jpg', 'rb')
        photo2 = open ('Пачки/АртусТилеана.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Артус Магнус Сакриф Тирос Ройнар\n\nКомментарий:\nВ конце 3 волны должны быть фулл фул щиты, откат скиллов. Юзаем 2 скилл Сакриф, Магнусом 3 скиллом добиваем перса на 3 волне. На 4 волне Тиросом сначала 2 скилл, далее можно на авто. В случае, если не добили - второй заход варварами: Дэнайа, Семь ножей (3 скилл наносит хороший дамаг), Беллара, Мэдб, Азариэль")
        bot.send_photo(message.chat.id, photo2, caption = "№2. Артус Магнус Сакриф Тирос Тилеана\n\nКомментарий:\nПеред 4 волной нужно кинуть 2 скилл сакриф и откатить скиллы остальных героев.\nСсылка: https://youtu.be/cOvr4lKJbng")        
    #Мидрин
    #Трорин
    elif message.text == 'Трорин':
        photo1 = open ('Пачки/ТроринАзариэль.jpg', 'rb')
        photo2 = open ('Пачки/ТроринГномы.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Трорин, Троддар, Велундар, Харгрим, Азариэль (4 волна)\n\n Комментарий: Используем 2 скилл Трорина, Азариэль и Харгримом кидаем хил. Босс бьет 3 скиллом и получает ответ урона.") 
        bot.send_photo(message.chat.id, photo2, caption = "№2. Трорин, Троддар, Велундар, Харгрим, Ангрим (4 волна)\n\n Комментарий: Используем 2 скилл Трорина, Азариэль и Харгримом кидаем хил. Босс бьет 3 скиллом и получает ответ урона.")  
    #Прук Кривоморд
    #Древерад
    #Сунь Укун
    #Камень
    elif message.text == 'Камень':
        photo1 = open ('Пачки/ГоблиныТирос.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption = "№1. Гоблинус Тирос Пронырникс Шустр Гоблушка Верзила Крипс\n\nКомментарий:\nГоблушка - 4 скилл(наносит по противнику не гоблину урон, равный 25% от текущего здоровья цели, игнорирующий доспех и сопротивление магическому урону), Тирос - 2 скилл(с шансом 100% критический удар также нанесёт дополнительный урон в размере 9% от максимального запаса здоровья цели).\n\nСсылка: https://youtu.be/8ysB-0t3aOw")

bot.polling(none_stop=True)
