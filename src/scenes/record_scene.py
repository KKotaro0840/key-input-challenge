import pygame
from scenes.base_scene import BaseScene
from scenes.menu_scene import MenuScene
from data.record_manager import RecordManager
from utils.helpers import draw_text


class RecordScene(BaseScene):
  def handle_event(self, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      self.manager.change_scene(MenuScene(self.manager))

  def draw(self, screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "キロク（最新8回）", 300, 80)

    records = RecordManager.load()
    latest = list(reversed(records))[:8]

    y = 160
    for record in latest:
      mode = record.get("mode", "UNKNOWN")
      draw_text(
          screen,
          f"{record.get('name', '?')} | {mode} | "
          f"成功:{record.get('success', 0)} "
          f"正解:{record.get('correct', 0)} "
          f"ミス:{record.get('miss', 0)}",
          80, y
      )
      y += 40

    draw_text(screen, "ESC: もどる", 320, 520)
