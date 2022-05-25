import datetime


def show_input_text(text):
    return f'Input text: {text}'


def show_date_today():
    return datetime.datetime.today()


print(show_date_today())
