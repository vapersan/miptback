import json

from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from feedback.models import Feedback, Teacher, Questions, Answers

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


def json_resp_api_1(request):
    response_data = {
        'Фото': 'https://i.imgur.com/NNopiz5.jpg',
        'ФИО': 'Плахов Игорь Александрович',
        'Дата рождения': '20.12.2001',
        'Паспорт': '4515******, ФМС России по гор. Москве',
        'СНИЛС': '',
        'Email': 'abc123@gmail.com',
        'Телефон': '88005553535',
        'Адрес по прописке физ. лица': 'г. Москва, ул. Тверская д. * кв. *',
        'Адрес проживания физ. лица': 'г. Москва, ул. Тверская д. * кв. *',
        'Уровень обучения': 'Бакалавр',
        'Статус': 'Учится',
        'Период обучения': '01.09.2017 - 31.08.2021',
        'Факультет': 'Физтех-школа Аэрокосмических Технологий',
        'Курс': '1',
        'Группа': 'Б03-908б',
        'Базовая кафедра': ' ',
        'Форма обучения': 'Очная',
        'Источник финансирования': 'Минестерство образования РФ',
        'Должность': ' ',
        'Ставка': '',
        'Отец': '***',
        'Сестра': '***',
        'Мать': '***',
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def json_resp_api_2(request):
    response_data = {
        'Средний балл': '4.5',
        'Рейтинг по курсу': '60',
        'Рейтинг по ФШ': '31',
        'Статус': 'Учится',
        'Уровень образования': 'Бакалавр',
        'Курс': '1',
        'Подразделение': 'Физтех-школа Аэрокосмических Технологий',
        'Группа': 'Б03-908б',
        'Направление': 'Системный анализ и управление (бакалавриат)',
        'Программа': 'Теория и математические методы системного анализа',
        'Форма оплаты обучения': 'Минестерство образования РФ',
        'Базовая кафедра': ' ',
        'Научный руководтель': ' ',
        'Тема дипломной работы': ' ',
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_monthly_event(request):
    ret = []
    teachers = Teacher.objects.all()
    for teacher in teachers:
        dat = {'text': teacher.name, 'pk': teacher.pk, 'quests': []}
        for quest in Questions.objects.filter(teacher=teacher):
            dat['quests'].append({
                'text': quest.question,
                'pk': quest.id,
                'name': f"{dat['pk']}:{quest.id}"})
        ret.append(dat)
    return JsonResponse(ret, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def save_monthly_event(request):
    answers = json.loads(request.body)['data']
    for k, v in answers.items():
        Answers(answer=int(v), question_id=int(k.split(':')[1])).save()
    return HttpResponse(b'OK')
