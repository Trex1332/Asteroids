from CircleShape import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.rad = radius

    def draw(self,screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius, 2)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * velocity * dt

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
        self.position += self.velocity * dt


    def split(self):
        self.kill() 
        if self.rad == ASTEROID_MIN_RADIUS:
            return
        

        
           #split
        angle = random.uniform(20,50)

        a1 = self.velocity.rotate(angle )
        a2 = self.velocity.rotate(-angle)

        a1 *= 1.2
        a2 *=1.2


        newrad = self.rad - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, newrad)
        ast1.velocity = a1
        ast2 = Asteroid(self.position.x, self.position.y, newrad)
        ast2.velocity = a2

       



