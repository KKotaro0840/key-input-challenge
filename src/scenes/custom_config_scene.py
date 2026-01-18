import pygame
from scenes.base_scene import BaseScene
from scenes.game_scene import GameScene
from utils.helpers import draw_text

class CustomConfigScene(BaseScene):
  def __init__(self, manager):
    super().__init__(manager)
    self.cursor = 0
    self.config = {
        "start_key_length": 3,
        "base_keys": ["a", "s", "d"],
        "increase_length_every": 5,
        "add_key_every": 10,
        "additional_keys": ["q", "e"],
        "time_limit": 15.0
    }

  def handle_event(self, event):
    if event.type != pygame.KEYDOWN:
      return

    if event.key == pygame.K_UP:
      self.cursor = (self.cursor - 1) % 6
    elif event.key == pygame.K_DOWN:
      self.cursor = (self.cursor + 1) % 6
    elif event.key == pygame.K_LEFT:
      self._change_value(-1)
    elif event.key == pygame.K_RIGHT:
      self._change_value(1)
    elif event.key == pygame.K_RETURN:
      self.manager.change_scene(
          GameScene(self.manager, "CUSTOM", self.config)
      )
    elif event.key == pygame.K_ESCAPE:
      from scenes.mode_select_scene import ModeSelectScene
      self.manager.change_scene(ModeSelectScene(self.manager))

  def _change_value(self, delta):
    if self.cursor == 0:
      self.config["start_key_length"] = max(
          1, self.config["start_key_length"] + delta)
    elif self.cursor == 2:
      self.config["increase_length_every"] = max(
          1, self.config["increase_length_every"] + delta)
    elif self.cursor == 3:
      self.config["add_key_every"] = max(
          1, self.config["add_key_every"] + delta)
    elif self.cursor == 5:
      self.config["time_limit"] = max(
          5, self.config["time_limit"] + delta)

  def draw(self, screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "カスタム設定", 300, 80)
    items = [
        f"初期キー数: {self.config['start_key_length']}",
        f"基本キー: {', '.join(self.config['base_keys'])}",
        f"キー数増加成功数: {self.config['increase_length_every']}",
        f"キー追加成功数: {self.config['add_key_every']}",
        f"追加キー: {', '.join(self.config['additional_keys'])}",
        f"制限時間: {self.config['time_limit']:.1f}"
    ]

    y = 180
    for i, item in enumerate(items):
      prefix = "▶ " if i == self.cursor else "   "
      draw_text(screen, prefix + item, 200, y)
      y += 45
