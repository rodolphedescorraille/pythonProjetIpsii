démarrer l'appli :

suivre les indication du fichier sujet.md

sans bdd (pour exercice 1):

  executer les commandes : (dans le repertoire "share-code-plus")

    python sharecode.py
    
avec bdd (à partir de l'exercice 2):
  
  executer les commandes : (dans le repertoire "share-code-plus")
  
    python initdb.py // attention commande a executer seulement une fois sinon petite erreur
    python sharecodedb.py
    
    
fichier utiliser pour les exercice et modification apporté:
    
  - ex 1 : (fonctionnelle)
  j'ai modifier le fichier model.py et sharecode.py pour sauvgarder 
  le type de language utiliser en extension sur le fichier
  
  -ex 2 : (fonctionnelle)
  j'ai créer des copie des fichier model.py -> model_sqlite.py 
  et sharecode.py -> sharcodedb.py
  
  -ex 3 : (non fonctionelle :/)
  je n'ai pas eu le temp de le finire j'ai juste eu le temps de 
  créer la table dans le initdb.py.
  
  j'aurais ensuite utilisé des fonctions python pour récupérer les infos (IP,navigateur...)
  j'aurais stoqué les infos en BDD dans la nouvelle table
  j'aurais récupérer les info via requet sql un peux a la manière "get_last_entries_from_files"
  et les auraient affiché avec un ordre lié au lastCommit (DATETIME) du plus récent au vieux sur la route admin
  
  
  