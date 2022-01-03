
import os
from datetime import datetime
from typing import Optional

from django.shortcuts import render


def file_list(request, date: Optional[datetime] = None):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = '.'
    names_list = os.listdir(path)
    files = []
    for name in names_list:
        if os.path.isfile(os.path.join(path, name)):
            info = os.stat(name, follow_symlinks=False)
            c_time = datetime.fromtimestamp(info.st_ctime)
            m_time = datetime.fromtimestamp(info.st_mtime)

            files += [
                {'name': name,
                 'ctime': c_time,
                 'mtime': m_time,
                 },
            ]
    if date:
        files = [file for file in files if date.date() == file['ctime'].date() or date.date() == file['mtime'].date()]
    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }
    print(context)
    return render(request, template_name, context)


def file_content(request, name):
    with open(name, encoding='utf-8') as f:
        file_content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

