from django.http import JsonResponse, HttpResponse
from enemy.serializer import EnemySerializer
from weapon.models import Weapon, WeaponType
from weapon.serializer import WeaponSerializer
import random
from character.models import Character
from django.shortcuts import get_object_or_404
from enemy.models import EnemyType, Enemy
#from labyrinth.models import Labyrinth

model1 =["#X##########",
        "# ###   O###",
        "# #   ##  ##",
        "#   #X ##X##",
        "######    ##"]

#X##########
# ###   O###
# #   ##  ##
#   #X ##X##
######    ##

def enterTheDungeon(req, characterId):
    character = get_object_or_404(Character, pk=characterId)    
    """print(model1[0][0])
    labyrinthe = Labyrinth(cases=model1)
    print(labyrinthe.cases[0][0])

    character.numLigne = 4
    character.numColonne = 6"""

    #todo implement discovery function
    
    return HttpResponse("You enter a cold dungeon")


def lootBox(req):
    randomType = random.choice(list(WeaponType))
    randomDgt = random.randint(1,10)
    randomWeapon = Weapon(type=randomType, degats=randomDgt)
    randomWeapon.save()
    serial = WeaponSerializer(randomWeapon)
    return JsonResponse(serial.data, safe= False)

def generateEnemy(req):
    randomType = random.choice(list(EnemyType))
    randomDgt = random.randint(1,3)
    randomPv = random.randint(3,10)
    randomEnemy = Enemy(type=randomType, degats=randomDgt, pv=randomPv)
    randomEnemy.save()
    serial = EnemySerializer(randomEnemy)
    return JsonResponse(serial.data, safe= False)

def equiper(req, characterId, weaponId):
    character = get_object_or_404(Character, pk=characterId)
    weapon =  get_object_or_404(Weapon, pk=weaponId)
    character.arme = weapon
    character.save()
    return HttpResponse()

def fight(req, characterId, enemyId):
    character = get_object_or_404(Character, pk=characterId)
    enemy =  get_object_or_404(Enemy, pk=enemyId)

    while character.pv > 0 and enemy.pv > 0:
        enemy.pv -= character.arme.degats
        character.pv -= enemy.degats

    character.save()
    enemy.delete()

    if character.pv <=0:
        return HttpResponse("Game over", status=418)
    else:
        return HttpResponse(f"{character.nom} a terrasé son ennemi, il lui reste {character.pv} pv", status=200)
