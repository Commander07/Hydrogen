# Hydrogen Mod Loader (HML)

HML Is a feature rich modding framework for all your python needs.

## Features

- EventHandler
  - Automated events
  - Manual event calling
  - Event return values
  - Custom Events
- Static and Dynamic mod loading
- Mod meta data
- User friendly api
- Drag & drop infrastructure

## Installation

Download your wanted version [here](https://github.com/Commander07/Hydrogen/releases) and extract it and move everything in the 'src' folder to your project root.

## Usage

### Importing mods

```python
from mods.hydrogen import utils, events

# Import mod 'example'.
utils.import_mod("example")
```

### Get mod instance

```python
from mods.hydrogen import utils, events

# Get mod 'example'.
utils.get("example")
```

### Calling events

```python
from mods.hydrogen import utils, events


# Object to store event data.
class data:
  name = "Zombie"


# Call event OnKill in all mods with the data from the data object.
return_value = utils.call_event(events.OnKill, data)
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
