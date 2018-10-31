from json import load
from requests import get

def status():
    config = load_properties()
    response = get(config['url'], headers=config['headers'])
    jobs = response.json()['jobs']
    for i in range(len(jobs)):
        print('branch: ' + jobs[i]['name'] + '  - status: ' + jobs[i]['color'])


def load_properties():
    with open('jenkins/config.json', 'r') as f: 
        config = load(f)
    return config