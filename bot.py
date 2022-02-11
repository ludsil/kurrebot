from email import message
from lib2to3.pgen2 import token
from aiohttp import payload
import os
from pathlib import Path
import os
#external
from flask import Flask
from slackeventsapi import SlackEventAdapter
import slack #slackclient
import gspread
from dotenv import load_dotenv
#egna
from sheets import create_kurrebet, add_participant


app = Flask(__name__)

load_dotenv()

# .env fil
slack_token = os.getenv("SLACK_TOKEN")
slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")

slack_event_adapter = SlackEventAdapter(slack_signing_secret, '/slack/events', app) # signing secret, route, webserver

client = slack.WebClient(token=slack_token)
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def on_message(payLoad):
  event = payLoad.get('event', {})
  channel_id = event.get('channel')
  user_id = event.get('user')
  text = event.get('text')
  print(text)
  if text == 'hjälp':
    post_help()
  elif user_id != BOT_ID:
    create_kurrebet(text)
    
@slack_event_adapter.on('reaction_added')
def on_reaction_added(payLoad):
  
  ####### unit tests 🤡 ######
  # print(payLoad)
  # print(payLoad.get('event').get('reaction'))
  # print(payLoad.get('event').get('user'))
  # print(get_display_name('U02VASQHK2A'))
  # print(client.users_profile_get(user='U02VASQHK2A'))
  
  reacting_user = get_display_name(payLoad.get('event').get('user'))
  conversation_id = payLoad.get('event').get('item').get('channel')
  message_timestamp = payLoad.get('event').get('item').get('ts')
  
  specific_bet = client.conversations_history(channel = conversation_id, latest = message_timestamp, limit = 1, inclusive = True)
  bet_text = specific_bet.get('messages')[0].get('text')
  # print(bet_text)
  bet_title = " ".join(bet_text.split('\n')[0].split()[:-1])
  
  if payLoad.get('event').get('reaction') == 'white_check_mark':
    add_participant(reacting_user, bet_title, 5)

  if payLoad.get('event').get('reaction') == 'x':
    add_participant(reacting_user, bet_title, 6)

def get_display_name(userId):
  profileinfo = client.users_profile_get(user=userId)
  return profileinfo.get('profile').get('display_name')

def invalid_format(bet_text):
  invalid = False
  bet_text = bet_text.split('\n')
  if len(bet_text[0].split()) < 2 or len(bet_text) != 2:
    invalid = True
    print('1')
  try:
    int(bet_text[0].split()[-1])
  except:
    print('2')
    invalid = True
  if invalid:
    client.chat_postMessage(channel='#general', text="Fel format!")
  return invalid

def post_help():
  client.chat_postMessage(channel='#general', text="du får hjälp")

if __name__ == "__main__":
  app.run(debug=True) # Kan välja port här på något sätt