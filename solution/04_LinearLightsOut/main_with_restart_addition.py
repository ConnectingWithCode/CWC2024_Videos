import play
import random

game = play.new_image("background.png", size=84)
game.counter = 0
game.game_over = False

play.new_text("Linear Lights Out",
              y=200,
              font_size=100)

message = play.new_text("Turn all of the lights off!",
                        y=100,
                        font_size=50,
                        color = 'grey')

light_list = []
light_images = ["light_off.png", "light_on.png"]

# Creates the seven light sprites
for k in range(7):
    light = play.new_image(light_images[0],
                           x=-300 + k * 100,
                           y=0,
                           size=75)
    light.is_on = False
    light.num = k
    light_list.append(light)


def reset_game():
    game.counter = 0
    game.game_over = False
    message.words = "Turn all of the lights off!"
    for k in range(7):
        light_list[k].image = light_images[0]
        light_list[k].is_on = False
    for _ in range(100):
        button_press(random.randint(0,6))
    update_game_over()
    if game.game_over:
        button_press(random.randint(0,6))
        update_game_over()


def button_press(light_num):
    if light_num == 0:
        toggle_light(light_list[light_num])
        toggle_light(light_list[light_num + 1])
    elif light_num == 6:
        toggle_light(light_list[light_num - 1])
        toggle_light(light_list[light_num])
    else:
        toggle_light(light_list[light_num - 1])
        toggle_light(light_list[light_num])
        toggle_light(light_list[light_num + 1])


def update_game_over():
    off_counter = 0
    for light in light_list:
        if not light.is_on:
            off_counter += 1
    if off_counter == len(light_list):
        game.game_over = True
    else:
        game.game_over = False


@play.repeat_forever
async def control_lights():
    if game.game_over:
        message.words = f"You won in {game.counter} moves!"
        if game.counter == 1:
            message.words = f"You won in {game.counter} move!"
        message.show()
        await play.timer(seconds=2)
        message.words = f"New game about to start."
        await play.timer(seconds=2)
        reset_game()
        return
    for light in light_list:
        if play.mouse.is_clicked:
            if play.mouse.is_touching(light):
                button_press(light.num)
                game.counter += 1
                message.words = f"Moves: {game.counter}"
                await play.timer(seconds=0.25)
    update_game_over()


def toggle_light(light):
    if light.is_on:
        light.image = light_images[0]
        light.is_on = False
    else:
        light.image = light_images[1]
        light.is_on = True


reset_game()
play.start_program()

