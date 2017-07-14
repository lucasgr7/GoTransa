import sys
from gochatbot import GoChatBot
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

goChatBot = GoChatBot()

print("Gotransa is begin..")
print(goChatBot.GetAnswer("oi"))

# # The following loop will execute each time the user enters input
# while True:
#     try:
#         # We pass None to this method because the parameter
#         # is not used by the TerminalAdapter
#         bot_input = bot.get_response(None)

#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break