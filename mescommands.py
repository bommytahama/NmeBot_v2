import time

class messagethings(object):
  def __init__(self, mes):
    self.mes = mes

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
    '$allroles': [send_message, [message,
                                 str(guilds_and_roles)[:2000]]],
    '$weather': [send_message, [message,
                                weather_yeah(message.content[9:])]],
    '$cheadle': [send_filec, [message, discord.File("result.jpg")]],
    '$echo ': [send_message, [message, message.content[6:]]],
    '$chance': [send_message, [message, str(chance) + ' out of 50000']],
    '$words': [send_message, [message, str(len(wordlist)) + ' words']],
    '$timeleftcheadle':
    [send_message, [message, time_left(tsecc, wtimec) + ' seconds']],
    '$voicetimer':
    [send_message, [message,
                    read_return_time('jointime.txt') + ' seconds']],
    '$lensonglist':
    [send_message, [message, str(len(joinboice.songlist)) + ' songs']],
    '$joinvoice': [join_channel, [message]],
    '$namitime':
    [send_message, [message,
                    read_return_time('namitime.txt') + ' seconds']],
    #'$mmmmtime': [send_message, [message, time_left(tsec_mmmm ,wait_mmmm) + ' secondmmmm']],
    '$addreaction ': [react, [message, lastmes_dict[str(message.channel.id)]]],
    '$mesdict': [send_message, [message, lastmes_dict]],
    'mm': [send_message, [message, mmmm()]],
    'ping': [send_message, [message, ping_pong(str(message.content))]],
    'pong': [send_message, [message, ping_pong(str(message.content))]],
}
command_namelist = list(command_dict)
