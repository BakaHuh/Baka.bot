import hikari
import lightbulb


main = lightbulb.BotApp(token='OTQ1MzM0ODc5MDYxNjcxOTQ2.YhOptg.i03OWyybRYbba9gcJqQHQkpMLCI')

@main.command
@lightbulb.command('hello', 'hello')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  await ctx.respond('hello!')

@main.command
@lightbulb.command('group','it is a group huh')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group(ctx):
  pass


@group.child
@lightbulb.command('Manga','https://mangapill.com')
@lightbulb.implements(lightbulb.SlashSubGroup)
async def Manga(ctx):
  await ctx.respond('https://mangapill.com')


main.run()
 
 



