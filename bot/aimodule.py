import aiml
from os import listdir
from os.path import dirname, isfile
import cbot

#kernel = aiml.Kernel()

path = dirname(__file__) + "/libs"
brain_path = dirname(__file__) +"/bot_brain.brn"

def train():
    #if isfile(brain_path):
    #    kernel.bootstrap(brainFile = "bot_brain.brn")
    #else:
    #    aimls = listdir(aiml_path)
    #    for aiml in aimls:
    #        kernel.bootstrap(learnFiles=aiml_path + "/" + aiml)
    #    kernel.saveBrain("bot_brain.brn")
    cbot.train()


def record():
    print (kernel.getSessionData())

def respond(msg):
    #return kernel.respond(msg)
    return cbot.respond(msg)

def incident():
    return kernel.getSessionData()
