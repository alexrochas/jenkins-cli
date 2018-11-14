from json import load
from requests import get
from requests import post


def get_status(job):
    config = load_properties()
    response = get(_build_status_url(
        config['url'], job), headers=config['headers'])
    jobs = response.json()['jobs']
    for i in range(len(jobs)):
        print('branch: ' + jobs[i]['name'] + '  - status: ' + jobs[i]['color'])

    return response.status_code


def deploy_job(job, env):
    config = load_properties()
    response = post(_build_deploy_url(
        config['url'], job, env),
        data={},
        headers=config['headers'])

    print(response)


def load_jobs():
    config = load_properties()
    response = get(_build_load_url(config['url']),
                   headers=config['headers'])

    response_jobs = response.json()['jobs']
    return response_jobs


def load_properties():
    with open('jenkins/config.json', 'r') as f:
        config = load(f)
    return config


def _build_status_url(url, job):
    return url + 'view/Cartoes/job/Plataforma/job/' + job + '/api/json?tree=jobs[name,url,color]'


def _build_deploy_url(url, job, env):
    return url + 'job/Plataforma/job/' + job + '/job/' + env + '/buildWithParameters'


def _build_load_url(url):
    return url + 'job/Plataforma/api/json?tree=jobs[name]'
