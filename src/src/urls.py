from django.contrib import admin
from django.urls import include, path

from src.views import lootBox, equiper, generateEnemy, fight, enterTheDungeon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('character/', include("character.urls")),
    path('weapon/', include("weapon.urls")),
    path('enemy/', include("enemy.urls")),
    path('lootBox/', lootBox),
    path('generateEnemy/', generateEnemy),
    path('enterTheDungeon/<int:characterId>', enterTheDungeon),
    path('equip/<int:characterId>/<int:weaponId>', equiper),
    path('fight/<int:characterId>/<int:enemyId>', fight),
]
