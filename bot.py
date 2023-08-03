from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot(
                "Chatbot", #Name of the chatbot
               # storage_adapter='chatterbot.storage.SQLStorageAdapter',
               preprocessors = [
                   "chatterbot.preprocessors.clean_whitespace"
               ],
                logic_adapters = [  #Logic adapters determine the logic for how Chatterbot selects a response to a statement
                    "chatterbot.logic.BestMatch",
                    #"chatterbot.logic.TimeLogicAdapter",
                    #"chatterbot.logic.MathematicalEvaluation",
                    #"chatterbot.logic.UnitConversion"
                ]
            )

# We can train the chatbot from any given list of strings
'''
trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend😁",
])
trainer.train([
    "Are you a star?",
    "No, I'm the guy next to the star!",
])
'''

#Or we can train it on several collections of pre cleaned data available with the chatbot library
big_trainer = ChatterBotCorpusTrainer(chatbot)
big_trainer.train('chatterbot.corpus.english')

exit_conditions = (":q", "quit", "exit")

#Build a custom preprocessor to process input to be standardized
#Remove whitespace, capitalize the first letter,


#This is the UI interface and execution loop
while True:
    query = input("> ")
    if query in exit_conditions: break
    else: 
        print(f"😵‍💫{chatbot.get_response(query)}")
        # Access confidence level of BestMatch logic adapter
        best_match_confidence = chatbot.logic_adapters[0].maximum_similarity_threshold
        #print(f"Confidence of BestMatch logic adapter: {best_match_confidence}")