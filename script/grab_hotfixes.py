#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Borderlands 3 Hotfix Monitor (grab_hotfixes.py)
# Copyright (C) 2019 CJ Kucera
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import git
import json
import appdirs
import requests
import datetime

hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/epic/pc/oak/verification'
output_dir = '/home/pez/git/b2patching/bl3hotfixes'
point_in_time_base = 'point_in_time'
point_in_time_dir = os.path.join(output_dir, point_in_time_base)
cumulative_file = 'hotfixes_current.json'

# Get our cache dir, and create if it doesn't exist
cache_dir = appdirs.user_cache_dir('bl3hotfixes', 'Apocalyptech')
if not os.path.isdir(cache_dir):
    os.makedirs(cache_dir)
if not os.path.isdir(cache_dir):
    raise Exception('Couldn\'t create cache dir: {}'.format(cache_dir))

# Get our current hotfix data, if we can
hotfix_cache = os.path.join(cache_dir, 'hotfixes.json')
cur_hotfixes = None
if os.path.exists(hotfix_cache):
    with open(hotfix_cache) as df:
        cur_hotfixes = df.read()

# Grab hotfixes (and other data) from server
r = requests.get(hotfix_url)
verification = json.loads(r.text)

# Loop through to find 'Micropatch', which is the one we want
hotfixes_new = None
for service in verification['services']:
    if service['service_name'] == 'Micropatch':
        hotfixes_new = service
        break

# If we didn't get hotfixes, error.
if not hotfixes_new:
    raise Exception('Could not find hotfixes!')

# Format them
hotfixes = json.dumps(hotfixes_new, indent='  ')

# Check to see if we need to write out a new hotfix file
do_write = False
if cur_hotfixes:
    if hotfixes != cur_hotfixes:
        #print('Hotfixes have changed')
        do_write = True
    else:
        #print('Hotfixes are unchanged')
        pass
else:
    #print('No original hotfixes')
    do_write = True

# Do the write, if we have to
if do_write:

    # First write the new file to the cache
    print('Writing new hotfix cache to {}'.format(hotfix_cache))
    with open(hotfix_cache, 'w') as df:
        df.write(hotfixes)

    # Now also write out the hotfixes to a new repo file
    now = datetime.datetime.utcnow()
    hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
    print('Writing new hotfixes to {}'.format(hotfix_filename))
    with open(os.path.join(point_in_time_dir, hotfix_filename), 'w') as df:
        df.write(hotfixes)

    # Now write to our cumulative file
    print('Writing new hotfixes to {}'.format(cumulative_file))
    with open(os.path.join(output_dir, cumulative_file), 'w') as df:
        df.write(hotfixes)

    # Do the git interaction
    print('Pushing to git')
    repo = git.Repo(output_dir)
    repo.git.pull()
    repo.git.add('--', os.path.join(point_in_time_base, hotfix_filename))
    repo.git.add('--', cumulative_file)
    repo.git.commit('-a', '-m', now.strftime('Auto-update with new hotfixes - %Y-%m-%d %H:%M:%S'))
    repo.git.push()
