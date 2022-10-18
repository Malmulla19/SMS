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
        "from": "Any Name",
        "to": "AnyNumber",
        "text": "DO NOT FORGET THE EVALUATION",
    }
)
try:
    response = responseData["messages"][0]
    if response["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response['error-text']}")
except Exception as e:
    print(f"Message failed with error: {e}")