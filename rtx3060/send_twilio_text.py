from twilio.rest import Client
from passwords import twilio_auth_token, twilio_account_sid


def send_text(message, receiving_number):
    """ send text message to a phone number """

    # Your Account SID from twilio.com/console
    account_sid = twilio_account_sid
    # Your Auth Token from twilio.com/console
    auth_token  = twilio_auth_token

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=receiving_number, 
        from_="+12564884788",
        body=message)

    print(message.sid)