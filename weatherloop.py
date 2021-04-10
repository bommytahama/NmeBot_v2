from discord.ext import tasks, commands
import asyncio
import discord
import time
from pyowm import OWM
import datetime

owm = OWM('36468e84160aed68e1cf6d38fed55140')
mgr = owm.weather_manager()

client = commands.Bot(intents=discord.Intents.all(), command_prefix='$')
weatherchannel = 825882341314265129

city_list = ['San Diego, US']


def get_weather_things(city):
    obs = mgr.weather_at_place(city)
    w = obs.weather
    wgen = w.detailed_status
    wtemp = w.temperature('fahrenheit')['temp']
    wtempmax = w.temperature('fahrenheit')['temp_max']
    wtempmin = w.temperature('fahrenheit')['temp_min']
    wwind = w.wind()
    wwindspeed = wwind['speed']
    t = time.gmtime(time.time() + (3600 * 6))
    hourur = t.tm_hour
    qwerty = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, hourur)
    obsf = mgr.forecast_at_place(city, '3h')
    weather = obsf.get_weather_at(qwerty)
    wgenfor = weather.detailed_status
    if wgenfor == wgen:
        filler = 'continue to get'
    else:
        filler = 'be getting'
    changedict = {
        'clear sky': 'clear skies :sunny:',
        'few clouds': 'a few clouds :cloud:',
        'scattered clouds': 'scattered clouds :partly_sunny:',
        'broken clouds': 'broken clouds :white_sun_small_cloud:',
        'overcast clouds': 'overcast clouds :fog:',
        'light rain': 'light rain :cloud_rain:',
    }
    changedictlist = list(changedict)
    wgenlist = [wgen, wgenfor]
    for thing3 in wgenlist:
        for thing4 in changedictlist:
            if str(thing3) == thing4:
                wgenlist[wgenlist.index(thing3)] = changedict[str(thing3)]
    wgen = wgenlist[0]
    wgenfor = wgenlist[1]

    return city, wgen, str(wtemp), str(wtempmin), str(wtempmax), str(
        wwindspeed), filler, wgenfor


#maybe it was ME who was fucking up


def filewritew(filename, time_now, timertime):
    timefile = open(filename, "r+")
    timefile.truncate()
    timefile.writelines(str(time_now) + '\n' + str(timertime))
    timefile.close()


weathermessage = 'in {} right now there\'s {}, with temperatures around {}°F with lows of {}°F and highs of {}°F, as well as wind speeds around {} mph, and later on it seems like we\'ll {} {}'


@tasks.loop()
@client.event
async def weathertimer():
    tsecw = time.time()
    t = time.gmtime()
    send_time_l = 12  #am #l = local
    send_time = send_time_l + 7
    if send_time >= 24:
        send_time -= 24
    if t.tm_hour == send_time and t.tm_min == 0:
        wtimew = 0
    elif t.tm_hour < send_time:
        wtimew = ((60 * 60) * ((send_time - 1) - t.tm_hour)) + (
            (60) * (59 - t.tm_min)) + (60 - t.tm_sec)
    elif t.tm_hour >= send_time:
        wtime1 = ((60 * 60) *
                  (23 - t.tm_hour)) + ((60) *
                                       (59 - t.tm_min)) + (60 - t.tm_sec)
        wtime2 = send_time * 60 * 60
        wtimew = wtime1 + wtime2
    filewritew('weathertime.txt', tsecw, wtimew)
    await asyncio.sleep(wtimew)
    message_channelw = client.get_channel(weatherchannel)
    print(f"Got channel {message_channelw}")
    for c in city_list:
        await message_channelw.send(
            weathermessage.format(*get_weather_things(c)))
    await asyncio.sleep(240)


@weathertimer.before_loop
async def before_weather():
    await client.wait_until_ready()
    await asyncio.sleep(1)


weathertimer.start()
