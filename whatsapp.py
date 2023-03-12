import os

from dotenv import load_dotenv
from flask import Flask, request
from twilio.rest import Client

from chat import chat

load_dotenv()
app = Flask(__name__)

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
from_number = os.environ.get('FROM_NUMBER')
to_number = os.environ.get('TO_NUMBER')

client = Client(account_sid, auth_token)
messages = []


@app.route('/', methods=['GET', 'POST'])
def whatsapp():
    last_message = request.form['Body']
    messages.append(
        {"role": "user", "content": last_message})
    response = chat(messages)

    client.messages.create(
        from_=f'whatsapp:{from_number}',
        body=response.choices[0].message.content,
        to=f'whatsapp:{to_number}'
    )
    return '200'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
