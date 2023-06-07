import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from functools import lru_cache
data = json.loads(open("/home/sigma/Downloads/nfL6.json", "r").read())
train = []
#for k, row in enumerate(data):
#    train.append(row['question'])
#    train.append(row['answer'])
#    if k > 35000:
#        break
chatbot = ChatBot('QA')
#trainer = ListTrainer(chatbot)
#trainer.train(train)
while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)
    