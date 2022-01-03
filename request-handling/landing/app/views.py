from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    param = request.GET.get('from-landing', None)
    counter_show[param] += 1
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    param = request.GET.get('ab-test-arg', None)
    template = ''
    if param == 'original':
        counter_click[param] += 1
        template = 'landing.html'
    elif param == 'test':
        counter_click[param] += 1
        template = 'landing_alternate.html'
    # else:
    #     template = 'landing.html'

    return render(request, template)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    counter_click_original = counter_click.get('original')
    counter_click_test = counter_click.get('test')
    counter_show_original = counter_show.get('original')
    counter_show_test = counter_show.get('test')
    test_conversion = round(counter_show_test / counter_click_test, 2) \
        if counter_show_test and counter_click_test else None
    original_conversion = round(counter_show_original / counter_click_original, 2) \
        if counter_show_original and counter_click_original else None
    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
