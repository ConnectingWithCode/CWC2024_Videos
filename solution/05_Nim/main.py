import play
import random


play.new_image("christmas_background.png")

# Select first player and position player button
if random.randint(1, 2) == 1:
    player_button = play.new_image("P1Button.png", size=80, x=-275, y=-240)
    player_button.is_player_one_turn = True
else:
    player_button = play.new_image("P2Button.png", size=80, x=275, y=-240)
    player_button.is_player_one_turn = False


# Function to move player button to correct position and change image
def update_player_button():
    if player_button.is_player_one_turn:
        player_button.image = "P1Button.png"
        player_button.x = -275
    else:
        player_button.image = "P2Button.png"
        player_button.x = 275


PENGUIN = 0
POLARBEAR = 1
SEAL = 2


# Multidimensional array to store rows of images
images = [[], [], []]


# Places a copy of an image in the designated x,y position.
def place_image(obj_type, x_location, y_location):
    if obj_type == PENGUIN:
        obj = play.new_image("penguin.png", size=18, x=x_location, y=y_location)
    if obj_type == POLARBEAR:
        obj = play.new_image("polarbear.png", size=16, x=x_location, y=y_location)
    if obj_type == SEAL:
        obj = play.new_image("seal.png", size=13, x=x_location, y=y_location)
    obj.has_x = False
    images[obj_type].append(obj)


# Coordinates the placement of rows of images with appropriate spacing
def place_row_of_images(obj_type, y_location, quantity):
    spacing = 100
    x = -spacing * ((quantity - 1) / 2)
    for _ in range(quantity):
        place_image(obj_type, x, y_location)
        x += spacing


# Handles the placement of images for all three rows
place_row_of_images(PENGUIN, -100, random.randint(3, 8))
place_row_of_images(POLARBEAR, 0, random.randint(3, 8))
place_row_of_images(SEAL, 100, random.randint(3, 8))


# Toggling, as appropriate, from images with and without an X
def update_images():
    for sprite in images[PENGUIN]:
        if sprite.has_x:
            sprite.image = "penguinX.png"
        else:
            sprite.image = "penguin.png"
    for sprite in images[POLARBEAR]:
        if sprite.has_x:
            sprite.image = "polarbearX.png"
        else:
            sprite.image = "polarbear.png"
    for sprite in images[SEAL]:
        if sprite.has_x:
            sprite.image = "sealX.png"
        else:
            sprite.image = "seal.png"


# Our main game loop that looks for mouse clicks and responds accordingly
@play.repeat_forever
def forever_loop():
    if play.mouse.is_clicked:
        # go through each row and look at each image to determine which row is "active" (only one allowed for game play)
        selected_row = -1
        for k in range(3):
            for sprite in images[k]:
                if sprite.is_clicked:
                    sprite.has_x = not sprite.has_x
                    selected_row = k
        # if there is a selected row, remove X's from images in other remaining rows
        if selected_row != -1:
            for k in range(3):
                if selected_row != k:
                    for sprite in images[k]:
                        sprite.has_x = False
        # if player button clicked, count remaining images and determine if any need to be hidden
        if player_button.is_clicked:
            images_remaining = 0
            image_selected = False
            for k in range(3):
                for sprite in images[k]:
                    if sprite.has_x and sprite.is_shown:
                        image_selected = True
                        sprite.hide()
                    elif sprite.is_shown:
                        images_remaining += 1
            # check for win, toggle player if game continues
            if image_selected and images_remaining > 0:
                player_button.is_player_one_turn = not player_button.is_player_one_turn
                update_player_button()
            elif images_remaining == 0:
                if player_button.is_player_one_turn:
                    play.new_text("Player 1 WINS!")
                else:
                    play.new_text("Player 2 WINS!")

        update_images()


play.start_program()
