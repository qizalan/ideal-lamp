import time

class func:
  def q(q):
    ans = input(f'{q}\n> ')
    if ans == '':
      print('You need to provide an answer!')
      return func.q(q)
    else:
      return ans
  def yNQ(q):
    ans = input(f'{q}\n> ')
    if ( ans.lower() != 'y' and ans.lower() != 'n' ):
      if ( ans.lower() != 'yes' and ans.lower() != 'no' ):
        print('You need to provide a yes/no answer!')
        return func.yNQ(q)
    else:
      return ans
  def mCQ(q, opts):
    ans = input(f'{q}\nOptions: {opts}\n> ')
    if ( ans not in opts ):
      print(f'You need to provide one of these answers: {opts}')
      return func.mCQ(q, opts)
    else:
      return ans

  def mCQH(opts):
    ans = input('> ')
    if ( ans not in opts ):
      print(f'You need to provide one of these answers: {opts}')
      return func.mCQH(opts)
    else:
      return ans
  
  def tD(string, delay = 4):
    print(string)
    time.sleep(delay)
  def tI(string):
    print(string)
    input('> ')
  
  def clear(lines = 50, delay = 5):
    for i in range(lines):
      print('\n')
      time.sleep(0.005)
    time.sleep(delay)
  def screen(sprites = []):
    sLine = '┌——————————————————————————————————————┐'
    eLine = '└——————————————————————————————————————┘'
    print(sLine)
    for l in range(18):
      line = '|'
      for c in range(38):
        length = len(line)
        for s in sprites:
          if ( s[1][0] == c and s[1][1] == l ):
            line += s[0]
        if ( len(line) == length ):
          line += ' '
      line += '|'
      print(line)
    print(eLine)
  def screenT(text, sprites, sLoc = [0, 0]):
    for i in range(len(text)):
      if ( text[i] == ' ' ): continue
      sprites.append([ text[i], [ sLoc[0] + i, sLoc[1] ] ])
    return sprites