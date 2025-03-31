from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from enemy.models import Enemy
from enemy.serializer import EnemySerializer

class EnemyView(TemplateView):
    def get(self, req):
        enemies = Enemy.objects.all() # retrieve queryset
        # serializing (turn an object into a json)
        enemySerializer = EnemySerializer(enemies, many=True)
        return JsonResponse(enemySerializer.data, safe=False)
        
    def delete(self, req: HttpRequest, id):
        myCharacter = get_object_or_404(Enemy, pk=id)
        myCharacter.delete()
        return HttpResponse()