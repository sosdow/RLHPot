import sys
sys.path.append("../")

import kippo
from zope.interface import implements

from kippo.core import ttylog, fs, utils
from kippo.core.userdb import UserDB
from kippo.core.config import config
from kippo.dblog.kippo_mysql import *
import commands
import ConfigParser
from kippo.core.config import *
from kippo.core.constants import *



for row in getDB().getCases():
    if row["rl_params"] != "" and row["rl_params"] is not None:
        l = row["rl_params"].replace("[", "").replace("]", "")
        l = l.strip().split()
        print ",".join(l)



