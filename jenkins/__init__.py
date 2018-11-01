from json import load
from requests import get


def get_status(job):
    config = load_properties()
    response = get(_build_status_url(
        config['url'], job), headers=config['headers'])
    jobs = response.json()['jobs']
    for i in range(len(jobs)):
        print('branch: ' + jobs[i]['name'] + '  - status: ' + jobs[i]['color'])

    return response.status_code


def load_properties():
    with open('jenkins/config.json', 'r') as f:
        config = load(f)
    return config


def _build_status_url(url, job):
    return url + 'view/Cartoes/job/Plataforma/job/' + job + '/api/json?tree=jobs[name,url,color]'
