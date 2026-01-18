import pygame
from utils.constants import FONT_NAME, FONT_SIZE, TEXT_COLOR

_font = None

def get_font():
  global _font
  if _font is None:
    _font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
  return _font

def draw_text(screen, text, x, y):
  font = get_font()
  image = font.render(text, True, TEXT_COLOR)
  screen.blit(image, (x, y))

def is_katakana(char):
  return ('ァ' <= char <= 'ヴ') or char == 'ー'
