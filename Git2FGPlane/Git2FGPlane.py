# -*- coding: utf-8 -*-

#import os
#from sys import platform as _platform
#from time import sleep
from git import *

class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print('Downloading: (==== {} ====)'.format(message), end='\r')

def getOut(msg):
    input('{}. Press ENTER to close'.format(msg))
    exit()

try:
    lines = open('Git2FGPlaneCfg.txt', 'r').read().splitlines()
except:
    getOut('Error: Configuration file not found. Or no read level.\n')
print('Configuration file found...Starting...\n\nRegistered aircrafts:')
if not lines :
    getOut("\nNone registered aircraft was found.")
for link in lines :
    print(link)
print("\n")
i = 1
for link in lines:
    print('Updating {} | {} of {} : '.format(link,i, len(lines)))
    PATH_NAME = "DownloadedAircrafts/{}/Aircraft/{}".format(link.split('.com/')[1].split('/')[0],link.split('.com/')[1].split('/')[1].replace('.git',''))
    try :
        IS_GIT = True  if Repo(PATH_NAME).git_dir else False
    except :
        IS_GIT = False
    if not IS_GIT:
        prog = Progress()
        Repo.clone_from("git://github.com/{}".format(link.split('.com/')[1]), PATH_NAME, progress=Progress())
    else:
        g = Repo(PATH_NAME)
        g.git.reset('--hard')
        origin = g.remotes.origin
        origin.pull(progress=Progress())
    i=i+1
getOut("\nUpdates finished")

if _platform == "linux" or _platform == "linux2":
    # linux
    print()
elif _platform == "darwin":
    # MAC OS X
    print()
    #os.chdir("/Applications/FlightGear.app/Contents/Resources")
elif _platform == "win32":
    # Windows
    print()
os.system('git-cmd git clone git://github.com/{} PASTA'.format(result))