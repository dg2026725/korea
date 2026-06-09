b = box(pos = vec(50,0,-25), size = vec(100,100,0), texture = 'https://i.imgur.com/u3haxbY.jpeg')

for q in range(50) :
    box(pos = vec(50,-50,q), size = vec(100,5,50), color = vec(214/255,217/255,216/255), shininess = 0)
    box(pos = vec(50,-45,q), size = vec(80,5,40), color = vec(214/255,217/255,216/255), shininess = 0)
    box(pos = vec(50,-43,q), size = vec(75,3,35), color = vec(214/255,217/255,216/255), shininess = 0)
    box(pos = vec(50,-10,q), size = vec(75,3,20), color = vec(0/255,100/255,0/255), shininess = 0)
    box(pos = vec(20,-30,q), size = vec(5,40,5), color = vec(178/255,34/255,34/255), shininess = 0)
    box(pos = vec(80,-30,q), size = vec(5,40,5), color = vec(178/255,34/255,34/255), shininess = 0)
    box(pos = vec(50,-40,q), size = vec(55,10,5), color = vec(60/255,179/255,113/255), shininess = 0)
    box(pos = vec(50,-23,q), size = vec(55,25,5), color = vec(255/255,250/255,240/255), shininess = 0)
    box(pos = vec(50,-35,53), size = vec(10,20,1), color = vec(254/255,245/255,230/255), shininess = 0)
    
while True :
    rate(50)
    k = keysdown()
    if ' ' in k :
        b.texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQruH_sEODrsDkBrnaLGn8Lysog30Uu_BglWWAcJpcqoddPS_mpOcDt_Qc&s=10'

while True :
    rate(50)
    w = k()
    if 'w' in k :
        b.opacity = random.random()
