#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programme principal - Combat Seigneur des Anneaux
"""

import time
# j'importe les classes depuis app.classes
from app.classes.Personnage import Personnage
from app.classes.MagicienBlanc import MagicienBlanc  
from app.classes.RoiSorcier import RoiSorcier
import random


def afficher_titre():
    # affiche le titre du jeu
    print("\n" + "="*60)
    print("""
    ⚔️  COMBAT ÉPIQUE - SEIGNEUR DES ANNEAUX  ⚔️
         🧙‍♂️ Magicien Blanc VS Roi-Sorcier 👹
    """)
    print("="*60)
    time.sleep(2)


def afficher_status(j1, j2, num_tour):
    """fonction pour afficher les stats du combat"""
    print(f"\n{'='*20} TOUR {num_tour} {'='*20}")
    print("📊 STATUS DU COMBAT:")
    
    # pour le joueur 1
    vie_j1 = j1.vie - j1.degats
    if vie_j1 < 0:
        vie_j1 = 0
    barre = ""
    for i in range(0, int(vie_j1/10)):
        barre = barre + "█"
    for i in range(0, int((100-vie_j1)/10)):
        barre = barre + "░"
    print(f"\n  {j1.nom}")
    print(f"    Vie: [{barre}] {vie_j1}/{j1.vie}")
    print(f"    Exp: {j1.experience} points")
    
    # pour le joueur 2
    vie_j2 = j2.vie - j2.degats
    if vie_j2 < 0:
        vie_j2 = 0
    barre2 = ""
    for i in range(0, int(vie_j2/10)):
        barre2 = barre2 + "█"
    for i in range(0, int((100-vie_j2)/10)):
        barre2 = barre2 + "░"
    print(f"\n  {j2.nom}")
    print(f"    Vie: [{barre2}] {vie_j2}/{j2.vie}")
    print(f"    Exp: {j2.experience} points")
    print("="*50)


def combat():
    """fonction principale du combat"""
    
    # création des persos
    print("\n🎭 Préparation du combat...")
    gandalf = None
    sorcier = None
    gandalf = MagicienBlanc()
    sorcier = RoiSorcier()
    
    print(f"  ✅ {gandalf.nom} entre en scène!")
    print(f"  ✅ {sorcier.nom} entre en scène!")
    
    afficher_titre()
    
    print("\n🎬 LE COMBAT COMMENCE!")
    print(f"\n  {gandalf.nom}: « {gandalf.cri_de_guerre} »")
    print(f"  {sorcier.nom}: « {sorcier.cri_de_guerre} »")
    time.sleep(2)
    
    num_tour = 1
    combat_en_cours = True
    
    # boucle principale du combat
    while combat_en_cours == True:
        
        # je vérifie si quelqu'un est mort
        if gandalf.est_vivant() == False:
            combat_en_cours = False
            break
        if sorcier.est_vivant() == False:
            combat_en_cours = False
            break
            
        afficher_status(gandalf, sorcier, num_tour)
        time.sleep(1)
        
        # gestion des tours
        tour_actuel = Personnage.tour
        if tour_actuel == 'joueur1':
            print(f"\n🎯 Tour de {gandalf.nom}")
            resultat = gandalf.frappe(sorcier)
            Personnage.tour = 'joueur2'
        elif tour_actuel == 'joueur2':
            print(f"\n🎯 Tour de {sorcier.nom}")
            resultat = sorcier.frappe(gandalf)
            Personnage.tour = 'joueur1'
        
        num_tour = num_tour + 1
        time.sleep(2)
    
    # annonce du gagnant
    print("\n" + "🎆"*30)
    
    if gandalf.est_vivant() == True and sorcier.est_vivant() == False:
        print(f"\n🏆 VICTOIRE DE {gandalf.nom}!")
        print("✨ La lumière triomphe des ténèbres!")
    elif gandalf.est_vivant() == False and sorcier.est_vivant() == True:
        print(f"\n🏆 VICTOIRE DU {sorcier.nom}!")
        print("🌑 Les ténèbres recouvrent la Terre du Milieu...")
    
    print("🎆"*30)
    
    # stats finales
    tours_str = str(num_tour - 1)
    print(f"\n📜 Combat terminé en {tours_str} tours")
    print(f"⭐ Exp finale {gandalf.nom}: {gandalf.experience}")
    print(f"⭐ Exp finale {sorcier.nom}: {sorcier.experience}")


# programme principal
if __name__ == "__main__":
    try:
        combat()
        print("\n👋 Fin du combat épique!")
    except KeyboardInterrupt:
        print("\n\n⚠️ Combat interrompu!")
        pass
    except:
        print(f"\n❌ Une erreur est survenue")