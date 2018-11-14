from jenkins import load_jobs

services = []


def _get_branches():
    return ['dev', 'hlg', 'master']


def _get_services():

    if not services:
        response_jobs = load_jobs()
        for i in range(len(response_jobs)):
            services.append(response_jobs[i]['name'])

    return services


def _get_actions():
    return ['build', 'status']


def _add_element_into_dictionary(elements):
    for element in elements:
        dictionary[element] = _get_services()


def _add_none_into_dictionary(elements):
    for element in elements:
        dictionary[element] = ''


def setup():
    _add_element_into_dictionary(_get_branches())
    _add_none_into_dictionary(_get_services())


def build_dictionary(target_word):
    return dictionary[target_word]


dictionary = {
    'build': _get_branches(),
    'status': _get_services(),
    'empty': _get_actions()
}
