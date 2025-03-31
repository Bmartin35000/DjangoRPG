import json
from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView

from character.models import Character
from character.serializer import CharacterSerializer

# Create your views here.

class CharacterView(TemplateView):
    def get(self, req):
        characters = Character.objects.all()
        print(characters)
        return JsonResponse("ok", safe=False)
    
    def post(self, req: HttpRequest):
        bodyDict = json.loads(req.body) # json to dict
        characterSerializer = CharacterSerializer(data=bodyDict) # dict to modelSerializer
        if characterSerializer.is_valid():
            characterSerializer.save()
            return JsonResponse("ok", safe=False)
        else:
            print(characterSerializer.errors)
            return JsonResponse("ko", safe=False, status=400)
            