from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.storage import storage_adapter
import logging

bot = None

class GoChatBot:
    def GetAnswer(self,message):
        lerey = ChatBot(
            "Go Transa",
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            database='gotransa',
            database_uri='mongodb://192.241.245.34:27017/',
            logic_adapters=[
                "chatterbot.logic.MathematicalEvaluation",
                "chatterbot.logic.TimeLogicAdapter",
                "chatterbot.logic.BestMatch"
            ]
        )
        return lerey.get_response(message)