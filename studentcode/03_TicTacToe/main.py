import play

board = play.new_image("board.png", size=45)

marks = [
    play.new_image("blank.png", x=-100, y=100, size=50),
    play.new_image("blank.png", x=0, y=100, size=50),
    play.new_image("blank.png", x=100, y=100, size=50),
    play.new_image("blank.png", x=-100, y=0, size=50),
    play.new_image("blank.png", x=0, y=0, size=50),
    play.new_image("blank.png", x=100, y=0, size=50),
    play.new_image("blank.png", x=-100, y=-100, size=50),
    play.new_image("blank.png", x=0, y=-100, size=50),
    play.new_image("blank.png", x=100, y=-100, size=50)
]

play.start_program()
