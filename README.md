# Générateur de Mot de Passe Sécurisé

Ce projet Python permet de générer des mots de passe sécurisés, avec des options personnalisables, un indicateur de force et un thème sombre. L'application permet de choisir la longueur du mot de passe, d'inclure des chiffres et des caractères spéciaux, et d'évaluer la force du mot de passe généré.

## Fonctionnalités

- **Génération de mot de passe** : Choisissez la longueur, les options de chiffres et de caractères spéciaux.
- **Indicateur de force** : Visualisez la force du mot de passe généré avec un code couleur.
- **Copie dans le presse-papiers** : Copiez le mot de passe généré en un clic.
- **Thème sombre** : Une interface moderne et claire avec un thème sombre.

## Structure du projet

Voici la structure du projet et le rôle de chaque fichier/dossier :
passwordGenerator/
│
├── main.py                      # Point d’entrée principal de l’application
├── config/
│   └── theme.py                 # Couleurs et constantes de thème (sombre)
│
├── core/
│   ├── password_logic.py        # Logique de génération de mot de passe
│   └── strength_evaluator.py    # Évaluation de la force du mot de passe
│
├── ui/
│   ├── widgets.py               # Fonctions pour créer les éléments d’interface
│   └── layout.py                # Organisation de la fenêtre principale
│
└── utils/
│   ├── clipboard.py             # Fonctions utilitaires (copie presse-papiers, etc.)
└── README.md                    # Instructions

## Installation

### Prérequis
Avant de lancer l'application, vous devez installer les dépendances suivantes :
- **Tkinter** : Inclus par défaut avec Python.
- **pyperclip** : Bibliothèque pour copier dans le presse-papiers.
  
Vous pouvez installer `pyperclip` avec la commande suivante :
```bash
pip install pyperclip


### Lancer l’application
- Clonez ou téléchargez ce repository, puis placez-vous dans le dossier du projet et exécutez la commande :
python main.py

## Fonctionnement
	1.	Sélectionnez la longueur du mot de passe dans le champ approprié.
	2.	Choisissez si vous voulez des chiffres et des caractères spéciaux.
	3.	Cliquez sur Générer pour créer un mot de passe sécurisé.
	4.	La force du mot de passe sera affichée sous forme de barre colorée et étiquetée.
	5.	Cliquez sur Copier pour copier le mot de passe dans votre presse-papiers.# PasswordGenerator
