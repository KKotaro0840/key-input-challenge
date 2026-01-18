import pygame
from scenes.base_scene import BaseScene
from utils.helpers import draw_text


class ResultScene(BaseScene):
  def __init__(self, manager, logic):
    super().__init__(manager)
    self.logic = logic

  def handle_event(self, event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
      from scenes.name_input_scene import NameInputScene
      self.manager.change_scene(
          NameInputScene(self.manager, self.logic)
      )

  def draw(self, screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "ゲーム終了", 320, 140)
    draw_text(screen, f"成功数: {self.logic.success}", 300, 220)
    draw_text(screen, f"正解キー数: {self.logic.correct}", 300, 260)
    draw_text(screen, f"ミス回数: {self.logic.miss}", 300, 300)
    draw_text(screen, "Enter: なまえにゅうりょく", 240, 360)
