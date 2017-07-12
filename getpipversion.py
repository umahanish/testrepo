import re

import requests

master_version_file = 'taskcat/master_version'
develop_version_file = 'taskcat/develop_version'

def get_pip_version(pkginfo_url):
    pkginfo = requests.get(pkginfo_url).text
    for record in pkginfo.split('\n'):
        if record.startswith('Version'):
            current_version = str(record).split(':', 1)
            return (current_version[1]).strip()


#current_develop_version = get_pip_version('https://testpypi.python.org/pypi?name=taskcat&:action=display_pkginfo')
current_develop_version = '0.dev373.dev3'
print("PyPi Develop Version is [{}]".format(current_develop_version))
#current_master_version = get_pip_version('https://pypi.python.org/pypi?name=taskcat&:action=display_pkginfo')
current_master_version =  '730.73.73'
print("PyPi Master Version is [{}]".format(current_master_version))

new_poduction_release = int(re.findall(r'\d+', current_master_version)[-1])
new_development_release = int(re.findall(r'\d+', current_develop_version)[-1])

production_version =re.sub('\d$', lambda x: str(int(x.group(0)) + 1), current_master_version)
development_version =re.sub('\d$', lambda x: str(int(x.group(0)) + 1), current_develop_version)

print("current_develop_version")
print(development_version)
print("current_master_version")
print(production_version)

with open(master_version_file, 'w') as m:
    m.write(str(current_master_version))

with open(develop_version_file, 'w') as d:
    d.write(str(current_develop_version))