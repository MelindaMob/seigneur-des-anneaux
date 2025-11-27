import random
import time
from app.classes.Personnage import Personnage

class RoiSorcier(Personnage):
    """Le roi sorcier d'Angmar le méchant"""
    
    def __init__(self, nom="👹 Roi-Sorcier d'Angmar"):
        super().__init__(nom)
        
        # je crée la liste de frappes
        self._frappes = list()
        self._frappes.append({"nom": "Lame de Morgul", "force": 18, "exp": 3, "emoji": "🗡️"})
        self._frappes.append({"nom": "Souffle des Nazgûl", "force": 12, "exp": 2, "emoji": "💀"})
        self._frappes.append({"nom": "Ténèbres du Mordor", "force": 22, "exp": 4, "emoji": "🌑"})
        
        self.cri_de_guerre = "Aucun homme ne peut me tuer!"
        self.nb_attaques = 0
    
    def frappe(self, cible, force=None):
        # je choisis une attaque au hasard
        numero = random.randint(0, 2)
        if numero == 0:
            attaque = self._frappes[0]
        elif numero == 1:
            attaque = self._frappes[1]
        elif numero == 2:
            attaque = self._frappes[2]
        
        self.nb_attaques = self.nb_attaques + 1
        
        print(f"\n⚔️  {self.nom} utilise {attaque['nom']} {attaque['emoji']}")
        time.sleep(1)
        
        # test d'esquive un peu compliqué
        if not cible.esquive() == False:
            print(f"  ↩️  {cible.nom} esquive miraculeusement!")
            return False
        else:
            print(f"  💥 L'attaque frappe violemment!")
            cible.recoit_degat(self, attaque['force'])
            
            # j'augmente l'exp
            self._experience = self._experience + attaque['exp']
            print(f"  📈 {self.nom} gagne {attaque['exp']} points d'expérience!")
            
            # tous les 3 attaques il dit sa phrase
            if self.nb_attaques % 3 is 0:
                print(f"  💬 {self.nom}: « {self.cri_de_guerre} »")
            
            return True
    
    def get_experience(self):
        # getter pour l'exp
        return self._experience
    
    def set_experience(self, val):
        # setter pour l'exp
        self._experience = val