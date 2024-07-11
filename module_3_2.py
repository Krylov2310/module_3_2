task = 'Домашняя работа по уроку "Способы вызова функции", Задача "Рассылка писем":'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()


def send_email(message, recipient,*,sender = "university.help@gmail.com"):
    gaf = ('.ru', '.net', '.com', '.hotmail')
    if message == '':
        print('Текст сообщения не должно быть пустым!')
    elif recipient == '':
        print('Адрес отправителя не должен быть пустым!')
    elif not sender.endswith(gaf) or not ('@' in sender) or \
            not recipient.endswith(gaf) or not ('@' in recipient):
        print(f'Невозможно отправить письмо с адреса - {sender} на адрес - {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса - {sender} на адрес: - {recipient}, с текстом: {message}')
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса - {sender} на адрес - {recipient}.")


send_email('', 'krylov2310@gmail.com')
send_email('Поставьте пожалуйста зачет', '')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
                   sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print()
print(thanks)
