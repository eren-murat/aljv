from pygame import Vector2, Color, draw, font
import constants

def convert_map_to_screen(x, y):
    return Vector2(constants.RADIUS * (2 * x + 1), constants.RADIUS * (2 * y + 1))

def draw_creature(screen, creature):
    screen_pos = convert_map_to_screen(creature.position[0], creature.position[1])
    size = constants.RADIUS / 2* (creature.get_size() + 1)

    stamina_color = Color(0, round(255 * creature.get_stamina()), 0)
    strength_color = Color(round(255 * creature.get_strength()), 0, 0)
    speed_color = Color(round(255 * creature.get_speed()), round(255 * creature.get_speed()), 0)
    smartness_color = Color(0, 0, round(255 * creature.get_smartness()))

    draw.circle(screen, stamina_color, screen_pos, size, 0, True)
    draw.circle(screen, strength_color, screen_pos, size, 0, False, True)
    draw.circle(screen, speed_color, screen_pos, size, 0, False, False, True)
    draw.circle(screen, smartness_color, screen_pos, size, 0, False, False, False, True)

    id_font = font.SysFont('Arial', 12)
    text_surface = id_font.render(str(creature.id), True, (0, 0, 0))
    screen.blit(text_surface, screen_pos + Vector2(size, size/2))

