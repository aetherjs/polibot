import telebot
import config

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

markup_year_choice = types.ReplyKeyboardMarkup(row_width=4)
item_year_1 = types.KeyboardButton('1 Курс')
item_year_2 = types.KeyboardButton('2 Курс')
item_year_3 = types.KeyboardButton('3 Курс')
item_year_4 = types.KeyboardButton('4 Курс')
markup_year_choice.add(item_year_1, item_year_2, item_year_3, item_year_4)

markup_course_choise = types.ReplyKeyboardMarkup(row_width=3)
itema = types.KeyboardButton('Бизнес-информатика')
itemb = types.KeyboardButton('Экономика')
itemc = types.KeyboardButton('Менеджемент')
markup_course_choise.add(itema, itemb, itemc)

markup_back = types.ReplyKeyboardMarkup(row_width=1)
item_back_button = types.KeyboardButton('Обратно к выбору курса')
markup_back.add(item_back_button)

current_year = 'Test'
current_course = 'Test'
current_level = ''

@bot.message_handler(commands=['start', 'chooseyear'])
def send_year_keyboard(message):
    global current_level
    current_level = 'Year'
    bot.send_message(message.chat.id, "Выберите свой курс", reply_markup=markup_year_choice)

@bot.message_handler(func=lambda message: (message.text in config.list_of_years) and current_level == 'Year')
def send_course_keyboard(message):
    global current_level
    current_level = 'Course'
    bot.send_message(message.chat.id, 'Хорошо, теперь уважите свое направление:', reply_markup=markup_course_choise)
    global current_year
    current_year = message.text

@bot.message_handler(func=lambda message: message.text in config.list_of_courses and current_level == 'Course')
def send_subject_keyboard(message):
    global current_level
    current_level = 'Subject'
    global current_course
    current_course = message.text
    list_of_subjects = []
    if (current_year == '1 Курс'):
        list_of_subjects = config.year1_dict[current_course]
    if (current_year == '2 Курс'):
        list_of_subjects = config.year2_dict[current_course]
    if (current_year == '3 Курс'):
        list_of_subjects = config.year3_dict[current_course]
    if (current_year == '4 Курс'):
        list_of_subjects = config.year4_dict[current_course]
    temp_markup = types.ReplyKeyboardMarkup(row_width=2)
    for subject in list_of_subjects:
        temp_item = types.KeyboardButton(subject)
        temp_markup.add(temp_item)
    bot.send_message(message.chat.id, 'Выберите интересующий вас курс:', reply_markup=temp_markup)

@bot.message_handler(func=lambda message: message.text in config.subjects_dict and current_level == 'Subject')
def send_subject_link(message):
    bot.send_message(message.chat.id, config.subjects_dict[message.text], reply_markup=markup_back)
    

@bot.message_handler(func=lambda message: message.text == 'Обратно к выбору курса')
def back_to_courses(message):
    send_year_keyboard(message)

bot.polling()