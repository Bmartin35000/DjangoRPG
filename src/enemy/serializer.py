from rest_framework import serializers

from enemy.models import Enemy

class EnemySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Enemy
        fields = '__all__'