# IUT: Chaine CI/CD

@author Rxinui

## Atelier 1 : Single Page Web
### Pré-requis

Les technologies qui seront utilisées lors de cet atelier nécessitent :

Une installation de :

- [git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)

Un compte utilisateur sur :

- [Github (intégration)](https://github.com/login)
- [Deta.sh (déploiement)](https://web.deta.sh/)

### Rappels: commandes utiles

- Enregistrer les modifications : `git commit -a -m "<message de commit>"`
- Pousser les modifications sur GitHub pour la 1er fois : `git push --set-upstream origin atl1_actif`
- Pousser les modifications sur GitHub : `git push`

### Code source

Le dossier `atelier/` contient le code source de l'application. N'oubliez pas de vous placez dans ce dossier dans votre chaine CI/CD pour lancer les scripts.

- `atelier/init.sh` initialise un environnement Python avec les dépendances nécessaires au bon fonctionnement de l'application
- `atelier/run.sh` démarre l'application Python dans le bon environnement
- `atelier/main.py` correspond au code source de l'application. C'est une API REST basique qui affiche quelques écoles d'supérieurs de Toulouse.
- `atelier/ecoles.json` contient les données nécessaires au fonctionnement de l'application. Répertorie un extrait des écoles d'supérieurs de Toulouse.

### Exercice

Intégrer et déployer une API REST écrit en Python. L'API est construit par FastAPI et permet de lister les écoles d'supérieurs de Toulouse disponible dans notre base de données.

Dans un premier temps, on va établir une chaine CI/CD en 2 taches :`build-test` puis `deploy`.
Dans un second temps, on rajoutera une fonctionnalitée à notre API puis on vérifira que la chaine CI/CD créé est bien fonctionnelle.

#### Partie CI

1. **TODO**: Compléter la chaine CI/CD `.github/workflows` pour qu'il se déclenche au `push` de votre branche de travail actuelle.

2. **TODO**: Écrire l'étape d'initialisation de l'environnement en se servant du script `atelier/init.sh`

3. **TODO**: Écrire l'étape de démarrage du serveur python en se servant du script `atelier/run.sh`

4. **TODO**: Écrire l'étape de test en lancant la commande `pytest` depuis le dossier `atelier/`

5. **TODO**: Enregistrer les modifications et pousser les sur votre GitHub. Regarder votre chaine CI/CD. Si c'est un succès alors passez à la partie CD sinon corriger vos erreurs puis répéter cette étape.

#### Partie CD

1. **TODO**: Utiliser l'action [deta-deploy-action](https://github.com/marketplace/actions/deploy-to-deta) pour déployer l'API Python.

*Note:* Créer un **Access Tokens** sur votre compte Deta à l'URL suivante https://web.deta.sh/home/<username>/ et copier le pour l'utiliser sur deta-deploy-action.

2. **TODO**: Enregistrer les modifications et pousser les sur votre GitHub. Regarder votre chaine CI/CD. Si c'est un succès alors passez vérifier sur votre site en production chez Deta.sh. Si l'API est accessible alors le déploiement est un succès sinon corriger vos erreurs puis répéter cette étape.

À présent, rajoutant une fonctionnalitée à notre API.

3. **TODO**: À l'aide du code source présent dans `main.py`, compléter la méthode `ajouter_ecole`.

- La méthode `ajouter_ecole` doit être déclenchée par un `HTTP GET` sur `/ecoles/new` avec les query paramètres GET `nom` et `groupe`.
- La méthode renvoie un `dict` de l'école ajouté

4. **TODO**: Enregistrer les modifications et pousser les sur votre GitHub. Sur votre site en production (deta.sh), ajouter votre IUT comme nouvelle école.

5. **TODO**: Afficher toutes les écoles et vérifier que votre IUT est présente.

*That's all folks :)*