import vonage
from dotenv import load_dotenv
import os
load_dotenv()
APIKEY = os.getenv("key")
APISECRET = os.getenv("secret")
print(APIKEY, APISECRET)
client = vonage.Client(key=APIKEY, secret=APISECRET)
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "ANY NAME",
        "to": "ANY NUMBER",
        "text": "DO NOT FORGET THE EVALUATION",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(
        f"Message failed with error: {responseData['messages'][0]['error-text']}")
