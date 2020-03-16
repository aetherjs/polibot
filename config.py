TOKEN = '1145289050:AAFlNovs5nN8EopjGgQ85sazhnYRVXL66yw'

list_of_years = ['1 Курс', '2 Курс', '3 Курс', '4 Курс']
list_of_courses = ['Бизнес-информатика','Экономика','Менеджемент']

subjects_dict = {'Делопроизводство':'https://openedu.ru/course/spbstu/CLEWO/', 'КСЕ':'https://openedu.ru/course/spbstu/CONCMOD/', 'Экология':'https://openedu.ru/course/spbstu/ECOLOGY/', 
                'Физкультура':'https://openedu.ru/course/spbstu/PHYSCUL/', 'Маркетинг':'https://openedu.ru/course/spbstu/MARKET/', 'Менеджемент':'https://openedu.ru/course/spbstu/MANAG/',
                'Философия':'https://openedu.ru/course/spbstu/PHYLOS/', 'Программирование':'https://openedu.ru/course/spbstu/WEBPYT/', 'Психология':'https://openedu.ru/course/spbstu/PSYHOL/',
                'Матметоды':'https://openedu.ru/course/spbstu/BUSMAT/', 'Основы проектной деятельности':'https://openedu.ru/course/spbstu/OPD/', 
                'Теория государства и права':'https://openedu.ru/course/spbstu/THEGOV/'}

year1_dict = {'Бизнес-информатика': ['Делопроизводство', 'КСЕ', 'Экология'],
              'Экономика': ['КСЕ', 'Экология'],
              'Менеджемент': ['Экология', 'Физкультура']
}

year2_dict = {'Бизнес-информатика': ['Маркетинг', 'Физкультура'],
              'Экономика': ['Менеджемент', 'Физкультура'],
              'Менеджемент': ['Делопроизводство', 'Маркетинг']
}

year3_dict = {'Бизнес-информатика': ['Философия', 'Программирование'],
              'Экономика': ['Психология', 'Программирование'],
              'Менеджемент': ['Философия', 'Психология']
}

year4_dict = {'Бизнес-информатика': ['Матметоды', 'Основы проектной деятельности'],
              'Экономика': ['Основы проектной деятельности', 'Программирование'],
              'Менеджемент': ['Теория государства и права', 'Основы проектной деятельности']
}