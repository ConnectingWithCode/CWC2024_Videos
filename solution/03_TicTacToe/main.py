import play

board = play.new_image("board.png", size=45)
board.winner = "-"  # Values:   "-" "X" "O" "T"
board.turn = "X"  # Values:   "X" "O"

message = play.new_text("X's Turn", y=220, font_size=80)
new_game = play.new_text("", y=-220, color="blue", font_size=40)

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

for mark in marks:
    mark.state = "-"


@new_game.when_clicked
def start_new_game():
    for mark in marks:
        mark.state = "-"
        mark.image = "blank.png"
    board.winner = "-"  # Values:   "-" "X" "O" "T"
    board.turn = "X"  # Values:   "X" "O"
    message.words = "X's Turn"  # On your own change the first player!
    new_game.words = ""


def get_index(x, y):
    round_x = round(x / 100)
    round_y = round(-y / 100)
    return 3 * (round_y + 1) + (round_x + 1)


@board.when_clicked
def board_click():
    index = get_index(play.mouse.x, play.mouse.y)
    if board.turn == "X" and marks[index].state == "-":
        marks[index].image = "x.png"
        marks[index].state = "X"
    elif board.turn == "O" and marks[index].state == "-":
        marks[index].image = "o.png"
        marks[index].state = "O"

    is_full = True
    for k in range(len(marks)):
        if marks[k].state == "-":
            is_full = False
    if is_full:
        board.winner = "T"

    # if (board.turn == marks[0].state
    #         and board.turn == marks[1].state
    #         and board.turn == marks[2].state):
    #     board.winner = board.turn

    # if (board.turn == marks[3].state
    #         and board.turn == marks[4].state
    #         and board.turn == marks[5].state):
    #     board.winner = board.turn

    if ((board.turn == marks[0].state
         and board.turn == marks[1].state
         and board.turn == marks[2].state)
            or (board.turn == marks[3].state
                and board.turn == marks[4].state
                and board.turn == marks[5].state)
            or (board.turn == marks[6].state
                and board.turn == marks[7].state
                and board.turn == marks[8].state)
            or (board.turn == marks[0].state
                and board.turn == marks[3].state
                and board.turn == marks[6].state)
            or (board.turn == marks[1].state
                and board.turn == marks[4].state
                and board.turn == marks[7].state)
            or (board.turn == marks[2].state
                and board.turn == marks[5].state
                and board.turn == marks[8].state)
            or (board.turn == marks[0].state
                and board.turn == marks[4].state
                and board.turn == marks[8].state)
            or (board.turn == marks[6].state
                and board.turn == marks[4].state
                and board.turn == marks[2].state)):
        board.winner = board.turn

    if board.winner == "X":
        message.words = "The Winner is X!"
        board.turn = "-"
    elif board.winner == "O":
        message.words = "The Winner is O!"
        board.turn = "-"
    elif board.winner == "T":
        message.words = "Tie Game"
        board.turn = "-"
    elif board.turn == "X":
        board.turn = "O"
        message.words = "O's Turn"
    elif board.turn == "O":
        board.turn = "X"
        message.words = "X's Turn"

    if board.turn == "-":
        new_game.words = "New Game"


play.start_program()
