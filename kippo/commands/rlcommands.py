# Copyright (c) 2009 Upi Tamminen <desaster@gmail.com>
# See the COPYRIGHT file for more information

# Commands mapped to common malware

from kippo.core.honeypot import HoneyPotCommand
from kippo.dblog.kipporl import *
import os

commands = {}

class command_pr(HoneyPotCommand):
    def call(self):
	cmd = " ".join([self.honeypot.cmd] + list(self.args))
	path = "/tmp/root/"+self.honeypot.cwd
	ret = os.popen("cd %s; %s" % (path, cmd)).read()
	if ret and ret[-1] != "\n":
	    ret = ret + "\n"
	self.write(ret)

class command_fake(HoneyPotCommand):
    def call(self):
	ret = getDB().getFakeCommand(self.honeypot.cmd)
	if ret and ret[-1] != "\n":
	    ret = ret + "\n"
	self.write(ret)

commands['lsp'] = command_pr
commands["cpp"] = command_pr
commands["catp"] = command_pr

