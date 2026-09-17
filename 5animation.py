import os
import time

def clear_screen():
    # Очистка экрана для Windows ('cls') или Linux/macOS ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

# 3 кадра анимации (персонаж поднимает руки и делает шаг)
FRAME_1 = """
   (•_•)
   <)   )╯  Привет, консоль!
    /   \\
"""

FRAME_2 = """
   ( •_•)>⌐■-■
   (   (>   Загрузка стилей...
   /    \\
"""

FRAME_3 = """
   (⌐■_■)
  \\(   )/   Всё работает отлично!
   /   \\
"""

FRAMES = [FRAME_1, FRAME_2, FRAME_3]

COLOR = '\u001b[36m\u001b[1m'  # Яркий циан
RESET = '\u001b[0m'

def animate(cycles=4, delay=0.5):
    try:
        for _ in range(cycles):
            for frame in FRAMES:
                clear_screen()
                print(f"{COLOR}=== Демонстрация консольной анимации ==={RESET}")
                print(f"{COLOR}{frame}{RESET}")
                time.sleep(delay)
        clear_screen()
        print(f"{COLOR}=== Анимация успешно завершена! ==={RESET}")
    except KeyboardInterrupt:
        clear_screen()
        print("Воспроизведение остановлено пользователем.")

if __name__ == '__main__':
    animate(cycles=3, delay=0.5)