from datetime import datetime
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pytz
from rest_framework.response import Response


def set_timezone(request):
    if request.user.is_active == False:
        return HttpResponse(json.dumps({}),
                        content_type="application/json"
                        )

    if request.method == 'POST':
        bb = json.loads(request.body.decode("utf-8"))
        request.user.timezone = bb['timezone']
        request.user.save()
        request.session['django_timezone'] = bb['timezone']
        return redirect('/')
    else:
        return render(request, 'forms/Infrustructure/Timezone/template.html',
                      {'timezones': pytz.common_timezones,
                       "value":datetime.now()
                      })
def get_timezone(request):
    if request.user.is_active == False:
        return HttpResponse(json.dumps({"timezone":"Asia/Tehran"}),
                        content_type="application/json"
                        )
    return HttpResponse(json.dumps({"timezone":request.user.timezone}),
                        content_type="application/json"
                        )
