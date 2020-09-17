#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Challenge
questions = [
    'What is 1 + 2 * 3?',
    'What color gives blue and red together?'
]

answer = [
    '7',
    'purple'
]


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    context.user_data['state'] = 0
    update.message.reply_text('Hello traveler! Welcome to the journey bla bla. Your first question is the following:')
    update.message.reply_text(questions[context.user_data['state']])


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('This is an exciting text adventure! Type /quest to get your current quest.')


def quest_command(update, context):
    """Send a message when the command /help is issued."""
    if not context.user_data:
        update.message.reply_text('Please start the journey by typing /start.')
    elif context.user_data['state'] >= len(questions):
        update.message.reply_text('Sadly there is no quest left. You can restart the journey by typing /start.')
    else:
        update.message.reply_text(questions[context.user_data['state']])


def echo(update, context):
    """Echo the user message."""
    if context.user_data and 'state' in context.user_data:
        if context.user_data['state'] >= len(questions):
            update.message.reply_text('Sadly there is no quest left. You can restart the journey by typing /start.')
            return
        if update.message.text.lower() == answer[context.user_data['state']]:
            update.message.reply_text('Congratulation traveler! That is the correct answer.')
            context.user_data['state'] += 1 
            if context.user_data['state'] >= len(questions):
                update.message.reply_text('Sadly that was the last quest.')
            else:
                update.message.reply_text('Your next quest is directly following:')
                update.message.reply_text(questions[context.user_data['state']])
        else:
            update.message.reply_text('No! Random Wisdom.')
    else:
        update.message.reply_text('Hello traveler! Type /start to start your journey.')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    with open('telegram.key', 'r') as file:
        token = file.read()
        updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("quest", quest_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()