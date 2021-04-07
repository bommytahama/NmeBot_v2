#so uh v2
#while trying to remove unneeded libraries, i may have broke something in v1
#i wasnt able to edit installed libraries at all and it kept returning library errors on startup
#so this was the solution...oops

#-------------------------------------

#bot for our private discord NME (Noose Maniacs)
#join here: https://discord.com/invite/mjxC8M2 <3
#trash star beat the odds

#2 DO:
#roles txt (idk lol)
#floppa gif when someone says floppa
#maybe fix nami timer again
#organise (both code and stupid fucking comments)

import keep_alive
from discord.ext import tasks
import asyncio
import random
from PIL import Image, ImageFont, ImageDraw
import discord
import os
import time
import joinboice
import weatherloop
#from pyowm import OWM
#import namiping

exec(open("joinboice.py").read())
#exec(open("namiping.py").read())
exec(open("weatherloop.py").read())

#light blue: (135, 206, 250)
#pink: (255, 192, 203)
#dark(?) pink: (219, 112, 147)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
testingid = 815405711726084156  #testing server
target_channel_id = 815084936985706506  #noose maniacs server
general_id = 725245718750822411  #t_n general chat
general_idd = 773783347067486258  #nomral general
lastmes_id = 822725428833550366
tbanned_ids = [725245717865693224, 776529380405936128]

msg = ''
wordsfile = open('20k_words.txt', 'r')
wordlist = []
for line in wordsfile:
    stripped_line = line.strip()
    wordlist.append(stripped_line)
wordsfile.close()


def filewriteg(filename, time_now, timertime):
    timefile = open(filename, "r+")
    timefile.truncate()
    timefile.writelines(str(time_now) + '\n' + str(timertime))
    timefile.close()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    #print(client.guilds[0].roles[5].name)
    global guilds_and_roles
    #global tchannel_ids
    tchannel_ids = []
    guilds_and_roles = {}
    for guildd in client.guilds:
        for channell in guildd.text_channels:
            tchannel_ids.append(channell.id)

    for id in tbanned_ids:
        tchannel_ids.remove(id)
    #print(tchannel_ids)

    global lastmes_dict
    lastmes_dict = {}
    for idd in tchannel_ids:
        ttchannel = client.get_channel(idd)
        ttchannel_lastmesid = ttchannel.last_message_id
        lastmes_dict[str(idd)] = ttchannel_lastmesid
    #print(guilds_and_roles)
    #await role_stuff.start()
    #print('abced'.find('b'))


# rev_e = rev.partition('<')[0]
#print('<' + rev_e[::-1])
#await client.get_channel(815405711726084156).send('<' + rev_e[::-1])
#print(thing.content[::-1])

#in my arms i leave my life for yours
#i go on to live so many moooooore


class role_stuff(object):
    def __init__(self, mm):  #mm is member
        self.mm = mm
        self.rolelist = []
        for r in self.mm.roles:
            self.rolelist.append(r.id)
        del self.rolelist[0]



@client.event
async def on_message(message):
    #if message.author == client.user:
    #return
    #if message.author.id == 467408259414753283:
      #await message.channel.send('<:wyzzz:805564173937147940>')

    if message.channel.id in tbanned_ids:
        return

    chance = random.randint(0, 50000)
    if chance == time.gmtime().tm_wday:
        return_mes = ''
        for i in range(1, random.randint(1, 26)):
            return_mes += '<:asoingbobcry:807347515104034887>'
        await message.channel.send(return_mes)
        return

    global lastmes_dict

    if not (message.content.startswith('$addreaction')
            or len(message.content) <= 0) or len(message.attachments) > 0:
        #print(message.content)
        lastmes_dict[str(message.channel.id)] = message.id
        #print(lastmes_id)

    if message.author.bot:
        return

    def cheadle_com():
        cheadlewotd()

    def time_left(input_nowtime, input_waitime):
        nowtsec = time.time()
        elapsed = nowtsec - input_nowtime
        timeleft = input_waitime - elapsed
        return str(int(timeleft))

    def filereadtimes(filename_):
        timefile = open(filename_, 'r')
        linelist = timefile.readlines()
        #ini_string[:-(len(sstring))]
        nowtimev1 = linelist[0]
        timer = float(linelist[1])
        timefile.close()
        nowtime = float(nowtimev1[:-(2)])
        return [nowtime, timer]

    def read_return_time(file_name):
        l = filereadtimes(file_name)
        r = time_left(l[0], l[1])
        return r

    #so call me when the world looks bleak
    #i love you but its hard to believe
    #with every day will start to seem
    #the rest is metamodernity

    def ping_pong(input_message):
        if message.author.bot:
            return
        #print mystr[mystr.find(char1)+1 : mystr.find(char2)]
        input_message_new = ''
        dont_t = ''
        if '<' in input_message and '>' in input_message:
            dont_t_start = input_message.find('<')
            dont_t = input_message[dont_t_start:input_message.find('>') +
                                   1].upper()
            input_message_new = input_message.upper().replace(dont_t, '&-&-&')
        else:
            input_message_new = input_message.upper()
        rm1 = input_message_new.replace('ing'.upper(), '&&-&')
        rm1 = rm1.replace('ong'.upper(), '&&&')
        rm1 = rm1.replace('&&-&', 'ong')  #this is so fucking awful oh my god
        rm1 = rm1.replace('&&&', 'ing')  #2 DO: FIX THIS!!!!
        rm1 = rm1.replace('&-&-&', dont_t)
        return_message = rm1.lower() + " :ping_pong:"
        return return_message

    async def send_message(input_message, output):
        await input_message.channel.send(output)

    async def send_filec(input_message, output):
        cheadle_com()
        await input_message.channel.send(file=output)

    async def join_channel(input_message):
        await join_song_com(input_message.author.voice.channel.id,
                            input_message.content[len('$joinvoice '):])

    async def get_emoji(message_e):
        return_e = message_e.content[(len('$addreaction')) + 1:]
        return return_e

    async def react(message_r, message_t_id):
        emoji = await get_emoji(message_r)
        message_t = await message_r.channel.fetch_message(message_t_id)
        #print(emoji)
        await message_t.add_reaction(emoji)
        await message.delete()

    def weather_yeah(city):
        try:
            template_weather = weatherloop.weathermessage.format(
                *weatherloop.get_weather_things(city))
        except:
            city = 'Boston, US'
            template_weather = weatherloop.weathermessage.format(
                *weatherloop.get_weather_things(city))
        return template_weather

    command_dict = {
        '$allroles': [send_message, [message, str(guilds_and_roles)[:2000]]],
        '$weather':
        [send_message, [message, weather_yeah(message.content[9:])]],
        '$cheadle': [send_filec, [message, discord.File("result.jpg")]],
        '$echo ': [send_message, [message, message.content[6:]]],
        '$chance': [send_message, [message,
                                   str(chance) + ' out of 50000']],
        '$words': [send_message, [message,
                                  str(len(wordlist)) + ' words']],
        '$timeleftcheadle':
        [send_message, [message,
                        time_left(tsecc, wtimec) + ' seconds']],
        '$voicetimer': [
            send_message,
            [message, read_return_time('jointime.txt') + ' seconds']
        ],
        '$lensonglist':
        [send_message, [message,
                        str(len(joinboice.songlist)) + ' songs']],
        '$joinvoice': [join_channel, [message]],
        '$namitime': [
            send_message,
            [message, read_return_time('namitime.txt') + ' seconds']
        ],
        #'$mmmmtime': [send_message, [message, time_left(tsec_mmmm ,wait_mmmm) + ' seconds mmmm']],
        '$addreaction ':
        [react, [message, lastmes_dict[str(message.channel.id)]]],
        '$mesdict': [send_message, [message, lastmes_dict]],
        'mm': [send_message, [message, mmmm()]],
        'ping': [send_message, [message,
                                ping_pong(str(message.content))]],
        'pong': [send_message, [message,
                                ping_pong(str(message.content))]],
    }

    command_namelist = list(command_dict)

    #command_arglist = [
    #    [message, str(len(wordlist)) + ' words'],
    #    [message, time_left(tsecc, wtimec) + ' seconds'],
    #    [message, read_return_time('jointime.txt') + ' seconds'],
    #    [message, ping_pong(str(message.content))],
    #    [message, str(len(joinboice.songlist)) + ' songs'], [message],
    #    [message, read_return_time('namitime.txt') + ' seconds'],
    #    [message, mmmm()], [message, lastmes_dict[str(message.channel.id)]], #[message, time_left(tsec_mmmm ,wait_mmmm) + ' seconds mmmm'], [message, #lastmes_dict]
    #]

    for command in command_namelist:
        if command.upper() in message.content.upper():
            #print('test')
            if 'JAH' in message.content.upper():
                pass
            else:
                banned_2 = ['c', 's']
                banned_3 = ['i', 'ee', 'ea']
                banned_4 = ['c', 'k', 'ck', 's']
                banned_5 = ['a', 'ah', 'u', 'uh']
                for word2 in banned_2:
                    for word3 in banned_3:
                        for word4 in banned_4:
                            for word5 in banned_5:
                                fullword = word2 + word3 + word4 + word5
                                if fullword.upper() in message.content.upper():
                                    return_message = 'shut up higg'
                                    await message.channel.send(return_message)
                                    return
            command_args = command_dict[command][1]
            try:
                await command_dict[command][0](command_args[0],
                                               command_args[1])
            except:
                await command_dict[command][0](command_args[0])
            return

    #def voice_time():
    #    timefile = open('jointime.txt', 'r')
    #    linelist = timefile.readlines()
    #    #ini_string[:-(len(sstring))]
    #    nowtimev1 = linelist[0]
    #    timer = float(linelist[1])
    #    timefile.close()
    #    nowtimev = float(nowtimev1[:-(2)])
    #    nowtsecv = time.time()
    #    elapsedv = nowtsecv - nowtimev
    #    timeleftv = timer - elapsedv
    #    await message.channel.send(str(int(timeleftv)) + ' seconds')
    ##if message.content == 'ping' or message.content == 'ping :ping_pong:':
    ##await message.channel.send('pong :ping_pong:')
    #if message.content.startswith('ping'):
    #    #banned_words = [
    #     kiss kiss kiss a fantasyyy
    #      lay down with me, valerieeee
    #        #'cica', 'seecuh', 'seecah', 'sicuh', 'sicah',
    #        #' cica', ' seecuh', ' seecah', ' sicuh',
    #       # ' sicah', 'seaca', 'sica', ' seaca', ' sica',
    #        #'sicah', ' sicah', 'sicuh', ' sicuh',
    #    #]
    #    return_message = 'pong' + message.content[4:] + ' :ping_pong:'
    #    banned_1 = ['', ' ']
    #    banned_2 = ['c', 's']
    #    banned_3 = ['i', 'ee', 'ea']
    #    banned_4 = ['c', 'k', 'ck']
    #    banned_5 = ['a', 'ah', 'u', 'uh']
    #    for word1 in banned_1:
    #      for word2 in banned_2:
    #        for word3 in banned_3:
    #          for word4 in banned_4:
    #            for word5 in banned_5:
    #              fullword = word1 + word2 + word3 + word4 + word5
    #              if 'jah' in message.content:
    #                break
    #              elif fullword in message.content:
    #                return_message = 'fuck you higg'
    #    #for word in banned_words:
    #        #if message.content.startswith('ping' + word):
    #            #return_message = 'fuck you higg'
    #    await message.channel.send(return_message)
    #    print('ponged')
    #    an angel held me like a child
    #if message.content.startswith('$lensonglist'):
    #    await message.channel.send(len(joinboice.songlist))
    #if message.content.startswith('$joinvoice'):
    #    await join_song_com(message.author.voice.channel.id,
    #                        message.content[11:])
    #    #print(str(message.author.voice.channel.id))
    #if message.content.startswith('$namitime'):
    #    timefilen = open('namitime.txt', 'r')
    #    linelist = timefilen.readlines()
    #    sitting all alone
    #    and you call me on the phone
    #    and you say "i need love,
    #    can you get to me now?"
    #    #ini_string[:-(len(sstring))]
    #    nowtimen1 = linelist[0]
    #    timern = float(linelist[1])
    #    timefilen.close()
    #    nowtimen = float(nowtimen1[:-(2)])
    #    nowtsecn = time.time()
    #    elapsedn = nowtsecn - nowtimen
    #    ntime_left = timern - elapsedn
    #    :D  ^ 3^
    #    await message.channel.send(str(int(ntime_left)) + ' seconds left')

gdict = {}
@client.event
async def on_member_remove(member):
  try:
    gdict[str(member.guild.id)][str(member.id)] = role_stuff(member)
  except KeyError:
    gdict[str(member.guild.id)] = {}
    gdict[str(member.guild.id)][str(member.id)] = role_stuff(member)

@client.event
async def on_member_join(member):
    print('yeah')
    #if str(member.id) in list(gdict[str(member.guild.id)]):
    try:
      for r in gdict[str(member.guild.id)][str(member.id)].rolelist:
        try:
          await member.add_roles(member.guild.get_role(r))
          #print('added ' + member.guild.get_role(r).name)
        except discord.Forbidden:
          print(member.guild.get_role(r).name + ' is forbidden; passed')
          pass
    except KeyError:
      pass #add txt stuff here eventually?
                


#@client.event
#async def on_member_update(before, after):
#    #print(before)
#    #print(before)
#    if before.roles != after.roles:
#        global guilds_and_roles
#        guilds_and_roles[str(after.guild.name)][str(after.name)] = []
#        for role in after.roles:
#            guilds_and_roles[str(after.guild.name)][str(after.name)].append(
#                role.id)
#        #print(guilds_and_roles[str(after.guild.name)][str(after.name)])


def cheadlewotd():
    filename = 'dc_pics/' + str(random.randint(1, 70)) + '.jpg'
    #filename = 'dc_pics/' + str(51) + '.jpg'
    my_image = Image.open(filename)
    with Image.open(filename) as image:
        width, height = image.size
    top_size = width * 0.083
    bot_size = width * 0.17
    color = (135, 206, 250)
    top_font = ImageFont.truetype('impact.ttf', int(top_size))
    bottom_font = ImageFont.truetype('impact.ttf', int(bot_size))
    random_word = wordlist[random.randint(0, len(wordlist) - 1)]
    top_text = "Don Cheadle word of the day"
    bottom_text = random_word
    image_edit = ImageDraw.Draw(my_image)
    image_edit.text((width * 0.0265, -2), top_text, color, font=top_font)
    image_edit.text(
        (
            int(
                width * (0.5 - (0.038 * len(bottom_text)))
            ),  # i literally have                                                                       no idea how this                                                                       works
            int(height - (bot_size * 1.3))),
        bottom_text,
        color,
        font=bottom_font)
    my_image.save("result.jpg")


@tasks.loop()
@client.event
async def timer_shit_fuck():
    global tsecc
    tsecc = time.time()
    t = time.gmtime()
    send_time_l = 7  #am #l = local
    send_time = send_time_l + 7
    global wtimec
    if send_time >= 24:
        send_time -= 24
    if t.tm_hour == send_time and t.tm_min == 0:
        wtimec = 0
    elif t.tm_hour < send_time:
        print('2')
        wtimec = ((60 * 60) * ((send_time - 1) - t.tm_hour)) + (
            (60) * (59 - t.tm_min)) + (60 - t.tm_sec)
    elif t.tm_hour >= send_time:
        print('3')
        wtime1 = ((60 * 60) *
                  (23 - t.tm_hour)) + ((60) *
                                       (59 - t.tm_min)) + (60 - t.tm_sec)
        wtime2 = send_time * 60 * 60
        wtimec = wtime1 + wtime2
    await asyncio.sleep(wtimec)
    print('sending cheadle...')
    cheadlewotd()
    message_channel = client.get_channel(target_channel_id)
    #print(f"Got channel {message_channel}")
    await message_channel.send(file=discord.File('result.jpg'))
    print('cheadle sent')
    await asyncio.sleep(240)


@timer_shit_fuck.before_loop
async def before_timer_shit_fuck():
    await client.wait_until_ready()
    await asyncio.sleep(1)


#@jahtimer.before_loop
#async def before_timer_jahtimer():
#await client.wait_until_ready()
#await asyncio.sleep(1)
# :) <3

#----------------------------------------------------------------------------------------
#------------------------------------$joinvoice------------------------------------------
#----------------------------------------------------------------------------------------

#true_n_general = 802684938381557840  #nme
#testing_id = 815405498412171294  #testing
#doangus = 817632403228196874  #doangus
#yeah that girls disingenuous
#i cant lie shes a genius
#fuck mars we on venus

#vc_id_list = [doangus, true_n_general] #doangus then general
#vc_id_list = [testing_id]

songlistwvol = joinboice.songlistwvol
songlist = list(songlistwvol)


@client.event
async def joinm(boice_channel):
    #global channel
    print(f"Got channel {boice_channel}")
    return await boice_channel.connect()


@client.event
async def leavem(boice_channel, voicec):
    print(f"Leaving channel {boice_channel}")
    await voicec.disconnect()


@client.event
async def playsongm(index, voicec):
    print('playing ' + songlist[index])
    #songindex = random.randint(0, len(songlist) - 1)
    #songindex = 0
    song = songlist[index]
    audio = discord.FFmpegPCMAudio(source="songs/" + song + ".mp3")
    source = discord.PCMVolumeTransformer(audio)
    source.volume = songlistwvol[song]
    voicec.play(source)


@client.event
async def join_song_com(channel_id, index):
    thing = True
    try:
        int(index)
    except ValueError:
        thing = False
    if thing == False or not(int(index) in range(len(songlist))):
        songindex = random.randint(0, len(songlist) - 1)
    else:
        songindex = int(index)
    #songindex = 25
    channeld = client.get_channel(channel_id)
    vcm = await joinm(channeld)
    await asyncio.sleep(1)
    await playsongm(songindex, vcm)
    while vcm.is_playing():
        await asyncio.sleep(0.5)
    await leavem(channeld, vcm)


def mmmm():
    send_string = ''
    for i in range(random.randint(1, 51)):
        send_string += 'm'
    return send_string


@tasks.loop()
@client.event
async def mmmm_loop():
    global wait_mmmm
    global tsec_mmmm
    channel = client.get_channel(general_idd)
    tsec_mmmm = time.time()
    wait_mmmm = random.randint(10, 172800)
    await asyncio.sleep(wait_mmmm)
    #await asyncio.sleep(5)
    await channel.send(mmmm())


@mmmm_loop.before_loop
async def before_mmmm():
    await client.wait_until_ready()
    await asyncio.sleep(1)


#mmmm_loop.start()
timer_shit_fuck.start()  #this sucks
#fuck repl.it
#jahtimer.start()

keep_alive.keep_alive()

client.run(os.getenv('TOKEN'))