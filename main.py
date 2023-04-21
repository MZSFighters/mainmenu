from game import Game

g = Game()
# we have two loops now
#outer loop
while g.running:
    #g.playing = True
    g.curr_menu.display_menu()
    g.game_loop() #inner loop



