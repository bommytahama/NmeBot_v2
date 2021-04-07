import discord
from discord.ext import tasks
import random
import asyncio
import time
#import os
#from threading import Thread
#from multiprocessing import Pool

client = discord.Client(intents=discord.Intents.all())

true_n_general = 802684938381557840  #nme
testing_id = 815405498412171294  #testing
doangus = 817632403228196874  #doangus

#vc_id_list = [doangus, true_n_general]  #doangus then general
vc_id_list = [testing_id]


def filewritev(time_now, timertime):
    timefile = open('jointime.txt', "r+")
    timefile.truncate()
    timefile.writelines(str(time_now) + '\n' + str(timertime))
    timefile.close()


@client.event
async def on_ready():
    print('voice ready')

#4/6/2021
#last night i chipped my tooth by slamming it into my woter botttle
#im such a fuckup but at least weve got insurance :))) i love america and capitalism

songlistwvol = {
    'south': 0.3,  #0
    'yuyu': 0.25,  #1
    'iceage': 0.1,  #2
    'deepboom': 3,  #3
    'among': 1.5,  #4
    'higgtheme': 0.42,  #5
    'jahrant': 8,  #6
    'sutekime': 0.2,  #7
    't1': 4,  #8
    'wee': 1.2,  #9
    'zaregoto': 0.2,  #10
    'penis-1h': 0.12,  #11
    'xqcnme': 0.5,  #12
    'hachi': 0.2,  #13
    'hatersbroke': 0.3,  #14
    'horsepiano': 0.7,  #15
    'humor': 0.3,  #16
    'pop': 50,  #17
    'jujutsu': 0.24,  #18
    'duck': 0.24,  #19
    'cancun_sega': 0.34,  #20
    'ecco_lal': 0.3,  #21
    'cockver10': 0.2,  #22
    'bg2m': 0.3,  #23
    'codlaugh': 0.5,  #24
    'october': 0.9,  #25
    'cockmuncher': 10,  #26
    'among2': 1.5, #27
    'bladee': 1.2, #28
    'sus': 1, #29
    'floppameow': 3, #30
    'fnaftrailer': 5, #31
    'warowl': 100, #32
    'allofthelights': 2, #33
}
songlist = list(songlistwvol)

class voice_stuff(object):
  def __init__(self, vccid, indexx):
    self.vccid = vccid
    self.vcc = 1
    self.indexx = indexx
    self.channel = client.get_channel(self.vccid)
    self.voicec = None
  
  @client.event
  async def leave(self):
      print(f"Leaving channel {self.channel.name}")
      await self.voicec.disconnect()

  @client.event
  async def join(self):
      #global channel
      #print('got it')
      self.voicec = await self.channel.connect()
      #print('got it 2')

  @client.event
  async def playsong(self):
      print('playing ' + songlist[self.indexx])
      #songindex = random.randint(0, len(songlist) - 1)
      #songindex = 0
      song = songlist[self.indexx]
      audio = discord.FFmpegPCMAudio(source="songs/" + song + ".mp3")
      source = discord.PCMVolumeTransformer(audio)
      source.volume = songlistwvol[song]
      self.voicec.play(source)
      #while self.voicec.is_playing():
      #    self.vcc = 1
      #    await asyncio.sleep(0.5)
      #self.vcc = 0
      

  @client.event
  async def voicejoining(self):
      print('chech')
      print('chech2')
      await voice_stuff.join()
      print('chech3')
      await asyncio.sleep(1)
      print('chech4')
      await voice_stuff.playsong()
      print('chech5')
      await voice_stuff.leave()
      
      




#def between_vcj(idlist, indexx):
#  loop = asyncio.new_event_loop()
#  asyncio.set_event_loop(loop)


@tasks.loop()
@client.event
async def join_song():
    timer = random.randint(5, 172800)  #30 hours
    #timer = 1
    nowtimev = time.time()
    await asyncio.sleep(3)
    filewritev(nowtimev, timer)
    await asyncio.sleep(timer)
    #await asyncio.sleep(3)
    songindex = random.randint(0, len(songlist) - 1)
    #songindex = 16
    guildlist = []
    for g in client.guilds:
      voicelistm = []
      voicelist = []
      sortedvoice = []
      for v in g.voice_channels:
        if len(v.members) != 0:
          voicelistm.append(v.members)
          voicelist.append(v.id)
      vcmlen = len(voicelistm)
      for item in range(vcmlen):
        maxList = max(voicelistm, key=len)
        #maxLength = max(len(x) for x in voicelistm)
        sortedvoice.append(voicelist[voicelistm.index(maxList)])
        voicelist.remove(voicelist[voicelistm.index(maxList)]) #the industrial revolution and its consequences have been a disaster for the human race
        voicelistm.remove(maxList)
      if len(sortedvoice) == 0:
        try:
          sortedvoice.append(g.afk_channel.id)
        except:
          sortedvoice.append(random.choice(g.voice_channels).id)
      guildlist.append(sortedvoice)
    print(guildlist)
    biglist = []
    dictlist = []
    maxsorted = max(guildlist, key=len)
    for i in range(len(maxsorted)):
      biglist.append(list())
      for lst in guildlist:
        try:
          biglist[i].append(lst[i])
        except IndexError:
          pass
    #for lst in guildlist: #ADD THREADING HERE
    #  biglist.append(lst[0])    
    for listt in biglist:
      dictlist.append({})
      for idd in listt:
        dictlist[biglist.index(listt)][idd] = voice_stuff(vccid=idd, indexx=songindex)
    for dictt in dictlist:
      classlist = list(dictt)
      #this is all messy and awful but it works so im not changing it lololoolol
      for item in classlist:
        await dictt[item].join()
      for item in classlist:
        await dictt[item].playsong()
      vcclist = []
      await asyncio.sleep(0.5)
      for item in classlist:
        if dictt[item].voicec.is_playing():
          vcclist.append(1)
        else:
          vcclist.append(0)
      while 1 in vcclist:
        vcclist.clear()
        for item in classlist:
          if dictt[item].voicec.is_playing():
            vcclist.append(1)
          else:
            vcclist.append(0)
        await asyncio.sleep(0.5)
      for item in classlist:
        await dictt[item].leave()

    await asyncio.sleep(1)
    #while 1 in vcclist:
    #    await asyncio.sleep(1)
      


@join_song.before_loop  #im a fucking idiot
async def before_join_song():
    await client.wait_until_ready()
    await asyncio.sleep(1)
    print('voice loop ready')


#join_loop.start()
join_song.start()
