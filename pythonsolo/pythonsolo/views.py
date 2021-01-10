from django.shortcuts import render
from django.views import View

from .helper import get_tables, rtn


class TableView(View):

    def get(self, request, *args, **kwargs):
        table = request.GET.get('roll')

        if table:
            context = {
                'result': rtn(int(table))
            }
            return render(request, 'roll_result.html', context=context)

        context = {
            'tables': get_tables()
        }
        return render(request, 'tables.html', context=context)
