#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from mastodon import Mastodon

API_URL = 'https://botsin.space/'


def getSpam(sections=('spam-o', 'spam-ita-o')):
    cmd = ['fortune', '-o', *sections]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    try:
        stdout = stdout.strip()
        stdout = stdout.decode('utf8')
    except:
        return 'uh-oh: something was wrong with the encoding of the can\'s label; try again'
    if process.returncode != 0:
        return 'something terrible is happening: exit code: %s, stderr: %s' % (
                process.returncode, stderr.decode('utf8'))
    if not stdout:
        return 'sadness: the spam can was empty; try again'
    return stdout


def serve(token):
    spam = getSpam()
    print('serving:\n%s' % spam)
    mastodon = Mastodon(access_token=token, api_base_url=API_URL)
    mastodon.status_post(spam, sensitive=True, spoiler_text='NSFW')


if __name__ == '__main__':
    if 'SPAMBOT_TOKEN' not in os.environ:
        print("Please specify the Mastodon token in the SPAMBOT_TOKEN environment variable")
        sys.exit(1)
    serve(token=os.environ['SPAMBOT_TOKEN'])
