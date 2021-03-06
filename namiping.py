from discord.ext import tasks, commands
import asyncio
import discord
import time

client = commands.Bot(intents=discord.Intents.all(), command_prefix='$')
jah_id = 290214091442618380
knuc_id = 383719623184482304
terry_id = 587054039452221603
bee_id = 359881799939391488

id_list = [jah_id, knuc_id, terry_id, bee_id]
sda_channel = 745893614680539176


@client.event
async def nami_ping(channel_id, user_id_list):
    channel = client.get_channel(channel_id)
    ping_message = ''
    for user_id in user_id_list:
        ping_message += '<@' + str(user_id) + '> '
    ping_message += 'nami meeting'
    await channel.send(ping_message)


def filewriten(time_now, timertime):
    timefile = open('namitime.txt', "r+")
    timefile.truncate()
    timefile.writelines(str(time_now) + '\n' + str(timertime))
    timefile.close()


@tasks.loop()
@client.event
async def nami_timer():
    tsec = time.time()
    t = time.gmtime()
    send_min = 50
    send_day = 2  #wednesday == 2
    send_time_l = 10  #am #l = local
    send_time = send_time_l + 7
    if send_time >= 24:
        send_time -= 24
        send_day += 1
        if send_day >= 7:
            send_day -= 7

    if t.tm_hour == send_time and t.tm_min == send_min and t.tm_wday == send_day:
        #print('1-n')
        print('sending ping...')
        await nami_ping(sda_channel, id_list)
        await asyncio.sleep(240)
        return

    if t.tm_min <= send_min:
        #print('2-n-1')
        wtime1 = (60) * (send_min - t.tm_min)
        next_hour = 0
    else:
        #print('2-n-2')
        wtime1 = (60) * ((60 - t.tm_min) + send_min)
        next_hour = 1

    if t.tm_hour <= send_time and not(t.tm_hour == send_time and t.tm_min > send_time):
        #print('3-n-1')
        wtime2 = (60 * 60) * ((send_time - t.tm_hour) - next_hour)
        next_day = 0
    else:
        #print('3-n-2')
        wtime2 = (60 * 60) * (((24 - t.tm_hour) - next_hour) + send_time)
        next_day = 1


    if t.tm_wday <= send_day and not(t.tm_wday == send_day and (t.tm_hour > send_time or (t.tm_hour == send_time and t.tm_min > send_min))):
        #print#('4-n-1')
        wtime3 = (60 * 60 * 24) * ((send_day - t.tm_wday) - next_day)
    else:
        #print#('4-n-2')
        wtime3 = (60 * 60 * 24) * (((7 - t.tm_wday) - next_day) + send_day)

    wtime = wtime1 + wtime2 + wtime3
    filewriten(tsec, wtime)
    await asyncio.sleep(wtime)
    print('sending ping...')
    await nami_ping(sda_channel, id_list)
    wtimea = 720
    tsec = time.time()
    filewriten(tsec, wtimea)
    await asyncio.sleep(wtimea)

@nami_timer.before_loop
async def before_timer_nami():
    await client.wait_until_ready()
    await asyncio.sleep(1)

nami_timer.start()
