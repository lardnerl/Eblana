from django.contrib import admin
from database.models import *


class charFeatsInLine(admin.StackedInline):
    model = CharacterFeat
    extra = 6
    
class Character (admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['owner','name','idspecies','xp','body','armour','mana','isfinished']})
    ]
    inlines = [charFeatsInLine]


# Register your models here.
admin.site.register(Effect)
admin.site.register(Duration)
admin.site.register(Call)
admin.site.register(Prefix)
admin.site.register(Species)
admin.site.register(Character)
admin.site.register(Class)
admin.site.register(Feat)
admin.site.register(FeatType)
admin.site.register(CharacterClass)
admin.site.register(CharacterFeat)
admin.site.register(ClassFeat)
admin.site.register(Spell)
admin.site.register(ClassSpell)
admin.site.register(CharacterSpell)
admin.site.register(UsersDetails)
admin.site.register(Lore)
admin.site.register(ClassLore)
admin.site.register(CharacterLore)

