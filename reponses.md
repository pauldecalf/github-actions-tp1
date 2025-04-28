3. Dans ce repository, crée un répertoire .github/workflows. Quelle est l'utilité de ce
   répertoire ?
- Cela sert a définir des workflows pour github actions
  
10. Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions.
    Que constates-tu ?
- Il apparait dans les workflows de github actions avec le status
  
11. Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à
    "positif" par exemple).
    Que se passe-t-il lors du prochain push ?
- Je constate que le workflow de test apparait comme etant en " Failure"  
  
14. Que constates-tu après le push ?
- Que désormais le test passe en "success"  

