
def app_employ(bot, app):
    bot.input = app.pre(bot.input)
    bot.output = app.post(bot.output)
    return bot
