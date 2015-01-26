import json
import urllib2
import re

pattern = re.compile('[\W_]+')

def normalize_name(s):
  return pattern.sub('', s.lower())

def transform_name(name):
  """ transform name formatted as 'firstname lastname' to 'lastname, firstname' """
  split_name = name.split(' ', 1)
  firstname = str.strip(str(split_name[0]))
  lastname = str.strip(str(split_name[1]))
  s = '{}, {}'.format(lastname, firstname)
  normalized_name = normalize_name(s)
  # DLF and MFL have different ways of storing name of Odell Beckham Jr
  if normalized_name == 'beckhamjrodell':
    return 'beckhamodell'
  else:
    return normalized_name
  return normalized_name

def dlf_rankings():
  with open('rankings.json') as json_file:
    rankings = json.load(json_file)
    name_to_ranking = {}
    for ranking in rankings:
      nm = ranking['player']
      name = transform_name(nm)
      name_to_ranking[name] = ranking
    return name_to_ranking

def nfdl_rosters():
  url = 'http://football18.myfantasyleague.com/2014/export?TYPE=rosters&L=67651&W=&JSON=1'
  resp = urllib2.urlopen(url)
  return json.loads(resp.read())['rosters']['franchise']

def nfdl_franchises():
  url = 'http://football18.myfantasyleague.com/2014/export?TYPE=league&L=67651&W=&JSON=1'
  resp = urllib2.urlopen(url)
  franchises = json.loads(resp.read())['league']['franchises']['franchise']
  id_to_franchise = {}
  for franchise in franchises:
    id_to_franchise[franchise['id']] = franchise
  return id_to_franchise

def mfl_players():
  url = 'http://football18.myfantasyleague.com/2014/export?TYPE=players&L=67651&W=&JSON=1'
  resp = urllib2.urlopen(url)
  players = json.loads(resp.read())['players']['player']
  id_to_player = {}
  for player in players:
    id_to_player[player['id']] = player
  return id_to_player

def print_keepers():
  rankings = dlf_rankings()
  rosters = nfdl_rosters()
  all_players = mfl_players()
  franchises = nfdl_franchises()

  for roster in rosters:
    players = roster['player']
    print('------- {} -------'.format(franchises[roster['id']]['name']))
    keepers = []
    for player in players:
      player_info = all_players[player['id']]
      player_name = player_info['name']
      try:
        ranking = rankings[normalize_name(player_name)]
        if ranking['rank'] < 170:
          keepers.append((player_info, ranking))
      except:
        pass
        #print('####### can\'t find player: {}'.format(player_info))
    for k in sorted(keepers, key=lambda x: x[1]['rank']):
      print(k)
    print('Number of keepers: {}'.format(len(keepers)))

def main():
  print_keepers()

if __name__ == '__main__':
  main()
