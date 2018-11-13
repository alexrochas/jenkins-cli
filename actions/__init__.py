from jenkins import get_status, deploy_job
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings


def status(job):
    target_job = job.split(' ')[-1]
    get_status(target_job)


def deploy(job):
    target_job = job.split(' ')[-1]
    target_env = job.split(' ')[1]
    deploy_job(target_job, target_env)
