import pygame
import math
import constants
import genetic_algo as ga
import render
import utils
import matplotlib.pyplot as plt

# pygame setup
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# map setup
map_width = math.floor(constants.SCREEN_WIDTH/(constants.RADIUS*2))
map_height = math.floor(constants.SCREEN_HEIGHT/(constants.RADIUS*2))
cells = utils.create_cells(map_width, map_height)

# simulation setup
population = ga.generate_population(constants.INIT_POPULATION_SIZE)
cells = utils.place_creatures_on_map(population, cells, map_width, map_height)

year = 0
day = 0
pause = False

print("\nYEAR ", year)
yearly_average_scores = []
avg_score_at_start = utils.calculate_average_score(population)
print("Average score: %.2f" %(avg_score_at_start))
yearly_average_scores.append(avg_score_at_start)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        pause = not pause

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    gen_font = pygame.font.SysFont('Arial', 20)
    text_surface = gen_font.render('Year ' + str(year), False, (0, 0, 0))
    screen.blit(text_surface, (0,0))

    for p in population:
        render.draw_creature(screen, p)

    if not pause:
        day += 1
        if day % (constants.DAYS_IN_YEAR / constants.SIM_SPEED) == 0:
            cells = utils.move_population(population, cells, map_width, map_height)
            # dynamic simulation is triggered by two similar creatures meeting in adjacent cells
            population, cells = ga.dynamic_simulate(population, cells, map_width, map_height)

        if day == constants.DAYS_IN_YEAR:
            year += 1
            day = 0
            print("\nYEAR ", year)
            yearly_avg_score = utils.calculate_average_score(population)
            print("Average score: %.2f" %(yearly_avg_score))
            yearly_average_scores.append(yearly_avg_score)
            # simple simulation is standard genetic algorithm (always selects the two best parents)
            # population, cells = ga.simple_simulate(population, cells, map_width, map_height)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

# plot yearly average scores
plt.xticks(range(0, year))
plt.plot(yearly_average_scores)
plt.title("Population Average Score Over Time")
plt.xlabel("Year")
plt.ylabel("Score")
plt.show()