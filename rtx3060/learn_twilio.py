from twilio.rest import Client
from passwords import twilio_auth_token, twilio_account_sid

# Your Account SID from twilio.com/console
account_sid = twilio_account_sid
# Your Auth Token from twilio.com/console
auth_token  = twilio_auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18312772449", 
    from_="+12564884788",
    body="Hello from Python!")

print(message.sid)