import pygame
from scenes.base_scene import BaseScene
from data.record_manager import RecordManager
from utils.helpers import draw_text, is_katakana
from utils.constants import MAX_NAME_LENGTH


class NameInputScene(BaseScene):
  def __init__(self, manager, logic):
    super().__init__(manager)
    self.logic = logic
    self.name = ""
    pygame.key.start_text_input()  # ★必ずここ

  def handle_event(self, event):
    if event.type == pygame.TEXTINPUT:
      for char in event.text:
        if is_katakana(char) and len(self.name) < MAX_NAME_LENGTH:
          self.name += char

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        if self.name == "":
          self.name = "ナナシ"

        RecordManager.save({
            "name": self.name,
            "mode": self.logic.mode,
            "success": self.logic.success,
            "correct": self.logic.correct,
            "miss": self.logic.miss
        })

        pygame.key.stop_text_input()  # ★必ずここ
        from scenes.menu_scene import MenuScene
        self.manager.change_scene(MenuScene(self.manager))

      elif event.key == pygame.K_BACKSPACE:
        self.name = self.name[:-1]

def draw(self, screen):
    # fill は1回だけ
  screen.fill((0, 0, 0))

  draw_text(screen, "なまえをにゅうりょく（カナ）", 200, 200)
  draw_text(screen, self.name + "▌", 300, 260)
