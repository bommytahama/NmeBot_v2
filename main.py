#so uh v2
#while trying to remove unneeded libraries, i may have broke something in v1
#i wasnt able to edit installed libraries at all and it kept returning library errors on startup
#so this was the solution...oops

#-------------------------------------

#bot for our private discord NME (Noose Maniacs)
#join here: https://discord.com/invite/mjxC8M2 <3
#trash star beat the odds

#10/04/21
#complete command rewrite woooooooooooooooooo

#2 DO:
#OUTLINES on text
#db, use for large data analysis (word frequency)
#roles txt (idk lol)
#maybe fix nami timer again
#organise? (whatever dude shit works i dont give a fuck this sucks)

import keep_alive
from discord.ext import tasks, commands
import asyncio
import random
from PIL import Image, ImageFont, ImageDraw
import discord
import os
import time
import joinboice
import weatherloop
import requests
import json
#import anim
#from replit import db

exec(open("joinboice.py").read())
exec(open("namiping.py").read())
exec(open("weatherloop.py").read())

#light blue: (135, 206, 250)
#pink: (255, 192, 203)
#dark(?) pink: (219, 112, 147)

intents = discord.Intents.all()
client = commands.Bot(intents=intents, command_prefix='$')
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


daysdict = {
    '0': 'monday',
    '1': 'tuesday',
    '2': 'wednesday',
    '3': 'thursday',
    '4': 'friday',
    '5': 'saturday',
    '6': 'sunday',
}


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    #print(time.gmtime())
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game(
            'the day is ' +
            daysdict[str(time.gmtime(time.time() - 3600 * 7).tm_wday)]))
    tchannel_ids = []
    for guildd in client.guilds:
        for channell in guildd.text_channels:
            tchannel_ids.append(channell.id)

    for id in tbanned_ids:
        tchannel_ids.remove(id)

    global lastmes_dict
    lastmes_dict = {}
    for idd in tchannel_ids:
        ttchannel = client.get_channel(idd)
        ttchannel_lastmesid = ttchannel.last_message_id
        lastmes_dict[str(idd)] = ttchannel_lastmesid


class role_stuff(object):
    def __init__(self, mm):  #mm is member
        self.mm = mm
        self.rolelist = []
        for r in self.mm.roles:
            self.rolelist.append(r.id)
        del self.rolelist[0]


def time_left(input_nowtime, input_waitime):
    nowtsec = time.time()
    elapsed = nowtsec - input_nowtime
    timeleft = input_waitime - elapsed
    return str(int(timeleft))


def filereadtimes(filename_):
    timefile = open(filename_, 'r')
    linelist = timefile.readlines()
    nowtimev1 = linelist[0]
    timer = float(linelist[1])
    timefile.close()
    nowtime = float(nowtimev1[:-(2)])
    return [nowtime, timer]


def read_return_time(file_name):
    l = filereadtimes(file_name)
    r = time_left(l[0], l[1])
    return r


@client.command(
    help=
    'returns the weather (syntax: $weather [location]) (be sure your location is spelled correctly',
    brief='returns the weather')
async def weather(ctx, *, arg='Boston, US'):
    try:
        location = arg
        template_weather = weatherloop.weathermessage.format(
            *weatherloop.get_weather_things(location))
    except:
        location = 'Boston, US'
        template_weather = weatherloop.weathermessage.format(
            *weatherloop.get_weather_things(location))
    await ctx.channel.send(template_weather)


@client.command(help='cheadle wotd, no arguments', brief='cheadle wotd')
async def cheadle(ctx):
    await ctx.channel.send(file=discord.File(cheadlewotd()))


@client.command(help='echos text after the command', brief='echos')
async def echo(ctx, *, arg='put in something to echo you stupid fuck'):
    await ctx.channel.send(arg)


@client.command(help='wordlist count', brief='wordlist count')
async def words(ctx):
    await ctx.channel.send(str(len(wordlist)) + ' words')


@client.command(help='time until next cheadle in seconds',
                brief='time until next cheadle')
async def timeleftcheadle(ctx):
    await ctx.channel.send(time_left(tsecc, wtimec) + ' seconds')


@client.command(help='time until next voice join in seconds',
                brief='time until next voice join')
async def voicetimer(ctx):
    await ctx.channel.send(read_return_time('jointime.txt') + ' seconds')


@client.command(help='num of sounds for $joinvoice and random joining',
                brief='num of sounds')
async def lensonglist(ctx):
    await ctx.channel.send(str(len(joinboice.songlist)) + ' songs')


@client.command(
    help='joins your current voice channel and plays a random sound/song',
    brief='joins vc')
async def joinvoice(ctx, *, arg=''):
    songlistwvol = joinboice.songlistwvol
    songlist = list(songlistwvol)

    thing = True
    try:
        int(arg)
    except ValueError:
        thing = False
    if thing == False or not (int(arg) in range(len(songlist))):
        songindex = random.randint(0, len(songlist) - 1)
    else:
        songindex = int(arg)
    #songindex = 25
    channeld = client.get_channel(ctx.message.author.voice.channel.id)
    print('joining ' + channeld.name)
    vcm = await channeld.connect()
    await asyncio.sleep(0.3)
    song = songlist[songindex]
    audio = discord.FFmpegPCMAudio(source="songs/" + song + ".mp3")
    source = discord.PCMVolumeTransformer(audio)
    source.volume = songlistwvol[song]
    print('playing ' + song)
    vcm.play(source)
    while vcm.is_playing():
        await asyncio.sleep(0.5)
    print('leaving ' + channeld.name)
    await vcm.disconnect()


@client.command(help='time untile next nami and its alert',
                brief='time untile next nami')
async def namitime(ctx):
    await ctx.channel.send(read_return_time('namitime.txt') + ' seconds')


@client.command(help='mesdict (testing thing)', brief='many numbers')
async def mesdict(ctx):
    global lastmes_dict
    await ctx.channel.send(lastmes_dict)


@client.command(help='adds reactions to the previous message in that channel',
                brief='adds reactions to prev message')
async def addreactions(ctx, *args):
    emlist = []
    for arg in args:
        emlist.append(arg)

    message_t = await ctx.message.channel.fetch_message(lastmes_dict[str(
        ctx.message.channel.id)])

    for emoji in emlist:
        try:
            await message_t.add_reaction(emoji)
        except:
            pass
    await ctx.message.delete()


@client.command(help='floppa gif', brief='flopa')
async def floppa(ctx):
    ctx.message.channel.send(floppagif(ctx.channel, 'floppa'))


@client.event
async def on_message(message):

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

    if not (message.content.startswith('$addreactions')
            or len(message.content) <= 0) or len(message.attachments) > 0:
        lastmes_dict[str(message.channel.id)] = message.id

    if message.author.bot:
        return

    ctx = await client.get_context(message)
    if ctx.valid:
        await client.process_commands(message)
        return

    if 'mm' in message.content:
        send_string = ''
        for i in range(random.randint(1, 51)):
            send_string += 'm'
        await message.channel.send(send_string)

    def ping_pong(input_message):
        if message.author.bot:
            return
        banned_2 = ['c', 's']
        banned_3 = ['i', 'ee', 'ea']
        banned_4 = ['c', 'k', 'ck', 's']
        banned_5 = ['a', 'ah', 'u', 'uh']
        for word2 in banned_2:
            for word3 in banned_3:
                for word4 in banned_4:
                    for word5 in banned_5:
                        fullword = word2 + word3 + word4 + word5
                        if 'JAH' + fullword.upper() in message.content.upper():
                            return 'shut up higg'
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

    if 'ping' in message.content or 'pong' in message.content:
        await message.channel.send(ping_pong(message.content))


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
    try:
        for r in gdict[str(member.guild.id)][str(member.id)].rolelist:
            try:
                await member.add_roles(member.guild.get_role(r))
                #print('added ' + member.guild.get_role(r).name)
            except discord.Forbidden:
                print(member.guild.get_role(r).name + ' is forbidden; passed')
                pass
    except KeyError:
        pass  #add txt stuff here eventually?


def cheadlewotd():
    filename = 'dc_pics/' + str(random.randint(1, 71)) + '.jpg'
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
    return 'result.jpg'


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

    message_channel = client.get_channel(target_channel_id)
    await message_channel.send(file=discord.File(cheadlewotd()))
    print('cheadle sent')
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game(
            'the day is ' +
            daysdict[str(time.gmtime(time.time() - 3600 * 7).tm_wday)]))
    await asyncio.sleep(240)


@timer_shit_fuck.before_loop
async def before_timer_shit_fuck():
    await client.wait_until_ready()
    await asyncio.sleep(1)


@client.event
async def floppagif(input_message, keyword):
    apikey = 'ACQ2CXM2PN1Z'
    lmt = 50
    search_term = keyword
    r = requests.get(
        "https://g.tenor.com/v1/search?q={}&key={}&limit={}".format(
            search_term, apikey, lmt))
    idd = random.randint(0, lmt - 1)
    if r.status_code == 200:
        top_gifs = json.loads(r.content)
        fuck = top_gifs['results'][idd]['media'][0]['gif']['url']
    else:
        fuck = 'no gifs found'
    return fuck


#@jahtimer.before_loop
#async def before_timer_jahtimer():
#await client.wait_until_ready()
#await asyncio.sleep(1)
# :) <3

#------------------------------------------------------------------------------------
#------------------------------------$joinvoice--------------------------------------
#------------------------------------------------------------------------------------

songlistwvol = joinboice.songlistwvol
songlist = list(songlistwvol)


@client.event
async def joinm(boice_channel):
    print(f"Got channel {boice_channel}")
    return await boice_channel.connect()


@client.event
async def leavem(boice_channel, voicec):
    print(f"Leaving channel {boice_channel}")
    await voicec.disconnect()


@client.event
async def playsongm(index, voicec):
    print('playing ' + songlist[index])
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
    if thing == False or not (int(index) in range(len(songlist))):
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


timer_shit_fuck.start()
#jahtimer.start()

keep_alive.keep_alive()

client.run(os.getenv('TOKEN'))
