RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'

def draw_netherlands_flag(width=30, stripe_height=3):
    # Красная полоса
    for _ in range(stripe_height):
        print(f"{RED}{' ' * width}{END}")
    # Белая полоса
    for _ in range(stripe_height):
        print(f"{WHITE}{' ' * width}{END}")
    # Синяя полоса
    for _ in range(stripe_height):
        print(f"{BLUE}{' ' * width}{END}")

if __name__ == '__main__':
    draw_netherlands_flag()