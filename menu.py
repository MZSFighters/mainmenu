
import pygame

class Menu():
    def __init__(self, game):   #we taking game so we can make use of game variables we have already created
        self.game = game    #we storing the game we got as input in the self.game variable
        self.MID_WEIGHT, self.MID_HEIGHT = self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2
        self.run_display = True #variable that tells our menu to keep running
        self.cursor_rect = pygame.Rect(20, 0, self.MID_WEIGHT - 110, self.MID_HEIGHT - 200)    #creating the cursor rect
        self.offset = 70       #offset for our cursor(we want it to be on our lefft and not on top of our text)

    # let's write some helper functions
    def draw_cursor(self):
        #let's make use of the cursor already in oyr game file
        #self.game.draw_text("->", 15, self.cursor_rect.x, self.cursor_rect.y) #current x and y position that we can adjust to move up and down
        cursor = pygame.image.load("katana-28768.png")
        cursor = pygame.transform.scale(cursor, (100, 50))
        self.game.display.blit(cursor, (self.cursor_rect.x,self.cursor_rect.y))
    # blitting our menu to the screen
    def blit_screen(self):
        # from our hame loop
        self.game.window.blit(self.game.display, (0,0)) # whatever we draw on display will nowcome on window
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        self.state ="Start"     #we want our cursor to point at the start option
        self.startx, self.starty = self.MID_WEIGHT , self.MID_HEIGHT -35
        self.lsgx, self.lsgy = self.MID_WEIGHT, self.MID_HEIGHT + 15
        self.htpx, self.htpy = self.MID_WEIGHT, self.MID_HEIGHT + 65
        self.customcardsx, self.customcardsy = self.MID_WEIGHT, self.MID_HEIGHT + 115
        self.leaderboardx, self.leaderboardy = self.MID_WEIGHT, self.MID_HEIGHT + 165
        self.settingsx, self.settingsy = self.MID_WEIGHT, self.MID_HEIGHT + 215
        self.exitx, self.exity = self.MID_WEIGHT, self.MID_HEIGHT + 265
        #starting position for our cursor
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()    #checking input
            self.check_input()
            #self.game.display.fill(self.game.BLACK)
            start_image = pygame.image.load("onitama_highres.jpg")
            start_image = pygame.transform.scale(start_image, (700, 650))
            self.game.display.blit(start_image, (0,0))
            size = 10
            # Let's draw some text on the screen ...
            #self.game.draw_text('Main Menu',20, self.game.DISPLAY_WIDTH /2, self.game.DISPLAY_HEIGHT/2 -20)
            self.game.draw_text('Start New Game', size, self.startx, self.starty)
            self.game.draw_text('Load Saved Game', size, self.lsgx, self.lsgy)
            self.game.draw_text('How To Play', size, self.htpx, self.htpy)
            self.game.draw_text('Custom Cards', size, self.customcardsx, self.customcardsy)
            self.game.draw_text('Leaderboard', size, self.leaderboardx, self.leaderboardy)
            self.game.draw_text('Settings', size, self.settingsx, self.settingsy)
            self.game.draw_text('Exit', size, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()      # put everything on screen

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.lsgx + self.offset, self.lsgy)
                self.state = "LSG"
            elif self.state == 'LSG':
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.state = "HTP"
            elif self.state == "HTP":
                self.cursor_rect.midtop = (self.customcardsx + self.offset, self.customcardsy)
                self.state = "CustomCards"
            elif self.state == "CustomCards":
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = "LeaderBoard"
            elif self.state == "LeaderBoard":
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = "Settings"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"

        elif self.game.UP_KEY:
            '''
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            '''
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == 'LSG':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "HTP":
                self.cursor_rect.midtop = (self.lsgx + self.offset, self.lsgy)
                self.state = "LSG"
            elif self.state == "CustomCards":
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.state = "HTP"
            elif self.state == "LeaderBoard":
                self.cursor_rect.midtop = (self.customcardsx + self.offset, self.customcardsy)
                self.state = "CustomCards"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = "LeaderBoard"
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.settingsx + self.offset, self.settingsy)
                self.state = "Settings"

    def check_input(self):
        self.move_cursor()  #player moving cursor
        # player selects a state to other menu
        # take them to next screen
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.playing = True
            elif self.state == 'Exit':
                self.game.playing = True 
            self.run_display = False# so when player selects teh start key, it will tell menu to stop displaying





