AXIS_COLOR = '\u001b[33m'          # Жёлтый цвет осей и меток
LINE_COLOR = '\u001b[32m\u001b[1m'  # Ярко-зелёный цвет графика
RESET = '\u001b[0m'

def plot_linear_function():
    # Параметры сетки: 10 строк по вертикали (y от 0 до 18) и 10 значений по x (от 0 до 9)
    y_steps = 10
    x_steps = 10

    print("График функции y = 2x (1 квадрант):\n")

    # Идём сверху вниз по оси Y
    for row in range(y_steps - 1, -1, -1):
        y_val = row * 2
        # Метка на оси Y
        row_str = f"{AXIS_COLOR}{y_val:2d} |{RESET} "
        for x in range(x_steps):
            # Проверяем равенство y = 2x
            if 2 * x == y_val:
                row_str += f"{LINE_COLOR}* {RESET}"
            else:
                row_str += "  "
        print(row_str)

    # Горизонтальная ось X
    print(f"{AXIS_COLOR}    +" + "--" * (x_steps * 2 - 1) + f"{RESET}")
    # Подписи значений оси X
    x_labels = " ".join(f"{x:2d}" for x in range(x_steps))
    print(f"{AXIS_COLOR}     {x_labels}{RESET}")

if __name__ == '__main__':
    plot_linear_function()