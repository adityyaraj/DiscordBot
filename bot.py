import discord
import os

client = discord.Client()


@client.event
async def on_ready():
 print('Now Discord has a {0.user} who talks'.format(client))
    

@client.event
async def on_message(message):  
  if message.author == client.user:
    return

  if message.content.startswith('WerePig'):
      await message.channel.send ('Hi I am a hippo What can I do for you')
  if message.content.startswith('who is hippo'):
    await message.channel.send ('I am Hippo')
  if message.content.startswith('play hippo song'):
    await message.channel.send ("I want a hippopotamus for Christmas Only a hippopotamus will do I don't want a doll, no dinky Tinkertoy I want a hippopotamus to play with and enjoy I want a hippopotamus for Christmas I don't think Santa Claus will mind, do you? He won't have to use our dirty chimney flue Just bring him through the front door  That's the easy thing to do I can see me now on Christmas morning Creeping down the stairs Oh, what joy and what surprise When I open up my eyes To see my hippo hero standing there I want a hippopotamus for Christmas Only a hippopotamus will do No crocodiles, or rhinoceroseses I only like hippopotamuseses And hippopotamuses like me too I want a hippopotamus for Christmas A hippopotamus is all I want Mom says the hippo would eat me up But then teacher says a hippo is a vegetarian I want a hippopotamus for Christmas The kind I saw this summer at the zoo There's lots of room for him in our two car garage I'd feed him there and wash him there And give him his massage I can see me now on Christmas morning Creeping down the stairs Oh, what joy and what surprise When I open up my eyes To see my hippo hero standing there I want a hippopotamus for Christmas Only a hippopotamus will do No crocodiles, or rhinoceroseses I only like hippopotamuses And hippopotamuses like me too")
 
  if message.content.startswith('what do you do for living'):
      await message.channel.send ("I use to   sell  ....Humm you that know that   .........................................................................................Guess................................................................................................................................................................................can't guess try again ...............chamanprash")
  
  if message.content.startswith('what is your favourite animal'):
      await message.channel.send ('dariyaee haathee gaddhe')
  
  if message.content.startswith('what is your favourite movie'):
    await message.channel.send ('Ninteen Shades Of hippo')

  if message.content.startswith('which movie is that'):
    await message.channel.send ('its a hippo movie not for humans')

  if message.content.startswith('ok 19 hippo'):
    await message.channel.send ('dont go on its name a good movie not like human one')

  if message.content.startswith('where do you live'):
    await message.channel.send ('what will you do knowing where do i live will you send me macbook ')
  
  if message.content.startswith('klaus'):
    await message.channel.send ('he is an original')

  if message.content.startswith('klaus is standing in your back'):
    await message.channel.send ('What... no no...no..Help! I am Sorry')
 
  if message.content.startswith('bhak hippo'):
    await message.channel.send ('bhak bsdk')

  if message.content.startswith('bye'):
    await message.channel.send ('Bye see you later')

  if message.content.startswith('help'):
    await message.channel.send ("what's the problem")  
  
  if message.content.startswith('how are you'):
    await message.channel.send ('Fine Thanks For Asking') 

  if message.content.startswith('how are you'):
    await message.channel.send ('Fine Thanks For Asking')

  if message.content.startswith('hello'):
    await message.channel.send ('hi') 
  
  if message.content.startswith('hello'):
    await message.channel.send ('https://tenor.com/view/hello-its-me-hippo-gif-9986881')   
 
  if message.content.startswith('fuck'):
    await message.channel.send ('Fuck off')
  
  if message.content.startswith('fuck you'):
    await message.channel.send ('fuck off')
 
  if message.content.startswith('fuck off'):
    await message.channel.send ('fuck off u bloody bastard fuck u ')

  if message.content.startswith('hi'):
    await message.channel.send ('hi')   
  
  if message.content.startswith('Happy New Year'):
    await message.channel.send ('Happy New Year')  
client.run(os.getenv('hippoa'))
