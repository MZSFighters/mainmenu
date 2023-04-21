import pygame
from menu import MainMenu

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 700, 650
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))  #creates our canvas
        #window for player to see what we are drawing
        self.window = pygame.display.set_mode(((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)))
        self.font_name = "arialblack"
        #put some colours 
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        # now we have our game object
        self.curr_menu = MainMenu(self)


    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing = False
            #self.display.fill(self.BLACK)   #reset ur canvas
            start_image = pygame.image.load("onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.display.blit(start_image, (0,0))
            self.draw_text("Hi", 20, self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2)
            self.window.blit(self.display, (0,0)) # whatever we draw on display will nowcome on window
            pygame.display.update() #physically moves image on the computer screen
            self.reset_keys()
    

                




    # let's create the game loop

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                #added later
                self.curr_menu.run_display =False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            # we need a way to reset these variables after each game loop or each frame
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY = False, False, False, False

# to draw text on the screen
    def draw_text(self, text, size, x, y):
        #font = pygame.font.Font(self.font_name, size)
        font = pygame.font.SysFont("arialblack", 40)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)


