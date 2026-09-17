CYAN = '\u001b[36m\u001b[1m'  # Яркий бирюзовый цвет
RESET = '\u001b[0m'

def draw_pattern_c(repeats=3):
    # Матрица узора 'c' по рисунку 1.2
    # Каждый элемент заканчивается пробелом, чтобы не конфликтовать с кавычками
    pattern = [
        r"\     /   \     / ",
        r" \   /     \   /  ",
        r"  \ /   /\  \ /   ",
        r"   X   /  \  X    ",
        r"  / \ /    \/ \   ",
        r" /   X      X  \  ",
        r"/   / \    / \  \ ",
        r"   /   \  /   \   ",
        r"  /     \/     \  "
    ]

    print("Повторяющийся узор 'c':\n")
    for row in pattern:
        print(CYAN + (row + "  ") * repeats + RESET)

if __name__ == '__main__':
    draw_pattern_c(repeats=3)