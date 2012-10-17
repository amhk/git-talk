import os
from pyinotify import WatchManager, Notifier, EventsCodes, ProcessEvent, ThreadedNotifier
import pyinotify
import threading
import pygame

def do_post():
	pygame.event.post(pygame.event.Event(pygame.USEREVENT, dict()))

def start_watching():
	class OnEvent(ProcessEvent):
		def __init__(self):
			ProcessEvent(self)
			self.timer = None

		def process_default(self, event):
			accepted = [pyinotify.IN_MODIFY, pyinotify.IN_MOVE_SELF, pyinotify.IN_MOVED_FROM, pyinotify.IN_MOVED_TO]
			x = [x for x in accepted if event.mask & x == event.mask]
			if len(x) > 0:
				print "default: %-20s %s" % (os.path.join(event.path, event.name), event.maskname)
				if self.timer:
					self.timer.cancel()
					self.timer = None
				self.timer = threading.Timer(0.2, do_post)
				self.timer.start()

	wm = WatchManager()
	mask = pyinotify.ALL_EVENTS
	proc = OnEvent()
	notifier = ThreadedNotifier(wm, proc)
	notifier.start()
	wdd = wm.add_watch('.git', mask, rec=True, auto_add=True)
