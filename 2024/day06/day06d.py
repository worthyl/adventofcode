f = [list(l.strip()) for l in open("input.txt","rt")] # game field
NY,NX = len(f),len(f[0])

for y,l in enumerate(f):
  for x,c in enumerate(l):
    if c in "<>^v":
      sx,sy = x,y # start x, start y
      d = "^>v<".find(c) # direction UP RT DN LT ~ 0 1 2 3
      f[y][x] = "x" # start pos is visited
      break # could add 'if c in "<>^v": break' in outer loop and break it too

def game(x,y,d,sf):
  f = [l[:] for l in sf[:]]
  while 'loop':
    nx,ny = x+(0,1,0,-1)[d],y+(-1,0,1,0)[d] # newx newy
    if nx<0 or nx>=NX or ny<0 or ny>=NY: # finish
      return sum(v=="x" for l in f for v in l)
    if f[ny][nx]=="#": # turn right
      d = (d+1)%4
    else: # advance
      f[ny][nx] = "x" # visited
      x,y = nx,ny

print(game(sx,sy,d,f))

def game_with_loop(x,y,d,sf,ox,oy)->int:
  f = [l[:] for l in sf[:]]
  f[oy][ox] = "#"
  v = set() # visited
  while 'loop':
    v.add((x,y,d))
    nx,ny = x+(0,1,0,-1)[d],y+(-1,0,1,0)[d] # newx newy
    if nx<0 or nx>=NX or ny<0 or ny>=NY: # finish
      return 0
    if f[ny][nx]=="#": # turn right
      d = (d+1)%4
    else: # advance
      f[ny][nx] = "x" # visited
      x,y = nx,ny
    if (x,y,d) in v:
      return 1

print(sum(game_with_loop(sx,sy,d,f,x,y) for x in range(NX) for y in range(NY) if f[y][x]=="."))
