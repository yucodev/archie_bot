@Bot.command(pass_context=True)
async def random1and10(ctx, number):
    try:
        arg = random.randint(1, int(number))
    except ValueError:
        await Bot.say("Invalid number")
    else:
        await Bot.say(str(arg))
