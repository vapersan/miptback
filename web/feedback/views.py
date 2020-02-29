import json

from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from feedback.models import Feedback

aliceSession = {}


@csrf_exempt
def alice_skill(request):
    try:
        req_json = json.loads(request.body)
    except Exception:
        req_json = {'version': 1, 'session': 1}
    uid = req_json['session']['user_id']
    cmd = req_json['request']['command']
    if uid not in aliceSession:
        aliceSession[uid] = 0
    response = {
        "version": req_json['version'],
        "session": req_json['session'],
        "response": {
            "end_session": True,
            'text': 'Привет :D'
        }
    }
    if aliceSession[uid] == 0:
        # TODO: make it sound must better
        response['response']['text'] = 'Привет!'
        aliceSession[uid] += 1
    elif aliceSession[uid] == 1:
        if len(cmd) < 20:
            response['response']['text'] = 'Очень мало слов. Текст должен быть более 20 символов'
        else:
            Feedback(text=cmd).save()
            response['response']['text'] = 'Спасибо за отзыв!'
            response['response']['end_session'] = True
    aliceSession[uid] = aliceSession[uid] % 2
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
