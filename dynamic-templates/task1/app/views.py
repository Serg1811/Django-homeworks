import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf=8') as file:
        reader = csv.reader(file, delimiter=';')
        headers = []
        rows = []
        for i, row in enumerate(reader):
            if i == 0:
                headers = row
            else:
                rows += [[value if i == 0 or value == '' else float(value) for i, value in enumerate(row)]]
    context = {'headers': headers, 'rows': rows}
    return render(request, template_name, context)
