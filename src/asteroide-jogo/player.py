import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOT_SPEED, SHOT_RADIUS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            self.velocity += forward * 100 * dt

        if keys[pygame.K_s]:
            backward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += backward * 100 * dt
            
        if keys[pygame.K_a]:
            self.rotation -= 180 * dt
        if keys[pygame.K_d]:
            self.rotation += 180 * dt
            
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.position += self.velocity * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        direction = pygame.Vector2(0, -1).rotate(self.rotation)  # Changed from self.angle to self.rotation
        shot.velocity = direction * PLAYER_SHOT_SPEED
        return shot
        