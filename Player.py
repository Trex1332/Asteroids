from CircleShape import *
from bullet import Bullet

class Player(CircleShape,):
    timer = 0
    def __init__(self,x,y):

        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        self.position += self.velocity * dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
             self.rotate(dt)
        if keys[pygame.K_w]:
             self.move(dt)
        if keys[pygame.K_s]:
             self.move(-dt)
        if keys[pygame.K_SPACE]:
            
            if self.timer <= 0:
                self.timer = PLAYER_SHOOT_COOLDOWN
                self.shoot()
            
                

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        shot = Bullet(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED