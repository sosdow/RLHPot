from kippo.core.constants import *
import kippo
import time

def getCommandReward(command):
    l = ["wget", "scp", "ftp", "mount", "echo", "rm", "tar", "whoami", "cat"]
    for c in l:
        if c in command:
            return 1
        if command.startswith("./"):
            return 1
        l2 = ["python", "php", "sh", "bash"]
        for c in l2:
            if command.startswith(c):
                return 1
    return 0

def getCommandType(command):
    l = ["wget", "scp", "ftp", "mount", "echo", "rm", "tar", "whoami", "cat"]
    for c in l:
        if c in command:
            return 1
        if command.startswith("./"):
            return 1
        l2 = ["python", "php", "sh", "bash"]
        for c in l2:
            if command.startswith(c):
                return 1
    return 0

def getCurrentCommand():
    #global current_command
    #global current_reward
    #global prev_command
    while True:
	print "get current command -============================", kippo.core.constants.current_command
	if not kippo.core.constants.current_command:
	    time.sleep(1)
	else:
	    kippo.core.constants.prev_command = kippo.core.constants.current_command
	    kippo.core.constants.current_command = None
	    kippo.core.constants.current_reward = getCommandReward(kippo.core.constants.prev_command)
	    return getCommandType(kippo.core.constants.prev_command)

def getCurrentReward():
    return kippo.core.constants.current_reward

def doAction(action):
    print "do action ==================================="
    kippo.core.constants.rl_action = action
