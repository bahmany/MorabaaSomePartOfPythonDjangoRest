import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            tzname = request.session.get('django_timezone')
            if tzname:
                timezone.activate(pytz.timezone(tzname))
            else:
                timezone.activate(pytz.timezone(request.user.timezone))


    def process_response(self, request, response):
        if not request.user.is_authenticated():
            return response

        tzname = request.session.get('django_timezone')
        response.set_cookie('timezone', tzname, )
        return response
