import play

play.new_image("christmas_background.png")

#                 0               1                 2
p1_images = ["p1_frosty.png", "p1_santa.png", "p1_rudolph.png"]
p2_images = ["p2_frosty.png", "p2_santa.png", "p2_rudolph.png"]

player1 = play.new_image(p1_images[2], size=50, x=-200, y=-50)
player1.costume = 0
player1.score = 0

player2 = play.new_image(p2_images[2], size=50, x=200, y=-50)
player2.costume = 0
player2.score = 0

countdown = play.new_text("3", size=400, y=100, color="blue")
countdown.hide()

p1_text = play.new_text("", y=200, x=-200)
p2_text = play.new_text("", y=200, x=200)


def update_scores():
    p1_text.words = f"Score: {player1.score}"
    p2_text.words = f"Score: {player2.score}"


update_scores()


def update_costumes():
    player1.image = p1_images[player1.costume]
    player2.image = p2_images[player2.costume]
    player1.show()
    player2.show()


update_costumes()


@play.when_any_key_pressed
async def start_round(key):
    if key == "space":
        player1.hide()
        player2.hide()
        countdown.show()
        await play.timer(seconds=1.0)
        countdown.words = "2"
        await play.timer(seconds=1.0)
        countdown.words = "1"
        await play.timer(seconds=1.0)
        countdown.hide()
        update_costumes()
        score_round()


def score_round():
    if player1.costume == 0 and player2.costume == 1:
        player1.score += 1
    elif player1.costume == 1 and player2.costume == 2:
        player1.score += 1
    elif player1.costume == 2 and player2.costume == 0:
        player1.score += 1
    elif player2.costume == 0 and player1.costume == 1:
        player2.score += 1
    elif player2.costume == 1 and player1.costume == 2:
        player2.score += 1
    elif player2.costume == 2 and player1.costume == 0:
        player2.score += 1
    update_scores()


@play.when_any_key_pressed
def players(key):
    if key == "a":
        player1.costume = 0
    if key == "w":
        player1.costume = 1
    if key == "d":
        player1.costume = 2
    if key == "left":
        player2.costume = 0
    if key == "up":
        player2.costume = 1
    if key == "right":
        player2.costume = 2


play.start_program()
