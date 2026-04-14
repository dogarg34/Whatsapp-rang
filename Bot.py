import requests
import time
from telegram import Bot

TOKEN = "8031556197:AAESU6rd6mK6klIIJDkN3lqpmHJvZndojWs"
CHAT_ID = "-1003959502340"

bot = Bot(token=TOKEN)

url = "http://51.77.216.195/crapi/lamix/viewstats"

sent = set()  # duplicate avoid

while True:
    try:
        res = requests.get(url)
        data = res.json()

        for item in data["data"]:
            num = item["num"]
            msg = item["message"]
            cli = item.get("cli", "")

            # ✅ Sirf WhatsApp filter
            if "whatsapp" in msg.lower() or cli.lower() == "whatsapp":

                unique_id = item["dt"] + num
                if unique_id not in sent:
                    sent.add(unique_id)

                    text = f"""
📲 WhatsApp OTP

📱 Number: {num}
💬 Message: {msg}
                    """

                    bot.send_message(chat_id=CHAT_ID, text=text)

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
