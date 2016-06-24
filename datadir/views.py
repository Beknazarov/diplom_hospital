from django.apps import apps
from django.http.response import JsonResponse

#
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_model_data_ajax(request):
    if request.is_ajax():
        inputname = request.POST.get('inputname')
        if inputname:
            try:
                model = apps.get_model(app_label='datadir', model_name=inputname)
                data = model.objects.all().values_list('id', 'type')
                if data:
                    context = {'result': dict(data)}
                    response = JsonResponse(context)
                    return response
                else:
                    context = {'result': 'empty'}
                    response = JsonResponse(context)
                    return response
            except:
                context = {'result': 'none'}
                response = JsonResponse(context)
                return response

                # def get_set():
                #     model = 'pulse_deficit'
                #     data = apps.get_model(app_label='datadir', model_name=model)
                #     context = data.objects.all()
                #     print(context)
