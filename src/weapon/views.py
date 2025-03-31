from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from weapon.models import Weapon
from weapon.serializer import WeaponSerializer

class WeaponView(TemplateView):
    def get(self, req):
        weapons = Weapon.objects.all() # retrieve queryset
        # serializing (turn an object into a json)
        weaponSerializer = WeaponSerializer(weapons, many=True)
        return JsonResponse(weaponSerializer.data, safe=False)
        
    def delete(self, req: HttpRequest, id):
        myCharacter = get_object_or_404(Weapon, pk=id)
        myCharacter.delete()
        return HttpResponse()