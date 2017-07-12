from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.storage import storage_adapter
import logging
bot = ChatBot(
    "Go Transa",
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    database='./database.json',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database_name="C:/Users/Lucas/estudos/chatter bot/database.sqlite3"
)

conversation = [
    "Ola",
    "Oi!",
    "Como voce esta?",
    "Eu estou bem.",
    "isso e bom ouvir",
    "Obrigado.",
    "voce e bem vindo.",
    "Bom dia",
    "E ai?",
    "Bom dia",
    "Buenos dias!",
    "Bom dia",
    "E ai fera?",
    "Bom dia",
    "E ai fera"
]

bot.set_trainer(ListTrainer)
bot.train(conversation)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break