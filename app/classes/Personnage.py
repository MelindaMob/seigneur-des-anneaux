from abc import ABC, abstractmethod
import random

class Personnage(ABC):
    """Classe abstraite pour les personnages du jeu"""
    
    # variable de classe publique comme demandé
    tour = 'joueur1'
    
    def __init__(self, nom):
        # propriétés privées avec le _
        self._nom = nom
        self._vie = 100
        self._experience = 0
        self._degats = 0
        self._frappes = []  # sera rempli dans les classes filles
    
    # getters et setters avec @property
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, value):
        # verif que le nom est pas vide
        if value == "" or value == None:
            raise ValueError("Le nom ne peut pas être vide!")
        else:
            self._nom = value
    
    @property
    def vie(self):
        return self._vie
    
    @vie.setter  
    def vie(self, value):
        # je mets des limites pour la vie
        if value < 0:
            self._vie = 0
        elif value > 100:
            self._vie = 100
        else:
            self._vie = value
    
    @property
    def experience(self):
        return self._experience
    
    @experience.setter
    def experience(self, value):
        # pas d'exp négative
        if value < 0:
            print("⚠ L'expérience ne peut pas être négative!")
            return
        else:
            self._experience = value
    
    @property
    def degats(self):
        return self._degats
    
    @degats.setter
    def degats(self, value):
        if value < 0:
            self._degats = 0
        else:
            self._degats = value
    
    @property
    def frappes(self):
        return self._frappes
    
    @frappes.setter
    def frappes(self, value):
        self._frappes = value
    
    # méthode abstraite à implémenter dans les classes filles
    @abstractmethod
    def frappe(self, cible, force):
        pass
    
    def esquive(self):
        """30% de chance d'esquiver"""
        nombre = random.randint(1, 10)
        if nombre <= 3:
            return True
        else:
            return False
    
    def recoit_degat(self, adversaire, force_frappe):
        """méthode pour recevoir des dégâts"""
        # calcul des dégats comme dans la consigne
        exp_adversaire = adversaire.experience
        degats_totaux = force_frappe + exp_adversaire
        self.degats = self.degats + degats_totaux
        
        # affichage obligatoire
        vie_restante = self.vie - self.degats
        if vie_restante < 0:
            vie_restante = 0
        print(f"\n  💔 {self.nom} reçoit {degats_totaux} points de dégâts!")
        print(f"  ❤️  Vie restante: {vie_restante}/{self.vie}")
        print(f"  ⭐ Expérience: {self.experience}")
    
    def est_vivant(self):
        # vérifie si le perso est encore vivant
        if self.degats >= self.vie:
            return False
        else:
            return True