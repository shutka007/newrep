#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
from os import getenv

import aiohttp
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
from telebot import types
from telebot.async_telebot import AsyncTeleBot
load_dotenv()

bot = AsyncTeleBot(getenv('TOKEN'))


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    async  with aiohttp.ClientSession() as session:
        api_url = 'https://thecatapi.com/v1/images/search'
        headers = {'x-api-key': getenv('API_KEY')}


asyncio.run(bot.polling())