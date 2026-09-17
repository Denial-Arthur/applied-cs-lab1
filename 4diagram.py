import os
import random

FILENAME = 'sequence.txt'

# 1. Автогенерация файла, если он еще не создан
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for _ in range(250):
            f.write(f"{round(random.uniform(-50.0, 50.0), 2)}\n")

# 2. Чтение последовательности из файла
numbers = []
with open(FILENAME, 'r', encoding='utf-8') as file:
    for line in file:
        val = line.strip()
        if val:
            numbers.append(float(val))

# 3. Подсчет сумм по модулю для четных и нечетных индексов
# Четные позиции: 0, 2, 4... Нечетные: 1, 3, 5...
sum_even = 0.0
sum_odd = 0.0

for idx, num in enumerate(numbers):
    if idx % 2 == 0:
        sum_even += abs(num)
    else:
        sum_odd += abs(num)

total_sum = sum_even + sum_odd
pct_even = (sum_even / total_sum) * 100 if total_sum > 0 else 0
pct_odd = (sum_odd / total_sum) * 100 if total_sum > 0 else 0

# 4. Вывод числовой статистики
print(f"Обработано чисел из файла: {len(numbers)}")
print(f"Сумма по модулю (четные позиции):   {sum_even:.2f} ({pct_even:.1f}%)")
print(f"Сумма по модулю (нечетные позиции): {sum_odd:.2f} ({pct_odd:.1f}%)\n")

# 5. Отрисовка цветной диаграммы с использованием ANSI-символов
BAR_EVEN = '\u001b[42m'  # Зеленый фон
BAR_ODD = '\u001b[44m'   # Синий фон
RESET = '\u001b[0m'

MAX_BAR_WIDTH = 50
len_even = int((pct_even / 100) * MAX_BAR_WIDTH)
len_odd = int((pct_odd / 100) * MAX_BAR_WIDTH)

print("Диаграмма процентного соотношения:")
print(f"Чётные   | {BAR_EVEN}{' ' * len_even}{RESET}{' ' * (MAX_BAR_WIDTH - len_even)} | {pct_even:.1f}%")
print(f"Нечётные | {BAR_ODD}{' ' * len_odd}{RESET}{' ' * (MAX_BAR_WIDTH - len_odd)} | {pct_odd:.1f}%")