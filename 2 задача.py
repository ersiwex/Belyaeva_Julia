import random
import time
import os
def print_slow(text):
  """Выводит текст посимвольно с задержкой."""
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)
  print()
def generate_story():
  characters = ["Программист", "Дизайнер", "Менеджер", "Стажер"] # Добавил "Стажер"
  locations = ["Хакатон", "Школа", "Колледж", "Универ", "Офис"] # Добавил "Офис"
  actions = ["отправился на поиски решения", "не правильно создала фрейм", "не смог(а)подружиться с...", "Стали победителями...", 
             "застрял(а) в...", "влюбился(ась) в...", "нашел(а) общий язык с...", "потерял(а) важный файл..."]
  objects = ["Победа", "Участие", "Создание", "Знания", "Опыт", "Коллегой", "Проектом", "Дедлайном"]
  character = random.choice(characters)
  location = random.choice(locations)
  action = random.choice(actions)
  object = random.choice(objects)
  story = f"{character} {action} {object} в {location}..."
  return story
def clear_screen():
  """Очищает экран консоли."""
  os.system('cls' if os.name == 'nt' else 'clear')
def main():
  clear_screen()
  print_slow("Привет! Готов(а) к увлекательному приключению?")
  time.sleep(1)
  print_slow("Тогда держись крепче...")
  time.sleep(1)
  print_slow("...")
  time.sleep(1)

  story = generate_story()
  print_slow(story)
  print_slow("Что будет дальше?")
  time.sleep(1)
  print_slow("Это зависит только от тебя...")
if __name__ == "__main__": 
  main() 