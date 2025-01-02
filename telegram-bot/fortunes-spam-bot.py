#!/usr/bin/env python3
"""Telegram bot for fortunes-spam.

Build it with: docker build -t fortunes-spam-bot .
Run it with something like: docker run -ti --rm -e SPAMBOT_TOKEN=your-telegram-token fortunes-spam-bot

Copyright 2018-2025 Davide Alberani <da@mimante.net> Apache 2.0 license
"""

import os
import logging
import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

EXTERNAL_VOL = '/fortunes'

def getSpam(section):
    extPath = os.path.join(EXTERNAL_VOL, section)
    if os.path.isfile(extPath):
        section = extPath
    cmd = ['fortune', '-o', section]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    try:
        stdout = stdout.strip()
        stdout = stdout.decode('utf8')
    except Exception:
        return 'uh-oh: something was wrong with the encoding of the can\'s label; try again'
    if process.returncode != 0:
        return 'something terrible is happening: exit code: %s, stderr: %s' % (
                process.returncode, stderr.decode('utf8'))
    if not stdout:
        return 'sadness: the spam can was empty; try again'
    return stdout


async def serve(section, update, context):
    spam = getSpam(section)
    logging.info('%s wants some spam; serving:\n%s' % (update.effective_user.username, spam))
    await update.message.reply_text(spam)


def en(update, context):
    return serve('spam-o', update, context)


def it(update, context):
    return serve('spam-ita-o', update, context)


async def about(update, context):
    logging.info('%s required more info' % update.effective_user.username)
    await update.message.reply_text('See https://github.com/alberanid/fortunes-spam')


if __name__ == '__main__':
    if 'SPAMBOT_TOKEN' not in os.environ:
        print("Please specify the Telegram token in the SPAMBOT_TOKEN environment variable")
    logging.info('start serving delicious spam')
    application = Application.builder().token(os.environ['SPAMBOT_TOKEN']).build()
    application.add_handler(CommandHandler('en', en))
    application.add_handler(CommandHandler('it', it))
    application.add_handler(CommandHandler('about', about))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
