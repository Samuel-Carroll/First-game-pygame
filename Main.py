# noinspection PyUnresolvedReferences
import pgzrun, random, pygame

WIDTH = 1200

HEIGHT = 620

music.play('default')

char = Actor('char_0_idle')
char_0.x = 600
char_0.y = 570

char_0 = Actor('char_0_idle')
char_0.x = 150
char_0.y = 180

char_1 = Actor('char_1_idle')
char_1.x = 350
char_1.y = 180

char_2 = Actor('char_2_idle')
char_2.x = 550
char_2 = 180
bounce = False


char_3 = Actor('char_3_idle')
char_3.x = 750
char_3.y = 180
c_char_3 = False


char_4 = Actor('char_4_idle')
char_4.x = 950
char_4.y = 180

fish = Actor('fish')
store = []



#start screen var
start_screen = True
#if we want to run out main game code
run = False
#character select screen
character_menu = False
#music select screen
music_screen = False


state = 0

reset = 0

state_images = [
    "right",
    "left"
]

#varibales that deal with player movement
isJump = False
jumpCount = 10
left = False
right = True
vel = 10
#variables for the fish
fall = 5
time_delay = 1000
#whether to drop a fish or not
drop = False
#start of fish drop
start = True
#players score
score = 0
#amount of player lives
lives = 5
#checks to end the game
end_game = False
#Time delay to Jump again
delay = 500

#Jump variable 1
j_var1 = 0.7
j_var2 = 0.9

title = 'cat hopper'
#start button
start_button = Actor('start')
start_button.x = 600
start_button.y = 240

#go again button
cont_button = Actor('again')
cont_button.x = 600
cont_button.y = 50

#characters button
character_select = Actor('characters')
character_select.x = 600
character_select.y = 300

#back buttond
back = Actor('back')
back.x = 100
back.y = 40

#music_button
music_button = Actor('music')
music_button.x = 600
music_button.y = 360

#button
default_music = Actor('default')
default_music.x = 150
default_music.y = 250

#button
music_0 = Actor('music_0')
music_0.x = 150
music_0.y = 300

def place_fish():
    fish.x = random.randint(50, 1150)

def on_mouse_down(pos):
    global run, start_screen, lives, vel, end_game, score, fall, start, character_menu, char_0, char_1, state_images, char_2, music_screen, c_char_3, store, j_var1, j_var2, delay

    if start_button.collidepoint(pos):
        run = True
        start_screen = False

    if cont_button.collidepoint(pos):
        run = False
        start_screen = True
        lives = 5
        vel = 10
        end_game = False
        score = 0
        fall = 5
        start = True
        store = []

#Character select screen press
    if character_select.collidepoint(pos):
        run = False
        start_screen = False
        music_screen = False
        character_menu = True
#pressing in the music button
    if music_button.collidepoint(pos):
        run = False
        start_screen = False
        character_menu = False
        music_screen = True
#pressing on the Music option buttons
    if default_music.collidepoint(pos):
        music.play('default')
    if all_star.collidepoint(pos):
        music.play('music_0')

# pressing on the char0 Icon
    if char_0_icon.collidepoint(pos):
        char = Actor('idle')
        state_images = [
            "right",
            "left"
        ]
        bounce = False
        c_char_3 = False
        j_var1 = 0.7
        j_var2 = 0.9
        delay = 500
# pressing on the char1 Icon
    if char_1.collidepoint(pos):
        char = Actor('char_1_idle')
        state_images = [
            "1_left",
            "1_right"
        ]
        bounce = False
        c_char_3 = False
        j_var1 = 0.7
        j_var2 = 0.9
        delay = 450
# pressing on the char2 Icon
    if char_2.collidepoint(pos):
        char = Actor('char_2_idle')
        state_images = [
            "2_right",
            "2_left"
        ]
        bounce = True
        c_char_3 = False
        j_var1 = 0.5
        j_var2 =1
        delay = 10
# Pressing on char3 Icon
    if char_3.collidepoint(pos):
        char = Actor('char_3_idle')
        state_images = [
            "3_right",
            "3_left"
        ]
        bounce = False
        c_char_3 = True
        j_var1 = 1
        j_var2 = 0.7
        delay = 1000
# pressing on char4 Icon
    if char_4.collidepoint(pos):
        char = Actor("char_4_idle")
        state_images =[
            "4_right",
            "4_left"
        ]
        bounce = False
        c_char_3 = False
        j_var1 = 0.7
        j_var2 = 0.9
        delay = 500

    if back.collidepoint(pos):
        start_screen = True
        character_menu = False
        music_screen = False

def draw():
    if start_screen:
        screen.clear()
        screen.blit('menu_backdrop', (0,0))
        screen.blit(title, (0, 0))
        char.draw()
        start_button.draw()
        character_select.draw()
        music_button.draw()

    if character_menu:
        screen.clear()
        screen.blit('menu_backdrop', (0, 0))
        back.draw()
        #Drawing all the character icons
        char_0.icon.draw()
        char_1.draw()
        char_2.draw()
        char_3.draw()
        char_4.draw()
        char.x = 600
        char.y = 570
    #drawing the Music screen
    if music_screen:
        screen.clear()
        screen.blit('menu_backdrop', (0, 0))
        back.draw()

        default_music.draw()
        all_star.draw()

    if run:
        screen.clear()

        screen.blit('forest', (0, -55))

        cat.image = state_images[state]
        cat.draw()
        #drawing the fish
        for i in range(0, len(store)):
            store[i].draw()

        screen.draw.text("Score: " + str(score), (15, 5))
        screen.draw.text("Lives: " + str(lives), (1020, 5))
        #END GAME MESSAGE
        if end_game:
            screen.draw.text("YOU LOSE!", (540, 310))
            cont_button.draw()



def update():
    global state, neg, jumpCount, isJump, vel, left, right, reset, jumpReady, time_delay, drop, start, score, \
        fall, lives, end_game, boost, is_boost, boost_end, boss_fight, char, run, state_images, store

#move right
    if run:
        if keyboard.d and char.x < 1140:
            state = 0
            char.x += vel
            right = True
            left = False
    #move left
        if keyboard.a and char.x > 50:
            state = 1
            char.x -= vel
            right = False
            left = True
    #jump code

        if not(isJump) and pygame.time.get_ticks() - reset > delay:
            if keyboard.SPACE:
                isJump = True
                right = False
                left = False
                jump = True
                if not c_char_3:
                    vel = 15
                if c_char_3:
                    vel = 26
                reset = pygame.time.get_ticks()
        if isJump:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                char.y -= (j_var1*jumpCount ** 2) * j_var2 * neg
                jumpCount -= 1
            else:
                isJump = False
                if not c_char_3:
                    vel = 10
                if c_char_3:
                    vel = 7
                jumpCount = 10

    #Fish spawner
        if start:
            store.append(fish)
            place_fish()
            drop = True
            start = False
        if drop:
            fish.y += fall
    #Getting rid of fish if they hit screen border

        if fish.y > 620:
            store.pop(0)
            drop = False
            start = True
            fish.y = 0
            lives = lives-1
            if not c_char_3:
                sounds.miss.play()
            else:
                sounds.miss2.play()
    #Hit detection for Fish and Cat
        for i in range(len(store)):
            if char.colliderect(store[i]):
                store.pop(i)
                drop = False
                start = True
                fish.y = 0
                score = score+1
    #Char Lives
        if lives == 0:
            start = False
            drop = False
            end_game = True
    #levels of the game
        if score > 10:
            fall = 6
        if score > 20:
            fall = 7.5
        if score > 30:
            fall = 8
        if score > 40:
            fall = 9
        if score > 50:
            fall = 10



pgzrun.go()












