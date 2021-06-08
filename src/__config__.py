from dataclasses import dataclass


class events:
  @dataclass
  class Event:
    __name__: str

    def __call__(self, mod_instance):
      self.__self__ = mod_instance
      return self

  OnKill = Event("OnKill")
