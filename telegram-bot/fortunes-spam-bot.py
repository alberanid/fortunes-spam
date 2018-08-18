#!/usr/bin/env python3
"""Telegram bot for fortunes-spam.

Build it with: docker build -t fortunes-spam-bot .
Run it with something like: docker run -ti --rm -e SPAMBOT_TOKEN=your-telegram-token fortunes-spam-bot

Copyright 2018 Davide Alberani <da@erlug.linux.it> Apache 2.0 license
"""

import os
import logging
import subprocess
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def getSpam(section):
    cmd = ['fortune', '-o', section]
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


def serve(section, bot, update):
    spam = getSpam(section)
    logging.info('%s wants some spam; serving:\n%s' % (update.message.from_user.name, spam))
    update.message.reply_text(spam)


def en(bot, update):
    return serve('spam-o', bot, update)


def it(bot, update):
    return serve('spam-ita-o', bot, update)


def about(bot, update):
    logging.info('%s required more info' % update.message.from_user.name)
    update.message.reply_text('See https://github.com/alberanid/fortunes-spam')


if __name__ == '__main__':
    if 'SPAMBOT_TOKEN' not in os.environ:
        print("Please specify the Telegram token in the SPAMBOT_TOKEN environment variable")
    logging.info('start serving delicious spam')
    updater = Updater(os.environ['SPAMBOT_TOKEN'])
    updater.dispatcher.add_handler(CommandHandler('en', en))
    updater.dispatcher.add_handler(CommandHandler('it', it))
    updater.dispatcher.add_handler(CommandHandler('about', about))
    updater.start_polling()
    updater.idle()
