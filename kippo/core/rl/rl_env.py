from pybrain.rl.environments.environment import Environment
from scipy import zeros
from utils import *

class HASSHEnv(Environment):
    
    indim = 3
    
    outdim = 2
    
    def getSensors(self):
        val = getCurrentCommand()
        return [val,]
    
    def performAction(self, action):
        doAction(action)
        print "Action performed: ", action
    
    def reset(self):
        pass

