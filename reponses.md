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

18. Crée une nouvelle branche, fais-y des modifications, puis crée une Pull Request. Que se passe-t-il avec ton workflow de commentaires ?

- Après avoir créé une branche, fait une modification et ouvert une Pull Request, le workflow pr-comment.yml s'est exécuté automatiquement.
Un commentaire a été ajouté automatiquement à la Pull Request avec le message :
👋 Thanks for the PR! The automated tests will run shortly.
Cela confirme que le workflow de commentaires fonctionne correctement.

18. Crée une nouvelle branche, fais-y des modifications, puis crée une Pull Request.
    Que se passe-t-il avec ton workflow de commentaires ?
- Il n'a pas fonctionner directement car celui-ci s'appliqu'au prochain MR 


21. Que constates-tu après avoir poussé ces modifications ?
- Il ya  un badge dan,s le readme avec écrit passed :Build Status

23. Crée un workflow .github/workflows/docker.yml qui construit et teste l'image Docker.

- J'ai créé un fichier docker.yml dans .github/workflows.
Ce workflow construit une image Docker à partir du Dockerfile et l’exécute pour tester le fonctionnement de l’application.
Après avoir poussé les modifications, le workflow s'est déclenché correctement et a validé que l'image Docker fonctionne.


