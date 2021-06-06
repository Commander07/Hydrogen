"""
name: HML
author: https://github.com/commander07
description: Hydrogen Mod Loader (HML) is a modding framework for python games. That has features such as events, override and more!
"""
from dataclasses import dataclass
class GLOBAL: pass


class events:
  @dataclass
  class Event: name: str
  OnEnable = Event("OnEnable")
  OnDisable = Event("OnDisable")


class EventHandler:
  def __init__(self, event: events.Event):
    self.event = event

  def __call__(self, handle):
    setattr(GLOBAL, "example", {})
    getattr(GLOBAL, "example")[self.event.name] = handle

    return handle


def load_mod(self):
  try:
    getattr(GLOBAL, "example")["OnEnable"](events.OnEnable)
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
    })