# Pendu — Python / pygame

![pythonversion](https://img.shields.io/badge/python-3.x-blue)

Un simple Pendu développé en Python et utilisant pygame pour l'interface graphique.

## Présentation

### Le jeu du pendu

Le pendu est un jeu de lettres classique qui consiste à deviner un mot secret en proposant des lettres, une à une, avant que le dessin d’un pendu ne soit complété. C’est à la fois un jeu de réflexion et de vocabulaire.

### But du jeu

Le but est de trouver le mot secret avant de faire trop d’erreurs. Chaque lettre incorrecte rapproche le joueur de la défaite.

### Règles principales

1. Un mot est choisi secrètement par l’ordinateur.

2. Le mot est représenté par des tirets, une pour chaque lettre.

3. Le joueur propose une lettre à la fois.

4. Si la lettre est présente dans le mot, elle est révélée à sa/ses position(s).

5. Si la lettre n’est pas dans le mot, une partie du pendu est dessinée (tête, corps, bras, jambes…).

6. Le joueur gagne s’il trouve toutes les lettres avant que le pendu ne soit complet.

7. Le joueur perd si le dessin du pendu est terminé avant que le mot soit trouvé   

## Installation (Windows uniquement)

tbd

## Fonctionnalités

- Jeu du pendu classique avec une interface pygame.
- Gestion complète de la liste des mots :
    - Ajout de mots par l'utilisateur.
    - Suppression par cas ou complète des mots.
    - Réinitialisation des mots à leur état d'origine.
- Gestion de scores :
    - Système de nom du joueur.
    - Système de classement persisté pour sauvegarder les résultats.
    - Historique de parties, permettant de consulter les scores précédents.

## Contrôles

- **Souris** : Cliquer sur les boutons (Menu/Scores/Options/Pop-ups)
- **Échap** : Revenir en arrière/quitter le jeu (par rapport à l'écran affiché)

Dans **Jouer** :
- Clavier :
    - Entrer les lettres avec le clavier
        - Caractères acceptés : lettres

Dans **Scores** :

- **Souris** :
    - Utiliser les flèches `<` / `>` pour changer de pages (s'il y a plus de 10 scores)

Dans **Options → Mots → Ajouter mot** et les **Pop-ups** pour entrer **le nom**  :

- **Clavier** :
    - Taper les lettres avec le clavier
        - Caractères acceptés : lettres et tiret  
    - **Retour arrière**: Supprimer le dernier caractère entrée
    - **Enter**: Valider le mot entrée

Dans **Options → Mots → Retirer mot** :

- **Souris** :
    - Cliquer sur un mot pour le supprimer
    - Utiliser les flèches `<` / `>` pour changer de pages (s'il y a plus de 20 mots)

## Exécuter depuis le code source

### Prérequis

- Python 3.x
- pygame -> ```python -m pip install pygame```

## Exécuter

À partir du dossier racine du projet (le dossier qui contient `main.py`), exécuter :

```bash
python main.py
```

## Auteurs

Ce projet a été réalisé par [Nicolas](https://github.com/nicolas-riera), [Arthur](https://github.com/arthur-georget) et [Achraf](https://github.com/achraf-nait-belkacem).
