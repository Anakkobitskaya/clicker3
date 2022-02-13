import pygame


class Shop:
    def __init__(self):
        self.image = pygame.image.load(r'img/Return_button.jpg')
        self.pos = (0, 0)
        self.image1 = pygame.image.load(r'img/Click.jpg')
        self.pos1 = (50, 100)
        self.image2 = pygame.image.load(r'img/yron_v_second.jpg')
        self.pos2 = (50, 400)
        self.click_cost = 10
        self.DPS_cost = 100

    def try_to_buy(self, type, balance):
        if type == 'click':
            if balance >= self.click_cost:
                self.click_cost *= 2
                return balance - self.click_cost // 2
        return balance

    def draw(self, screen, balance):
        screen.blit(self.image, self.pos)
        screen.blit(self.image1, self.pos1)
        screen.blit(self.image2, self.pos2)
        self.write(screen, balance)

    def write(self, screen, balance):
        font = pygame.font.SysFont('Arial.ttf', 80)
        text = font.render(f'У вас на счету: {balance}', True, [255, 255, 255])
        screen.blit(text, (60, 0))
