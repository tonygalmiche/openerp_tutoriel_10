# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 10",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 10 
===================================================

Le but de ce module est de montrer les différentes possibilités de personnalisation des listes.

Ce module installe le module account_voucher pour pouvoir ajouter des listes sur les factures

Le fichier `view.xml` contient les vues, actions et menus de ce module.

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["base","account_voucher"],  # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],              # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],              # Liste des fichiers XML à installer pour charger les données de démonstration

  "update_xml" : ["view.xml"],  # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)
                                # -> Chargement du fichier XML contenant la configuration des menus pour ce module

  "installable": True,          # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False               # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}





