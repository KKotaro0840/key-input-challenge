import pygame
from scenes.base_scene import BaseScene
from utils.helpers import draw_text


class MenuScene(BaseScene):
  def handle_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        from scenes.mode_select_scene import ModeSelectScene
        self.manager.change_scene(ModeSelectScene(self.manager))

      elif event.key == pygame.K_2:
        from scenes.record_scene import RecordScene
        self.manager.change_scene(RecordScene(self.manager))

  def draw(self, screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "Key Input Challenge", 260, 150)
    draw_text(screen, "1: ゲームプレイ", 300, 260)
    draw_text(screen, "2: キロク", 300, 310)
