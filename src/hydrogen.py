"""
name: HML
author: https://github.com/commander07
description: Hydrogen Mod Loader (HML) is a modding framework for python games. That has features such as events, override and more!
"""
import atexit
import sys
from .__config__ import events as __events__
class GLOBAL: pass


class events(__events__):
  OnEnable = __events__.Event("OnEnable")
  OnDisable = __events__.Event("OnDisable")


class EventHandler:
  def __init__(self, event: events.Event, args=None, call=False):
    self.event = event
    if call:
      getattr(GLOBAL, event.__name__)(event.__self__, args)

  def __call__(self, handle):
    if self.event == events.OnDisable:
      atexit.register(handle, self)
      return handle
    setattr(GLOBAL, self.event.__name__, handle)
    return handle


def load_mod(self):
  try:
    GLOBAL.OnEnable(self)
  except KeyError:
    pass


def init_mod(self):
  self.load()


def Mod(name: str, author: str, description: str, id: str):
    return type("mod", (object, ), {
      "__init__": init_mod,
      "load": load_mod,
      "name": name,
      "author": author,
      "description": description,
      "id": id,
      "events": events,
      "EventHandler": EventHandler,
    })
