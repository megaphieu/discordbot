import os
import discord
import random
from replit import db

sender_id = ""
card_list = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,10,10,10,10]
my_card = []
is_playing = False
on_hand = 0
dealer_hand = 0

TOKEN = os.getenv('TOKEN')
client = discord.Client()
channel_id = 837607193557073931

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  print('Loaded database:\nid\t\t\t\t\tP-Coins')
  for i in db.keys():
    print(f'{i}\t{db[i]}')
  await client.get_channel(channel_id).send(f'{client.user} activated!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  id_ThanhMap = 617336626691178498
  id_lozAx = 640707930072809481
  # id_Quang = 140856315877654528

  message_content = message.content.lower().strip()

  # CHUNG
  if message_content == "u gei":
    await message.channel.send('no, u')

  ### BLACKJACK ###
  global sender_id
  global card_list
  global my_card
  global is_playing
  global dealer_card

  # START GAME
  if message_content.startswith('blackjack') and client.user.mentioned_in(message) and is_playing==False:
    
    is_playing = True
    sender_id = str(message.author.id)

    if sender_id not in db.keys():
      db[sender_id] = 1000

    await message.channel.send(f"{message.author.mention}'s account currently have {db[sender_id]} P-Coin(s). Default bet is 100.")

    my_card=random.sample(card_list,2)

    await message.channel.send(f'Game start!')
    await message.channel.send(f'On hand: {my_card}\nTotal: {sum(my_card)}')
    await message.channel.send('Choose: Hit or Stay?')

  # HIT
  if message_content=='hit' and is_playing==True:
    my_card.append(random.choice(card_list))
    await message.channel.send(f'on hand: {my_card}, total: {sum(my_card)}')
    if sum(my_card)>21:
      db[sender_id]-=100
      await message.channel.send(f'BUSTED! Better luck next time ;)\n-100 P-Coins (remaining: {db[sender_id]})')
      is_playing=False
    if sum(my_card)==21:
      db[sender_id]+=150
      await message.channel.send(f'BLACKJACK! Very niceee :>\n+150 P-Coins (remaining: {db[sender_id]})')
      is_playing=False
    if sum(my_card)<21:
      await message.channel.send('Choose: Hit or Stay?')

  # STAY
  if message_content=='stay' and is_playing==True:
    dealer_card = random.sample(card_list,2)
    while sum(dealer_card) < sum(my_card):
      dealer_card.append(random.choice(card_list))
    await message.channel.send(f'On hand: {my_card}\nTotal: {sum(my_card)}')
    await message.channel.send(f'Dealer hand: {dealer_card}\nTotal: {sum(dealer_card)}')

    if sum(dealer_card) > sum(my_card) and sum(dealer_card) <= 21:
      db[sender_id]-=100
      await message.channel.send(f'U LOSE! Better luck next time ;)\n-100 P-Coins (remaining: {db[sender_id]})')
    if sum(dealer_card) < sum(my_card) or sum(dealer_card) > 21:
      db[sender_id]+=100
      await message.channel.send(f'U WIN!:3\n+100 P-Coins (remaining: {db[sender_id]})')
    if sum(dealer_card) == sum(my_card):
      await message.channel.send('DRAW :v')
      
    is_playing=False

  # EVERY1
  if message.author.id != id_lozAx and message.author.id != id_ThanhMap:
    # Mentioned
    if client.user.mentioned_in(message) and not message_content.startswith('blackjack'):
      await message.channel.send('nani!?')

    # Starts with
    if message_content.startswith('xin chào') or message_content.startswith('hello'):
      await message.channel.send(f'Chào, {message.author.mention}. Tôi có quen bạn đấy :))')

    if message_content.startswith('clm'):
      await message.channel.send('clm :))')

    if message_content.startswith('cax'):
      await message.channel.send('lozz dô dăn hóe ;)')

    if message_content.startswith('loz'):
      await message.channel.send('chửi thề con cẹc, bắn mầy á :))')

    # Exactly equals
    if message_content=='.':
      await message.channel.send('.')

  # THG AXAXX
  if message.author.id == id_lozAx:
    await message.channel.send('adu, ax online kìa ae !!')

  # LOZZ THANH MAP
  if message.author.id == id_ThanhMap:
    # Mentioned
    if client.user.mentioned_in(message):
      await message.channel.send('ghiền :))')

    # Starts with
    if message_content.startswith('xin chào') or message_content.startswith('hello'):
      await message.channel.send(f'Xin chào, {message.author.mention}. Vâng, tôi có quen bạn đấy :))')

    if message_content.startswith('clm'):
      await message.channel.send('clm :))')

client.run(TOKEN)
