import random


class Player:
    # static class var attrib here
    # constructor, below,

    def __init__(self, name, health, strength):
        self.name = name
        self.validate_health(health)
        self.health = health
        self.validate_strength(strength)
        self._strength = strength
        self._starting_health = self.health
        self._current_health = self._starting_health

    def name(self):
        return self.name

    def health(self):
        return self.health

    def validate_health(self, health):
        if health > 100 or health < 1:
            raise ValueError(f"Invalid health: {health}")

    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, new_health):
        self.validate_health(new_health)
        self._current_health = new_health

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, new_strength):
        self.validate_strength(new_strength)
        self._strength = new_strength

    def validate_strength(self, strength):
        if strength > 100 or strength < 1:
            raise ValueError(f'Invalid date: {strength}')

    def attack(self):
        attacks = random.randint(0, self.strength)
        return attacks

    def take_damage(self, damage_amount):
        damage_block = random.randint(0, damage_amount)
        total_damage = (damage_amount - damage_block)
        self._current_health -= total_damage
        if self.current_health < 0:
            print(f'Player {self.name} is dead with {self.current_health} health!')
            exit()   # added this here as I am still figuring out why it doesn't accept bool.
            return True
        else:
            return False

    def heal(self):
        self._current_health += 10
        if self._current_health > self._starting_health:
            self._current_health -= self._current_health
            self._current_health += self._starting_health
            return self._current_health
        else:
            return self._current_health

    def __str__(self):
        # if health is less than 0 send in message it has died, see above, made it exit...
        # need to redo without exit next time
        return f'Player: {self.name}, Health: {self._current_health}, Strength: {self._strength}'
