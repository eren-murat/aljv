import random
import constants

class Creature:
    curr_id = 0

    def __init__(self, pos = (0, 0)):
        self.id = Creature.curr_id
        Creature.curr_id += 1
        self.position = pos
        self.traits = [self.generate_random_trait() for i in range(constants.NUM_TRAITS)]
        self.eval_creature()

    def generate_random_trait(self):
        return random.uniform(0, 1)

    def update_position(self, pos):
        self.position = pos

    def update_traits(self, traits):
        self.traits = traits
        self.eval_creature()

    def eval_creature(self):
        self.score = sum(self.traits) / len(self.traits)

    def print_info(self):
        print("ID %.d at (%.d, %.d) | SCORE: %.2f | Size: %.2f Stamina: %.2f Strength: %.2f Speed: %.2f Smartness: %.2f " %(self.id, self.position[0], self.position[1], self.score, self.traits[0], self.traits[1], self.traits[2], self.traits[3], self.traits[4]))
    
    def get_size(self):
        return self.traits[0]

    def get_stamina(self):
        return self.traits[1]

    def get_strength(self):
        return self.traits[2]

    def get_speed(self):
        return self.traits[3]

    def get_smartness(self):
        return self.traits[4]

    def get_score(self):
        return self.score
