import pygame
import sys
import random

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 900, 600
PLAY_WIDTH = WIDTH - 300  # Right 300px reserved for hash table
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hash Table Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)
LIGHT_BLUE = (100, 180, 255)
RED = (200, 50, 50)
GREEN = (0, 180, 0)

# Difficulty settings
difficulty_levels = [" Easy", " Medium", " Hard"]
fall_speeds = [7, 9, 11]
selected_difficulty_index = 1  # Default to Medium
fall_speed = fall_speeds[selected_difficulty_index]

# Game state
game_state = 'start'
input_box = pygame.Rect(100, 200, 700, 40)
input_text = ''
active = False
button_rect = pygame.Rect(350, 300, 200, 50)
button_color = BLUE

# Difficulty selection buttons
dec_difficulty_rect = pygame.Rect(100, 260, 50, 30)
inc_difficulty_rect = pygame.Rect(750, 260, 50, 30)

element_list = []
selected_method = None

# Collision buttons
collision_methods = ["Linear Probing", "Quadratic Probing", "Double Hashing"]
method_buttons = []
for i, method in enumerate(collision_methods):
    rect = pygame.Rect(300, 180 + i * 70, 300, 50)
    method_buttons.append((method, rect))

# Game objects
bucket = pygame.Rect(WIDTH//2 - 50, HEIGHT - 60, 100, 20)
bucket_speed = 8
falling_items = []
misses = 0
MAX_MISSES = 3
caught_elements = []

TABLE_SIZE = 10
hash_table = [None] * TABLE_SIZE

def insert_to_hash_table(val):
    global hash_table
    key = val % TABLE_SIZE

    if selected_method == "Linear Probing":
        index = key
        for _ in range(TABLE_SIZE):
            if hash_table[index] is None:
                hash_table[index] = val
                return
            index = (index + 1) % TABLE_SIZE

    elif selected_method == "Quadratic Probing":
        for i in range(TABLE_SIZE):
            index = (key + i * i) % TABLE_SIZE
            if hash_table[index] is None:
                hash_table[index] = val
                return

    elif selected_method == "Double Hashing":
        h1 = key
        h2 = 7 - (val % 7)
        for i in range(TABLE_SIZE):
            index = (h1 + i * h2) % TABLE_SIZE
            if hash_table[index] is None:
                hash_table[index] = val
                return

def spawn_falling_item():
    if element_list:
        x = random.randint(50, PLAY_WIDTH - 50)
        val = element_list.pop(0)
        falling_items.append({'rect': pygame.Rect(x, -30, 40, 40), 'value': val})

def draw_start_screen():
    screen.fill(WHITE)
    title_surface = font.render("(game_emoji) Hash Table Visual Game", True, BLACK)
    screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

    instruction = font.render("Enter integers (space-separated, max 10):", True, BLACK)
    screen.blit(instruction, (input_box.x, input_box.y - 30))

    pygame.draw.rect(screen, GRAY if not active else BLUE, input_box, 2)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 5))

    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Start Game", True, WHITE)
    screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

    # Difficulty section
    diff_label = font.render("Difficulty:", True, BLACK)
    screen.blit(diff_label, (WIDTH // 2 - 60, 260))
    current_diff = font.render(difficulty_levels[selected_difficulty_index], True, BLACK)
    screen.blit(current_diff, (WIDTH // 2 + 40, 260))

    pygame.draw.rect(screen, LIGHT_BLUE, dec_difficulty_rect)
    screen.blit(font.render("<<", True, BLACK), (dec_difficulty_rect.x + 10, dec_difficulty_rect.y + 5))
    pygame.draw.rect(screen, LIGHT_BLUE, inc_difficulty_rect)
    screen.blit(font.render(">>", True, BLACK), (inc_difficulty_rect.x + 10, inc_difficulty_rect.y + 5))

def draw_game_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, bucket)
    for item in falling_items:
        pygame.draw.rect(screen, RED, item['rect'])
        val_text = font.render(str(item['value']), True, WHITE)
        screen.blit(val_text, (item['rect'].x + 8, item['rect'].y + 8))

    miss_text = font.render(f"Misses: {misses}/{MAX_MISSES}", True, BLACK)
    screen.blit(miss_text, (20, 20))
    caught_text = font.render(f"Caught: {caught_elements}", True, BLACK)
    screen.blit(caught_text, (20, 60))

def draw_hash_table(table):
    box_width = 140
    box_height = 40
    start_x = WIDTH - box_width - 60
    start_y = 100

    label = big_font.render("Hash Table Visualization", True, BLACK)
    screen.blit(label, (start_x, start_y - 50))

    for i in range(len(table)):
        y = start_y + i * (box_height + 10)
        index_label = font.render(str(i), True, BLACK)
        screen.blit(index_label, (start_x - 25, y + 10))
        pygame.draw.rect(screen, WHITE, (start_x, y, box_width, box_height))
        pygame.draw.rect(screen, BLACK, (start_x, y, box_width, box_height), 2)

        if table[i] is not None:
            text = font.render(str(table[i]), True, BLACK)
            screen.blit(text, (start_x + 10, y + 10))

def update_game():
    global misses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket.left > 0:
        bucket.move_ip(-bucket_speed, 0)
    if keys[pygame.K_RIGHT] and bucket.right < PLAY_WIDTH:
        bucket.move_ip(bucket_speed, 0)

    for item in list(falling_items):
        item['rect'].y += fall_speed
        if item['rect'].colliderect(bucket):
            val = item['value']
            caught_elements.append(val)
            insert_to_hash_table(val)
            falling_items.remove(item)
        elif item['rect'].y > HEIGHT:
            misses += 1
            falling_items.remove(item)

# Main loop
running = True
spawn_timer = 0
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == 'start':
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                if button_rect.collidepoint(event.pos):
                    try:
                        element_list = list(map(int, input_text.split()))
                        fall_speed = fall_speeds[selected_difficulty_index]
                        game_state = 'select_collision'
                    except ValueError:
                        print("Invalid input")
                elif dec_difficulty_rect.collidepoint(event.pos):
                    selected_difficulty_index = max(0, selected_difficulty_index - 1)
                elif inc_difficulty_rect.collidepoint(event.pos):
                    selected_difficulty_index = min(len(difficulty_levels) - 1, selected_difficulty_index + 1)

            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        elif game_state == 'select_collision':
            if event.type == pygame.MOUSEBUTTONDOWN:
                for method, rect in method_buttons:
                    if rect.collidepoint(event.pos):
                        selected_method = method
                        game_state = 'play'

    if game_state == 'start':
        draw_start_screen()     
    elif game_state == 'select_collision':
        screen.fill(WHITE)
        title = font.render("Choose Collision Resolution Method:", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        for method, rect in method_buttons:
            pygame.draw.rect(screen, LIGHT_BLUE, rect)
            text = font.render(method, True, BLACK)
            screen.blit(text, (rect.x + 20, rect.y + 10))
    elif game_state == 'play':
        if len(falling_items) == 0 and element_list:
            spawn_timer += 1
            if spawn_timer > 30:
                spawn_falling_item()
                spawn_timer = 0
        update_game()
        draw_game_screen()
        draw_hash_table(hash_table)
        if misses >= MAX_MISSES:
            screen.fill(WHITE)
            game_over = font.render("Game Over! You missed too many!", True, RED)
            screen.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, HEIGHT // 2))
        elif not element_list and not falling_items:
            win_text = font.render("(congratulations_emoji) You caught all elements!", True, GREEN)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()