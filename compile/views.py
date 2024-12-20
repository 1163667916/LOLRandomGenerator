import json
import time
import random
import threading

from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from compile.models import Task
from compile.commands import commands, branches, status, platform

# Create your views here.


def get_version():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []

    for i in range(8):
        sa.append(random.choice(seed))

    result = ''.join(sa)
    return result


def insert_ten_thousand_task(request):

    nums = 100000

    for _ in range(200):
        create_lst = []
        for i in range(500):
            time = int(random.random() * 60)
            _hours = int(random.random() * 4) + 1
            start_time = datetime.now() - timedelta(time)
            _status = random.choice(status)
            end_time = start_time + \
                timedelta(hours=_hours, minutes=_hours *
                          10) if _status == 'success' else None

            kwargs = {
                'branch': random.choice(branches),
                'job_name': get_version(),
                'job_id': int(random.random() * 10000000),
                'status': _status,
                'platform': random.choice(platform),
                'command': random.choice(commands),
                'version': get_version(),
                'variables': {
                    'type': 'sdk',
                    'svn': '',
                    'variables': [{'KEY': 'BRANCH', 'VALUE': 'branch'}]
                },
                'start_time': start_time,
                'end_time': end_time,
            }
            create_lst.append(Task(**kwargs))
        Task.objects.bulk_create(create_lst)

    return HttpResponse('ok')


def task_list(request):
    task_list = Task.objects.filter(
        branch='develop',
        variables__type='build',
        command__in=commands
    ).order_by('-start_time')

    print(task_list.count())

    task_list = task_list.values(
        'id', 'branch', 'job_name',
        'job_id', 'platform', 'start_time',
        'end_time', 'command', 'status', 'variables',
        'version', user_name=F('user__name'), project_name=F('project__name')
    )

    a = {}
    for t in task_list:
        if t['command'] in a:
            a[t['command']].append(t)
        else:
            a[t['command']] = [t]

    lst = []
    for k, v in a.items():
        v[0].update({'children': v[1:11]})
        lst.append(v[0])
    return HttpResponse(json.dumps({'lst': lst}, cls=DjangoJSONEncoder))


def backend_query():
    while True:
        task_lst = Task.objects.filter(
            branch='develop', status='success').values()
        for item in task_lst:
            pass
        print('query........')
        time.sleep(5)


# threading.Thread(target=backend_query).start()
