import random

def create_cells(width, height):
    coordinates = []
    for x in range(width):
        for y in range(height):
            coordinates.append((x, y))

    return dict.fromkeys(coordinates)

def place_creatures_on_map(population, cells, width, height):
    for p in population:
        pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        p.update_position(pos)

        if cells[pos] is None:
            cells[pos] = [p]
        else:
            cells[pos].append(p)

    return cells

def move_population(population, cells, width, height):
    new_cells = dict.fromkeys(cells.keys())
    for p in population:
        pos = p.position
        new_pos = (pos[0] + random.randint(-1, 1), pos[1] + random.randint(-1, 1))
        new_pos = (max(0, min(new_pos[0], width - 1)), max(0, min(new_pos[1], height - 1)))
        p.update_position(new_pos)

        if new_cells[new_pos] is None:
            new_cells[new_pos] = [p]
        else:
            new_cells[new_pos].append(p)

    return new_cells

def calculate_average_score(population):
    return sum([p.get_score() for p in population]) / len(population)