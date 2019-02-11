from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from .models import KeyValue


def set_value(request):
    """create or update a key value object with keys and values given in GET method"""
    if request.method == 'GET':
        kv_created = []
        if request.GET:
            for key, val in request.GET.items():
                print(key, val)
                kv, created = KeyValue.objects.get_or_create(key=key)
                kv.value = val
                kv.save()
                kv_created += [{kv.key: kv.value, 'created':created}]
            resp = {
                'status': 'success',
                'message': _('Keys and values Successfully created or updated'),
                'data': kv_created
            }
            status_code = 200
        else:
            resp = {
                'status': 'warning',
                'message': _('No keys and values to create'),
                'data': []
            }
            status_code = 200
    else:
        resp = {
            'status': 'error',
            'message': _('method not allowed'),
        }
        status_code = 500
    return JsonResponse(resp, status=status_code)


def get_value(request):
    """get the value for the provided key"""
    if request.method == 'GET':
        key = request.GET.get('key', None)
        if key:
            value = KeyValue.objects.filter(key=key)
            if value.exists():
                resp = {
                    'status': 'success',
                    'message': _('value found'),
                    'data': {key: value.first().value}
                }
                status_code = 200
            else:
                resp = {
                    'status': 'success',
                    'message': _('value not found'),
                    'data': {}
                }
                status_code = 200
        else:
            resp = {
                'status': 'warning',
                'message': _('No key provided'),
                'data': []
            }
            status_code = 200
    else:
        resp = {
            'status': 'error',
            'message': _('method not allowed'),
        }
        status_code = 500
    print(resp)
    return JsonResponse(resp, status=status_code)


class TicTacToe(TemplateView):
    template_name = 'keyvalue/tictactoe.html'
