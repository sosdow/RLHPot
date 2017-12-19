import kippo
from kippo.core import dblog
from kippo.core.config import *
from twisted.enterprise import adbapi
from twisted.internet import defer
from twisted.python import log
from kippo.core.constants import *
import MySQLdb, uuid
from mysql import *
import MySQLdb.cursors

class DB:

    def __init__(self, cfg):
        if cfg.has_option('database_mysql', 'port'):
            port = int(cfg.get('database_mysql', 'port'))
        else:
            port = 3306
        host = cfg.get('database_mysql', 'host')
        db = cfg.get('database_mysql', 'database')
        user = cfg.get('database_mysql', 'username')
        passwd = cfg.get('database_mysql', 'password')
	self.con = MySQLdb.connect(host=host,  user=user, passwd=passwd,  db=db, port=port, cursorclass=MySQLdb.cursors.DictCursor) 

    
    def get_commands(self):
	cur=self.con.cursor()
	cur.execute("SELECT * from commands")
	return cur
    
    def getFakeCommand(self, cmd):
	cur=self.con.cursor()
	cur.execute("SELECT * from fake_commands where command=%s", (cmd, ))
	for i in cur:
	    return i["fake_output"]
	return "Fake command not found\n"
    
    def saveCase(self, case):
        print "case is saving", kippo.core.constants.rl_params
	cur=self.con.cursor()
	cmd = case["initial_cmd"]
	cur.execute("insert into cases(initial_cmd, action, next_cmd, cmd_profile, rl_params) values(%s, %s, %s, %s, %s)", (case["initial_cmd"], case["action"], case["next_cmd"], self.getProfile(cmd), str(kippo.core.constants.rl_params) ))
	self.con.commit();
    
    def getProfile(self, cmd):
	cur=self.con.cursor()
	cur.execute("SELECT prof_type from commands where command=%s", (cmd, ))
	for i in cur:
	    return i["prof_type"]
	return ""

    def getInsultMsg(self, loc):
	cur=self.con.cursor()
	cur.execute("SELECT message from messages  where country=%s", (loc, ))
	for i in cur:
	    return i["message"].strip()+"\n"
	cur=self.con.cursor()
	cur.execute("SELECT message from messages  where country=%s", ('DEFAULT', ))
	for i in cur:
	    return i["message"].strip()+"\n"

    def getCases(self):
        cur=self.con.cursor()
	cur.execute("SELECT * from cases order by id")
	return cur

db = None
def getDB():
    global db
    if db is None:
	db = DB(config())
    return db
