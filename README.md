# Git2FGPlane
An easy way to keep your GitHub aircraft always updated.

## Requirements

### Windows, Linux or MAC OS PC.
Only tested on windows.=

### Git 1.7.x or newer installed already / NOT PORTABLE VERSION (for now)!
https://git-scm.com/

### Python 3+
https://www.python.org/

### GitDB Python Package installed already.
https://pypi.python.org/pypi/gitdb

## Files Explanations

### Git2FGPlaneCfg.txt
File used to store all registered aircraft git URL. You need edit this manually

e.g file content:

```
https://github.com/RenanMsV/FGHolding.git
https://github.com/RenanMsV/FGsX.git
https://github.com/RenanMsV/BRFGPassengers.git
https://github.com/FGMEMBERS/EMB-121.git
https://github.com/YV3399/737-800YV.git
https://github.com/it0uchpods/A320Family.git
https://github.com/it0uchpods/727-200.git
https://github.com/FGMEMBERS/aw139.git
https://github.com/FGMEMBERS/R44.git
https://github.com/FGMEMBERS/R22.git
```

Then all that planes will be maintained updated.

### Git2FGPlane.py
Python file witch you runs to execute the tool.

### locales/* path. 
Translations files. Not yet implemented.

### git/* path.
GitPython files. Used for python git integration.

## Usage

* Open Git2FGPlaneCfg.txt and add/remove aircraft URL. One URL per line.
* Save it.
* Open Git2FGPlaneCfg.py and wait until your registered aircrafts gets updated.
* When it finishs updating will appear a confirmation message, just press ENTER on it to close Git2FGPlaneCfg.py
* Now all your updated aircraft should be located in "C:\Git2FGPlane\DownloadedAircrafts\DEVELOPERNAME\Aircraft\AIRCRAFTNAME" like "C:\Git2FGPlane\DownloadedAircrafts\FGMEMBERS\Aircraft\R22"
* Open FGFS Launcher.
* Go to Addons > Additional Aircraft Locations > + and add your Developer Aircraft path. Like C:\Git2FGPlane\DownloadedAircrafts\DEVELOPERNAME\Aircraft
* Then now you have all planes from this DEVELOPER in your launcher.
* Choose one aircraft and have a nice flight.

##### You'll need run Git2FGPlane.py when you need to update your aircrafts. It'll not runs by itself.
##### Git2FGPlane will update all aircrafts, so this process can take a long time.
##### Git2FGPlane will sometimes (if you try to change aircraft files) get an error and close. So you'll need undo this changes until continue updating others aircrafts.
##### Git2FGPlane do not allow file changes (add textures, sounds, fixes)... cause it maintain all aircrafts updated and try to delete local changes.
##### Git2FGPlane can be unstable.


## Versions

#### v0.1
Initial uploading.

## RoadMap

Request update confirmation per aircraft.

Graphical User Interface.

Code cleanup.
