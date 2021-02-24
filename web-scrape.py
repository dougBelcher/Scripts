# Twitch Web Scrape test
import requests
from twilio.rest import Client

# Twilio account info
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

endpoint = "https://api.twitch.tv/helix/streams?"
# Twitch account info
headers = {"Client-ID": "mfune8cyhzg8habvk93a7ja641tlxg"}
# Twitch profile and password
params = {"dougBelcher": ""}

response = requests.get(endpoint, params=params, headers=headers)
json_response = response.json()
streams = json_response.get('data', [])
is_active = lambda stream:stream.get('type') == 'live'
streams_active = filter(is_active, streams)
at_least_one_stream_active = any(streams_active)

last_messages_sent = client.messages.list(limit=1)
if last_messages_sent:
    last_message_id = last_messages_sent[0].sid
    last_message_data = client.messages(last_message_id).fetch()
    last_message_content = last_message_data.body
    online_notified = "LIVE" in last_message_content
    offline_notified = not online_notified
else:
	online_notified, offline_notified = False, False

if at_least_one_stream_active and not online_notified:
	client.messages.create(body='LIVE !!!',from_=5012146339,to=3147664461)
if not at_least_one_stream_active and not offline_notified:
	client.messages.create(body='OFFLINE !!!',from_=5012146339,to=3147664461)