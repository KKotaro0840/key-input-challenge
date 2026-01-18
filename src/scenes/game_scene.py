import pygame
import time
from scenes.base_scene import BaseScene
from scenes.result_scene import ResultScene
from game.game_logic import GameLogic
from game.key_generator import KeyGenerator
from utils.helpers import draw_text


class GameScene(BaseScene):
  def __init__(self, manager, mode, custom_config=None):
    super().__init__(manager)

    self.mode = mode
    self.start_time = time.time()
    self.exit_hold = None

    if mode == "CUSTOM":
      config = custom_config
    elif mode == "WASD":
      config = {
          "base_keys": ["w", "a", "s", "d"],
          "start_key_length": 3,
          "increase_length_every": 5,
          "add_key_every": 10,
          "additional_keys": ["q", "e"],
          "time_limit": 15.0
      }
    else:  # ARROW
      config = {
          "base_keys": ["up", "down", "left", "right"],
          "start_key_length": 3,
          "increase_length_every": 5,
          "add_key_every": 999,
          "additional_keys": [],
          "time_limit": 15.0
      }

    self.logic = GameLogic(config, mode)
    self.generator = KeyGenerator(self.logic.keys, self.logic.key_length)
    self.problem = self.generator.generate()
    self.index = 0

  def handle_event(self, event):
    if event.type == pygame.KEYDOWN:
      key = pygame.key.name(event.key)
      if key == self.problem[self.index]:
        self.index += 1
        self.logic.correct += 1
        if self.index >= len(self.problem):
          self.logic.on_success()
          self._new_problem()
      else:
        self.logic.on_miss()
        self._new_problem()

  def update(self, dt):
    if time.time() - self.start_time > self.logic.time_limit:
      self.manager.change_scene(ResultScene(self.manager, self.logic))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and keys[pygame.K_q]:
      if self.exit_hold is None:
        self.exit_hold = time.time()
      elif time.time() - self.exit_hold >= 1:
        self.manager.change_scene(ResultScene(self.manager, self.logic))
    else:
      self.exit_hold = None

  def _new_problem(self):
    self.generator = KeyGenerator(self.logic.keys, self.logic.key_length)
    self.problem = self.generator.generate()
    self.index = 0

  # ★★★★★ ここがクラス内 ★★★★★
  def draw(self, screen):
    screen.fill((0, 0, 0))

    remaining = self.logic.time_limit - (time.time() - self.start_time)

    if self.mode == "WASD":
      display_keys = [k.upper() for k in self.problem]
    elif self.mode == "ARROW":
      arrow_map = {"up": "↑", "down": "↓", "left": "←", "right": "→"}
      display_keys = [arrow_map[k] for k in self.problem]
    else:
      display_keys = self.problem

    base_x = 200
    y_keys = 280
    y_arrow = 320
    spacing = 40

    draw_text(screen, f"残り時間: {remaining:.1f}", 40, 40)

    for i, key in enumerate(display_keys):
      draw_text(screen, key, base_x + i * spacing, y_keys)

    draw_text(screen, "▲", base_x + self.index * spacing, y_arrow)
