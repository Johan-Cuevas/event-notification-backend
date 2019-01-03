from twilio.rest import Client # imports client from twilio


account_sid = 'ACxxxxxxxxxxxxx' # account tokens
auth_token = 'xxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

a = ['+1xxxxxxxx', '+1xxxxxxxx'] # list of numbers to send message to

for i in a:
    print(i)
    client.messages.create(from_= 'Twilio number',
                                 body = "Message goes here",
                                 to = i)
