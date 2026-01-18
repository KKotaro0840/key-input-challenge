class BaseScene:
  def __init__(self, manager):
    self.manager = manager

  def handle_event(self, event):
    pass

  def update(self, dt):
    pass

  def draw(self, screen):
    screen.fill((0, 0, 0))
