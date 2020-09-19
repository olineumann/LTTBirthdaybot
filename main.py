#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Birthday bot to send the birthday child on a journey with exciting quests.
"""

import logging
import datetime as dt

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import requests
from bs4 import BeautifulSoup

from data import *


def start(update, context):
    """Start the birthday journey with /start."""
    update.message.reply_text(replies['on_start'])
    if journey_started() or (context.user_data and 'force' in context.user_data):
        context.user_data['state'] = 0
        update.message.reply_text(replies['first_quest'])
        update.message.reply_text(questions[context.user_data['state']])
    else:
        update.message.reply_text(replies['journey_not_started'])
        update.message.reply_text(random_wisdom())


def help_command(update, context):
    """Explain the use of the telegram birthday bot with /help."""
    update.message.reply_text(replies['help'])
    update.message.reply_text(random_wisdom())


def hint_command(update, context):
    """Give a hint for the quest if needed with /hint."""
    if context.user_data and 'state' in context.user_data:
        if context.user_data['state'] >= len(questions):
            update.message.reply_text(replies['no_quests_left'])
            update.message.reply_text(random_wisdom())
        else:
            update.message.reply_text(hints[context.user_data['state']])
    else:
        update.message.reply_text(replies['no_context'])


def quest_command(update, context):
    """Resend the quest with /quest."""
    if context.user_data and 'state' in context.user_data:
        if context.user_data['state'] >= len(questions):
            update.message.reply_text(replies['no_quests_left'])
            update.message.reply_text(random_wisdom())
        else:
            update.message.reply_text(questions[context.user_data['state']])
    else:
        update.message.reply_text(replies['no_context'])


def force_command(update, context):
    """Overwrite the start_date checking with /force."""
    update.message.reply_text(replies['force_starting'])
    context.user_data['force'] = True


def solve_command(update, context):
    """Solve the question by giving the answer and sending the next question (/solve)."""
    if context.user_data and 'state' in context.user_data:
        if context.user_data['state'] >= len(questions):
            update.message.reply_text(replies['no_quests_left'])
            update.message.reply_text(random_wisdom())
        else:
            update.message.reply_text(replies['wants_solve'])
            update.message.reply_text(answers[context.user_data['state']])
            if explanations[context.user_data['state']] != '':
                update.message.reply_text(explanations[context.user_data['state']])
            context.user_data['state'] += 1
    else:
        update.message.reply_text(replies['no_context'])


def respond(update, context):
    """Respond to users input."""
    if context.user_data and 'state' in context.user_data:
        if context.user_data['state'] >= len(questions):
            update.message.reply_text(replies[''])
        elif update.message.text.lower() == answers[context.user_data['state']]:
            update.message.reply_text(replies['right'])
            if explanations[context.user_data['state']] != '':
                update.message.reply_text(explanations[context.user_data['state']])
            context.user_data['state'] += 1 
            if context.user_data['state'] >= len(questions):
                update.message.reply_text(replies['no_quests_left'])
            else:
                update.message.reply_text(replies['next_quest'])
                update.message.reply_text(questions[context.user_data['state']])
        else:
            update.message.reply_text(replies['wrong'])
            update.message.reply_text(random_wisdom())
    else:
        update.message.reply_text(replies['no_context'])
        update.message.reply_text(random_wisdom())


def random_wisdom():
    """Returning some random wisdom as string."""
    page = requests.get('http://sprichwortgenerator.de/')
    soup = BeautifulSoup(page.content, 'html.parser')
    wisdom = soup.findAll('div', {'class': 'spwort'})[0]
    return wisdom.encode_contents().decode("utf-8")


def journey_started(date=dt.datetime.now()):
    """Checking if the journey has started."""
    seconds_left = (date - start_date).total_seconds()
    return seconds_left > 0


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
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('hint', hint_command))
    dp.add_handler(CommandHandler('quest', quest_command))
    dp.add_handler(CommandHandler('force', force_command))
    dp.add_handler(CommandHandler('solve', solve_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
