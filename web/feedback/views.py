import json

from django.http import JsonResponse

# Create your views here.

aliceSession = {}


def alice_skill(request):
    try:
        req_json = json.loads(request.body)
    except Exception:
        req_json = {'version': 1, 'session': 1}
    print(request.body)
    print(request.POST)
    print(request.GET)
    print(request.method)
    response = {
        "version": req_json['version'],
        "session": req_json['session'],
        "response": {
            "end_session": True,
            'text': 'Привет :D'
        }
    }
    return JsonResponse(response)
