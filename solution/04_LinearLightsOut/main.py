import play
import random

game = play.new_image("background.png", size=84)
game.counter = 0

play.new_text("Linear Lights Out", y=200, font_size=100)

message = play.new_text("Turn all of the lights off!",
                        y=100,
                        font_size=50,
                        color='grey')

light_images = ["light_off.png", "light_on.png"]
light_list = []

for k in range(7):
    value = random.randint(0, 1)
    light = play.new_image(light_images[value],
                           x=-300 + k * 100,
                           y=0,
                           size=75)
    if value == 0:
        light.is_on = False
    else:
        light.is_on = True
    light.num = k
    light_list.append(light)


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


@play.repeat_forever
async def control_lights():

    # See if the game is over
    is_game_over = True
    for light in light_list:
        if light.is_on:
            is_game_over = False

    if is_game_over:
        message.words = f"You won in {game.counter} moves!"
        message.show()
        return

    # Not over?  Keep playing.
    for light in light_list:
        if play.mouse.is_clicked:
            if play.mouse.is_touching(light):
                button_press(light.num)
                game.counter += 1
                message.words = f"Moves: {game.counter}"
                await play.timer(seconds=0.25)


def toggle_light(light):
    if light.is_on:
        light.image = light_images[0]
        light.is_on = False
    else:
        light.image = light_images[1]
        light.is_on = True


play.start_program()
