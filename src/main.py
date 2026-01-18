import pygame
from scene_manager import SceneManager
from scenes.menu_scene import MenuScene


def main():
  pygame.init()
  pygame.font.init()

  screen = pygame.display.set_mode((800, 600))
  pygame.display.set_caption("Key Input Challenge")
  clock = pygame.time.Clock()

  manager = SceneManager(screen)
  manager.change_scene(MenuScene(manager))

  running = True
  while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      manager.handle_event(event)

    manager.update(dt)

    # ❗ ここで fill しない
    manager.draw()
    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()
