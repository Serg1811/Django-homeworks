from datetime import datetime

from django import template


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    date_of_publication = datetime.fromtimestamp(value)
    difference_seconds =(datetime.today() - date_of_publication).seconds
    if difference_seconds <= 10 * 60:
        return 'только что'
    elif difference_seconds <= 24 * 60 * 60:
        hours = round(difference_seconds/(60 * 60))
        if hours in (1, 21):
            return f'{hours} час назад'
        elif hours in (2, 3, 4, 22, 23, 24):
            return f'{hours} часа назад'
        else:
            return f'{hours} часов назад'
    else:
        return date_of_publication.strftime('%Y-%m-%d')


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(quantity):
    if quantity:
        if quantity < -5:
            return 'все плохо'
        elif quantity > 5:
            return 'хорошо'
        else:
            return 'нетрально'
    else:
        return 'не определено'


@register.filter
def format_num_comments(value):
    # Ваш код
    number_of_comments = int(value)
    if number_of_comments == 0:
        return "Оставьте комментарий"
    elif 0 < number_of_comments <= 50:
        return number_of_comments
    elif number_of_comments > 50:
        return '50+'


@register.filter
def format_selftext(text: str, count: int):
    text_list = text.split(' ')
    return ' '.join(text_list[:count]) + '...' + ' '.join(text_list[-count:])
