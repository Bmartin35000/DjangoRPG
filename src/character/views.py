import json
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from character.models import Character
from character.serializer import CharacterSerializer

class CharacterView(TemplateView):
    def get(self, req):
        characters = Character.objects.all() # retrieve queryset
        # serializing (turn an object into a json)
        characterSerializer = CharacterSerializer(characters, many=True)
        return JsonResponse(characterSerializer.data, safe=False)
    
    def post(self, req: HttpRequest):
        # deserializing (turn json into an object)
        bodyDict = json.loads(req.body) # json to dict
        characterSerializer = CharacterSerializer(data=bodyDict) # dict to modelSerializer
        if characterSerializer.is_valid():
            characterSerializer.save()
            return HttpResponse(status=201)
        else:
            return JsonResponse(characterSerializer.errors, status=400)
        
    def put(self, req: HttpRequest):
        bodyDict = json.loads(req.body)
        charInDb = get_object_or_404(Character, pk=bodyDict["id"])
        # updating the charInDB with the bodyDict
        characterSerializer = CharacterSerializer(charInDb, data=bodyDict)
        if characterSerializer.is_valid():
            characterSerializer.save()
            return HttpResponse(status=201)
        else:
            print(characterSerializer.errors)
            return JsonResponse(characterSerializer.errors, status=400)
        
    def delete(self, req: HttpRequest, id):
        myCharacter = get_object_or_404(Character, pk=id)
        myCharacter.delete()
        return HttpResponse()
    
    def delete(self, req: HttpRequest):
        myCharacters = Character.objects.all()
        myCharacters.delete()
        return HttpResponse()