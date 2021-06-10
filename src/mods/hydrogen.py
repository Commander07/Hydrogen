"""
Classes:

    events
    utils

Decorator:

    EventHandler(event: events.Event)

Functions:

    Mod(name: str, author: str, description: str, id: str) -> ModMetaData

utils:

    import_mod(self, mod)
    call_event(self, event: events.Event, data: object) -> list[Any | None]
    get(self, mod) -> class ...(ModMetaData)

"""
import os
import atexit
import importlib
from .__config__ import events as __events__
class GLOBAL: pass


class events(__events__):
  OnEnable = __events__.Event("OnEnable")
  OnDisable = __events__.Event("OnDisable")


class EventHandler:
  def __init__(self, event: events.Event, args=None, call=False):
    self.event = event
    if call:
      self.return_value = getattr(GLOBAL, event.__name__)(event.__self__, args)

  def __call__(self, handle):
    if self.event == events.OnDisable:
      atexit.register(handle, self)
      return handle
    setattr(GLOBAL, self.event.__name__, handle)
    return handle

  def get_return_value(self):
    return self.return_value


class utils:
  def __init__(self):
    self.mods = {}

  def import_mod(self, mod):
    self.mods[mod] = getattr(importlib.import_module(f"mods.{mod}"), mod)()

  def import_mods(self):
    for mod in [''.join(file.split(".")[:-1]) for file in next(os.walk("mods"))[2] if not file.startswith("__") and file != "hydrogen.py"]:
      self.import_mod(mod)

  def call_event(self, event: events.Event, data: object) -> list[any | None]:
    return_values = []
    for mod in self.mods:
      EventInstance = getattr(self.mods[mod].events, event.__name__)(self.mods[mod])
      return_values.append(self.mods[mod].EventHandler(EventInstance, args=data, call=True).get_return_value())
    return return_values

  def get(self, mod):
    return self.mods[mod]


utils = utils()


def load_mod(self):
  try:
    GLOBAL.OnEnable(self)
  except KeyError:
    pass


def init_mod(self):
  self.load()


def Mod(name: str, author: str, description: str, id: str):
    return type("ModMetaData", (object, ), {
      "__init__": init_mod,
      "load": load_mod,
      "name": name,
      "author": author,
      "description": description,
      "id": id,
      "events": events,
      "EventHandler": EventHandler,
    })
