from .hydrogen import Mod, EventHandler, events
META = Mod("Example Mod", "Commander", "Example hydrogen mod", "hydrogen:example")


class example(META):
  def __init__(self):
    super().__init__()

  @EventHandler(events.OnEnable)
  def OnEnable(e):
    print(e)