import play
import random

play.new_image("forest.png", size=85)

play.new_text("Coin Collector",
              y=200,
              font_size=100)

hero = play.new_image("piggy_facing_right.png", x=0, y=-200, size=20)
hero.is_game_over = False
hero.balance = 0
hero.target = random.randint(30, 120)

scoreboard = play.new_text(
  f"Balance = {hero.balance}   Target = {hero.target}",
  x=0,
  y=100,
  font_size=50,
  color='purple')

@play.repeat_forever
def forever_loop():
    pass

@play.repeat_forever
def control_hero():
    if hero.is_game_over:
        return
    if play.key_is_pressed("left", "a"):
        hero.x = hero.x - 15
        hero.image = "piggy.png"
    elif play.key_is_pressed("right", "d"):
        hero.x = hero.x + 15
        hero.image = "piggy_facing_right.png"

falling_coins = []

coin_images = ["penny.png", "nickel.png", "dime.png", "quarter.png", "theif.png"]
coin_values = [1, 5, 10, 25, -1]

def generate_coin():
    coin_index = random.randint(0,4)
    coin_filename = coin_images[coin_index]

    coin = play.new_image(coin_filename,
                          x=random.randint(-300, 300),
                          y=600,
                          size=35)
    coin.value = coin_values[coin_index]
    falling_coins.append(coin)

@play.repeat_forever
async def create_objects():
    if hero.is_game_over:
        return
    generate_coin()
    await play.timer(seconds=2)

@play.repeat_forever
def coin_falling():
    if hero.is_game_over:
        scoreboard.words = "YOU WIN!!!"
        scoreboard.font_size = 100
        return
    for coin in falling_coins:
        coin.y = coin.y - 4
        if coin.is_touching(hero):
            if coin.value == -1:
                hero.balance = 0
            else:
                hero.balance += coin.value
            if hero.balance == hero.target:
                hero.is_game_over = True
            scoreboard.words = f"Balance = {hero.balance}   Target = {hero.target}"
            falling_coins.remove(coin)
            coin.remove()
        elif coin.y < -225:
            falling_coins.remove(coin)
            coin.remove()

play.start_program()
