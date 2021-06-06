# Hydrogen Mod Loader (HML)

HML Is a feature rich modding framework for all your python needs.

## Features

- EventHandler
  - Automated events
  - Manual event calling
- Static and Dynamic mod loading
- Mod meta data
- Drag & drop infrastructure

## Installation

Download your wanted version from the 'releases' folder and extract it to a folder called 'mods'.
Now you have to choose between static or dynamic loading with the key diffrence being you load a mod with importlib with dynamic loading and vanilla python for static.

### Dynamic mod loading

```python
import importlib
mod_name = "example" # mod to install in 'mods' folder
mods = {} # dict for easy access of mods
mods[mod_name] = getattr(importlib.import_mod(f"mods.{mod_name}"), mod_name)() # get the mod class in the mod and initates it and adds it to the mod dict.
```

### Static mod loading

```python
import mods.example as example
example = example.example()
```
