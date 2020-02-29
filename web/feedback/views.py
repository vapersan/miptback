import json

from django.http import JsonResponse

# Create your views here.

aliceSession = {}


def alice_skill(request):
    req_json = json.loads(request.body)
    response = {
        "version": req_json['version'],
        "session": req_json['session'],
        "response": {
            "end_session": True,
            'text': 'Pong'
        }
    }
    return JsonResponse(response, ensure_ascii=False)
