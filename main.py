from rtmbot import RtmBot
from rtmbot.core import Plugin
import random
from secret import SLACK_TOKEN

class HelloPlugin(Plugin):
    def process_message(self, data):
        results = [' 🐕 간다 ', '왜 ❓', '🐶 🗯 🗯 🗯' , '나 고양인데? 🐱' ]

        if "댕댕" in data["text"]:
            num = random.randrange(0,3)
            self.outputs.append([data["channel"], results[num]])

config = {
    "SLACK_TOKEN": SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()


print("As soon as I have got flying to perfection, I have got a scheme about a steam engine.")
print("Let's eat Dinner!")
print("This is a Quotesbot.")
