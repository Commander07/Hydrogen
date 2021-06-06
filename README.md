# Hydrogen Mod Loader (HML)
HML Is a feature rich modding framework for all your python needs.
## Features
- EventHandler
    - Automated events
    - Manual event calling
- Static and Dynamic mod loading
- Mod meta data
- Drag & drop infrastructure
## Dynamic mod loading
```python
import importlib
mod_name = "example"
mods = {}
mods[mod_name] = getattr(importlib.import_mod(f"mods.{mod_name}"), mod_name)()
```
## Static mod loading
```python
import mods.example as example
example = example.example()
```