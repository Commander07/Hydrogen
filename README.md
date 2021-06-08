# Hydrogen Mod Loader (HML)

HML Is a feature rich modding framework for all your python needs.

## Features

- EventHandler
  - Automated events
  - Manual event calling
  - Custom Events
- Static and Dynamic mod loading
- Mod meta data
- Drag & drop infrastructure

## Installation

Download your wanted version [here](https://github.com/Commander07/Hydrogen/releases) and extract it and move everything in the 'src' folder to a folder called 'mods' in your project root.

## Usage

### Importing mods

```python
import importlib

# Create 2 variables 1 for storing all mods and 1 for the name of a mod too be imported.
example = "example"
mods = {}

# Import the mod and initialise it into the 'mods' variable
mods[example] = getattr(importlib.import_module(f"mods.{example}"), example)()
```

### Calling events

```python
# Object to store event data.
class store:
  name = "Zombie"


# Grab event from selected mod and give it the mod instance.
OnKillEvent = mods["example"].events.OnKill(mods["example"])

# Grab the hydrogen EventHandler and run the 'OnKillEvent' with the data in the 'store' variable.
mods["example"].EventHandler(OnKillEvent, store, call=True)
```

### Creating events

In 'mods/\_\_config__.py' you will find a class named 'events' if you want to add events you just simply want to add a line following the syntax shown in the example.

```python
from dataclasses import dataclass


class events:
  @dataclass
  class Event:
    __name__: str

    def __call__(self, mod_instance):
      self.__self__ = mod_instance
      return self

  # Creates an 'OnKill' event
  OnKill = Event("OnKill")
```
