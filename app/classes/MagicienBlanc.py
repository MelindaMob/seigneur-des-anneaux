import random
import time
from app.classes.Personnage import Personnage

class MagicienBlanc(Personnage):
    """Le magicien blanc genre Gandalf"""
    
    def __init__(self, nom="🧙‍♂️ Gandalf le Blanc"):
        super().__init__(nom)
        
        # liste des frappes du magicien
        self._frappes = [
            {"nom": "Éclair de lumière", "force": 15, "exp": 3, "emoji": "⚡"},
            {"nom": "Bouclier de Mithril", "force": 8, "exp": 2, "emoji": "🛡️"},
            {"nom": "Feu sacré d'Anor", "force": 25, "exp": 5, "emoji": "🔥"}
        ]
        self.cri_de_guerre = "Vous ne passerez pas!"
        self.compteur = 0  # je compte les attaques
    
    def frappe(self, cible, force=None):
        # choix aléatoire de l'attaque
        index = random.randint(0, len(self._frappes) - 1)
        attaque = self._frappes[index]
        
        print(f"\n⚔️  {self.nom} lance {attaque['nom']} {attaque['emoji']}")
        time.sleep(1)
        
        # test si la cible esquive
        esquive = cible.esquive()
        if esquive == True:
            print(f"  ↩️  {cible.nom} esquive l'attaque!")
            return False
        elif esquive == False:
            print(f"  💥 L'attaque touche!")
            cible.recoit_degat(self, attaque['force'])
            
            # incrémentation de l'exp
            ancienne_exp = self.experience
            nouvelle_exp = ancienne_exp + attaque['exp']
            self.experience = nouvelle_exp
            print(f"  📈 {self.nom} gagne {attaque['exp']} points d'expérience!")
            
            self.compteur = self.compteur + 1
            return True
    
    def get_nom(self):
        # pour récupérer le nom
        return self._nom