from replit import db

def wordtotal(serv_id):
  total = 0
  for item in list(db['wordstuff'][str(serv_id)]):
    total += db['wordstuff'][str(serv_id)][item]
  return total

def indiv_freq(serv_id, word):
  try: 
    db['wordstuff'][str(serv_id)][word]
  except KeyError:
    return 'no data available'
  
  wtotal = wordtotal(serv_id)
  percent = 100 * (db['wordstuff'][str(serv_id)][word]/wtotal)
  return f"the word '{word}' makes up {str(percent)}% of the words said in this server, having been said {str(db['wordstuff'][str(serv_id)][word])} times out of {str(wtotal)} total words said (since the time when this command was written)"
