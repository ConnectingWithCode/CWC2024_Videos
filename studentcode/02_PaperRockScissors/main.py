import play


@play.when_any_key_pressed
async def start_round(key):
    pass


@play.when_any_key_pressed
def players(key):
    pass


play.start_program()
