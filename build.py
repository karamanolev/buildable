#!/usr/bin/env python
import sys
import requests

project = 1
build = sys.argv[1]
commit_sha = sys.argv[2]
print('Create build...')
r = requests.post(
    'http://localhost:8002/api/v1/projects/{}/builds/'.format(project),
    json={
        'build_number': build,
        'commit_hash': commit_sha,
    },
)
r.raise_for_status()

print('Taking screenshot...')
import time
time.sleep(2)
print('Uploading screenshot...')
r = requests.put(
    'http://localhost:8002/api/v1/projects/{}/builds/{}/screenshots/{}'.format(
        project, build, 'eagle.png'),
    files={'image': open('eagle.png', 'rb')},
)
r.raise_for_status()
r = requests.put(
    'http://localhost:8002/api/v1/projects/{}/builds/{}/screenshots/{}'.format(
        project, build, 'tux.png'),
    files={'image': open('tux.png', 'rb')},
)
r.raise_for_status()

print(r.text)

print('Finishing build...')
r = requests.post(
    'http://localhost:8002/api/v1/projects/{}/builds/{}/finish'.format(project, build),
)
r.raise_for_status()
