import math
import random
from functions import func

playerName = None
playerGender = None

# Setup
def gameSetup():
  global playerName
  global playerGender
  playerName = func.q('Input your name...')
  playerGender = func.mCQ('Input gender...', {'m', 'f'})
  func.tI('''
NOTE
Due to the pressure of time, this program will unfortunately not be taking into account preferences of the LGBTQIA+ community.
Apologies in advance, I'd love to implement this someday.

Press [ENTER] to continue.''')
  func.clear()

# Introduction
def gameIntroduction():
  func.tD('Years ago, the United States was ravaged by war.')
  func.tD('Wanting to form an everlasting peace, the government sent out men to investigate the causes.')
  func.tD('They found that love was by far the most prominent cause of war.')
  func.tD('Love became known as amor deliria nervosa.')
  func.tD('Deliria caused desire. Desire ruined the people.')
  func.tD('For the protection of the people, the government closed all borders.')
  func.tD('For the protection of the people, the citizens were to move into protected cities.')
  func.tD('For the protection of the people, the government worked on a cure.')
  func.tD('The cure for amor delieria nervosa.')
  func.tD('Over years of experimentation, the government found a solution.')
  func.tD('The cure was for those over the age of 18.')
  func.tD('Getting the cure at a younger age would cause unwanted side-effects.')
  func.tD('The cure rid the patient of all desire for love.')
  func.tD('For without love, there is no desire.')
  func.tD('Without desire, you are truly happy.')
  func.tD('Without desire, you are at peace.')
  func.tD('And the government wants you to be happy.')
  func.tD('And the government wants you to be at peace.')
  func.clear()

# Exposition
def gameExposition():
  # func.tD('100 Days.')
  # func.tD('You have 100 days until your procedure.')
  # func.tD('The procedure which will save your life.')
  # func.tD('You will be truly at peace.')
  # func.tD('You can\'t wait.')
  # func.clear()

  func.tD('Delirium')
  func.tD('The Game')
  func.tD('Panic Monster Edition')
  func.tD('"So much to code" - Alan Qi')
  func.clear()

# Panic Monster Game
def gamePanic():
  '''
  Start at evaluations (show "optimal answer")
  Get a score
  See opposite gender
  Player chooses whether or not to approach
  Friend invites surfing the intranet ("illegal" music)
  Player chooses Y/N
  Raid occurs
  Player chooses to cooperate/resist
  If cooperate:
    Depending on previous choices: Dragged into a chase by the opposite gender from earlier. Can either choose to submit or resist. Chase difficulty based on previous choices
    If perfect: Rest of their life normally
  If resist:
    Gets into a chase. Meets opposite gender from earlier. Chase difficulty & catch punishment based on previous choices
  '''
  gameScore = 0

  # Evaluations
  eScore = 0
  func.tD(f'Hello {playerName}, welcome to evaluations.')
  func.tD('Here, you will be answering questions.')
  func.tD('At the end, you will be given a score.')
  func.tD('Answer to the best of your ability.')
  func.tI('Press [ENTER] to continue.')

  sprites = func.screenT('Optimal Answer', [], [ 24, 0 ])
  sprites = func.screenT('Blue', sprites, [ 34, 1 ])
  sprites = func.screenT('What is your favorite color?', sprites, [ 0, 13 ])
  sprites = func.screenT('1 - Red', sprites, [ 0, 14 ])
  sprites = func.screenT('2 - Green', sprites, [ 0, 15 ])
  sprites = func.screenT('3 - Blue', sprites, [ 0, 16 ])
  sprites = func.screenT('4 - Yellow', sprites, [ 0, 17 ])
  func.screen(sprites)
  ans = func.mCQH({ '1', '2', '3', '4' })
  ans = int(ans)
  if ( ans == 1 ): eScore += 1
  elif ( ans == 2 ): eScore += 2
  elif ( ans == 3 ): eScore += 3
  elif ( ans == 4 ): eScore += 0

  sprites = func.screenT('Optimal Answer', [], [ 24, 0 ])
  sprites = func.screenT('Rules', sprites, [ 33, 1 ])
  sprites = func.screenT('What do you value the most?', sprites, [ 0, 13 ])
  sprites = func.screenT('1 - Rules', sprites, [ 0, 14 ])
  sprites = func.screenT('2 - Friendship', sprites, [ 0, 15 ])
  sprites = func.screenT('3 - The Truth', sprites, [ 0, 16 ])
  sprites = func.screenT('4 - The Right Thing', sprites, [ 0, 17 ])
  func.screen(sprites)
  ans = func.mCQH({ '1', '2', '3', '4' })
  ans = int(ans)
  if ( ans == 1 ): eScore += 3
  elif ( ans == 2 ): eScore += 1
  elif ( ans == 3 ): eScore += 0
  elif ( ans == 4 ): eScore += 2

  sprites = func.screenT('Optimal Answer', [], [ 24, 0 ])
  sprites = func.screenT('Yes', sprites, [ 35, 1 ])
  sprites = func.screenT('Do you trust the government?', sprites, [ 0, 15 ])
  sprites = func.screenT('1 - No', sprites, [ 0, 16 ])
  sprites = func.screenT('2 - Yes', sprites, [ 0, 17 ])
  func.screen(sprites)
  ans = func.mCQH({ '1', '2' })
  ans = int(ans)
  if ( ans == 1 ): eScore += 0
  elif ( ans == 2 ): eScore += 4

  func.clear()
  func.tD('You have completed the evaluations.')
  func.tD(f'You have received a score of: {eScore}/10')
  gameScore += eScore
  func.clear()

  # Opposite Gender
  data = []
  if ( playerGender == 'm' ):
    data.append('girl')
    data.append('Lena')
  elif ( playerGender == 'f' ):
    data.append('boy')
    data.append('Alex')

  func.tD(f'While you are walking home, you see a {data[0]} named {data[1]}')
  sprites = func.screenT('Optimal Answer', [], [ 24, 0 ])
  sprites = func.screenT('Go Home', sprites, [ 31, 1 ])
  sprites = func.screenT('What do you do?', sprites, [ 0, 15 ])
  sprites = func.screenT('1 - Go Home', sprites, [ 0, 16 ])
  sprites = func.screenT(f'2 - Approach {data[1]}', sprites, [ 0, 17 ])
  func.screen(sprites)
  ans = func.mCQH({ '1', '2' })
  ans = int(ans)
  if ( ans == 1 ):
    gameScore += 3
    func.tI('You went home. You aren\'t cured yet, anyway.')
  elif ( ans == 2 ):
    gameScore -= 3
    func.tI(f'It won\'t hurt. You approach {data[1]} before heading back home.')
  func.clear()

  # Illegal Music
  func.tD('At home, you call your friend.')
  func.tI(f'"Oh hey {playerName}! How are you?"')
  func.tI('You hear a strange music coming from your friend\'s end.')
  func.tI('You decide to ask about it.')
  func.tI('"Huh? Oh, it\'s just some music that I found."')
  func.tI('"I got it from the Intranet."')
  func.tI('You decide to double check and make sure your friend got it from the Intranet Library of Approved Entertainment.')
  func.tD('"Well, you see..."')
  func.tI('"Umm, not really."')
  func.tI('"But seriously, it\'s great music. You should listen to it."')
  ans = func.yNQ('Will you listen to this music?')
  if ( ans.lower() == 'y' or ans.lower() == 'yes' ):
    gameScore -= 3
    func.tI('You and your friend spend time enjoying Always Gonna Let Your Down by Yeltsa Kcir.')
  elif ( ans.lower() == 'n' or ans.lower() == 'no' ):
    gameScore += 3
    func.tI('Nope, not worth the risk.')
  func.clear()

  # Raid
  func.tD('That night, you hear a siren.')
  func.tI('"Attention. This is a raid."')
  func.tI('"Do not try to resist."')
  func.tI('"Do not try to flee."')
  func.tD('A few minutes later, the regulators are knocking on your door.')

  sprites = func.screenT('Optimal Answer', [], [ 24, 0 ])
  sprites = func.screenT('Cooperate', sprites, [ 29, 1 ])
  sprites = func.screenT('What do you do?', sprites, [ 0, 15 ])
  sprites = func.screenT('1 - Cooperate', sprites, [ 0, 16 ])
  sprites = func.screenT(f'2 - Resist & Flee', sprites, [ 0, 17 ])
  func.screen(sprites)
  ans = func.mCQH({ '1', '2' })
  ans = int(ans)
  if ( ans == 1 ):
    gameScore += 4
    func.tI('Not worth it.')
    if ( gameScore >= 15):
      func.tD('The regulators pass on you.')
      func.tD('You get cured and lead a normal, plain life.')
      func.tD('You are at peace.')
      func.tI('The End')
      return
  elif ( ans == 2 ):
    gameScore -= 4
    func.tI('Yeah, regulators are poo poo anyway.')
  func.clear()

  # Chase
  func.tD('Cooperate or not, you are forced to flee.')
  func.tD(f'{data[1]} drags you to follow them.')
  func.tD('The regulators begin to chase you.')
  func.clear(delay = 0)

  func.tI('''
- Get caught soon, you may have a chance of being let go.
- Get caught later, you will be sent to the Crypts.
- Escape to the Wilds, you won't be caught.
- Input W/A/S/D to move.
- The regulators move 1 space for every space you move.
- Press [ENTER] to begin.
  ''')

  sprites = [[ 'P', [ random.randint(0, 37), random.randint(1, 16) ] ]]
  sprites.append([ 'W', [ random.randint(0, 37), random.choice([ 0, 17 ]) ] ])
  rng = math.floor(( 20 - gameScore ) / 2)
  for r in range(rng):
    position = [ random.randint(0, 37), random.randint(1, 17) ]
    if ( sprites[0][1] == position ): position[0] += 1
    sprites.append([ 'R', position ])

  moves = 0
  over = False
  while over == False:
    func.screen(sprites)
    if ( sprites[0][1] == sprites[1][1] ):
      over = 'Free'
      continue
    for i in sprites:
      if ( i[0] == 'P' or i[0] == 'W' ): continue
      if ( i[1] == sprites[0][1] ):
        over = True
        continue

    cmd = input('> ').lower()

    if ( cmd == 'w' ):
      if ( sprites[0][1][1] > 0 ): sprites[0][1][1] -= 1
    elif ( cmd == 'a' ):
      if ( sprites[0][1][0] > 0 ): sprites[0][1][0] -= 1
    elif ( cmd == 's' ):
      if ( sprites[0][1][1] < 17 ): sprites[0][1][1] += 1
    elif ( cmd == 'd' ):
      if ( sprites[0][1][0] < 37 ): sprites[0][1][0] += 1

    for i in sprites:
      if ( i[0] == 'P' or i[0] == 'W' ): continue
      dx = i[1][0] - sprites[0][1][0]
      dy = i[1][1] - sprites[0][1][1]
      if ( abs(dx) >= abs(dy) ): i[1][0] -= ( dx / abs(dx) )
      else: i[1][1] -= ( dy / abs(dy) )

    moves += 1
  
  if ( over == 'Free' ):
    func.tD(f'You and {data[1]} are free.')
    func.tD('You\'ve escaped to the Wilds.')
    func.tD('You live a new life, a happier one than anyone in the Government ever could have lived.')
    func.tD('You have found a new peace.')
    func.tI('The End')
    return
  if ( moves <= 10 and gameScore >= 7 ):
    func.tD('You are caught, but because of your cooperation the regulators let you go.')
    func.tD('You get cured and lead a normal, plain life.')
    func.tD('You are at peace.')
    func.tI('The End')
    return
  func.tD('You have been caught by the regulators.')
  func.tD('Due to your lack of cooperation, you have been sent to the Crypts')
  func.tD('Ward Six, to be precise.')
  func.tD('You will stay there forever.')
  func.tI('The End')
  return
  
def main():
  gameSetup()
  gameIntroduction()
  gameExposition()
  gamePanic()

if __name__ == '__main__':
  main()