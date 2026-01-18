import pygame
from scenes.base_scene import BaseScene
from utils.helpers import draw_text


class ModeSelectScene(BaseScene):
  def handle_event(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        from scenes.game_scene import GameScene
        self.manager.change_scene(GameScene(self.manager, "WASD"))

      elif event.key == pygame.K_2:
        from scenes.game_scene import GameScene
        self.manager.change_scene(GameScene(self.manager, "ARROW"))

      elif event.key == pygame.K_3:
        from scenes.custom_config_scene import CustomConfigScene
        self.manager.change_scene(CustomConfigScene(self.manager))

      elif event.key == pygame.K_ESCAPE:
        from scenes.menu_scene import MenuScene
        self.manager.change_scene(MenuScene(self.manager))

  def draw(self, screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "ゲームモード選択", 280, 150)
    draw_text(screen, "1: WASDキー", 300, 250)
    draw_text(screen, "2: ヤジルシキー", 300, 300)
    draw_text(screen, "3: カスタム", 300, 350)
    draw_text(screen, "ESC: もどる", 300, 430)
