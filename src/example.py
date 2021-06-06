from .hydrogen import Mod, EventHandler, events
META = Mod("Example Mod", "Commander", "Example HML mod", "hml:example")


class example(META):
  def __init__(self):
    super().__init__()

  @EventHandler(events.OnEnable)
  def OnEnable(self):
    print("Example mod enabled!")

  @EventHandler(events.OnDisable)
  def OnDisable(self):
    print("Example mod disabled!")