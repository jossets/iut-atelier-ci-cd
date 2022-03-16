"""API REST code source

@author Rxinui
"""
import json
from typing import Optional
from fastapi import FastAPI, HTTPException

BDD_PATH = "./ecoles.json"
app = FastAPI()


def __get_ecoles() -> dict:
    """Charge et retourne les écoles disponibles dans la BDD.

    Returns:
        dict: écoles
    """
    with open(BDD_PATH) as fp:
        return json.load(fp)


def __add_ecole(nom: str, groupe: str) -> dict:
    """Ajoute une école selon son {nom} et son {groupe} dans la BDD.

    Args:
        nom (str): nom école
        groupe (str): groupe école

    Returns:
        dict: école ajoutée
    """
    ecoles = __get_ecoles()
    ecoles[len(ecoles) + 1] = {"nom": nom, "groupe": groupe}
    with open(BDD_PATH, "w") as fo:
        json.dump(ecoles, fo, indent=2)
    return ecoles[len(ecoles)-1]


@app.get("/")
def home() -> dict:
    """Affiche une présentation de l'API.

    Returns:
        dict: présentation au format JSON
    """
    return {
        "message": "Bienvenue à l'atelier 1. Cette API liste les écoles d'supérieurs de Toulouse.",
        "routes": {
            "/ecoles": {
                "GET": {
                    "description": "Liste toutes les écoles d'supérieurs de Toulouse"
                }
            },
            "/ecoles?groupe={groupe}": {
                "GET": {
                    "description": "Liste toutes les écoles d'supérieurs d'un {groupe} donné (ie. INP, UT...)",
                    "argument": "groupe",
                }
            },
            "/ecoles/{ecole_id}": {
                "GET": {
                    "description": "Retourne l'école de l'{ecole_id} donné. L'{ecole_id} est un nombre allant de 1 à 10 (nombre totale d'écoles)"
                }
            },
        },
    }


@app.get("/ecoles")
def ecoles(groupe: Optional[str] = None) -> dict:
    """Liste tous les écoles disponible dans la base de données.

    Args:
        groupe (Optional[str], optional): Filtre les écoles par leur groupe. Defaults to None.

    Returns:
        dict: écoles selon les filtres donnés en format JSON
    """
    return (
        {
            _id: ecole
            for _id, ecole in __get_ecoles().items()
            if ecole["groupe"] == groupe
        }
        if groupe
        else __get_ecoles()
    )


@app.get("/ecoles/{ecole_id}")
def ecole_par_id(ecole_id: str) -> dict:
    """Liste l'école possédant l'id {ecole_id}.

    Args:
        ecole_id (str): identifiant de l'école

    Raises:
        HTTPException: {ecole_id} inconnu

    Returns:
        dict: école en format JSON
    """
    ecole = __get_ecoles().get(ecole_id)
    if not ecole:
        raise HTTPException(
            status_code=404,
            detail=f"Ecole pour id={ecole_id} est inexistante dans notre base de données.",
        )
    return ecole


# TODO a completer
def ajouter_ecole(nom: str, groupe: str) -> dict:
    """Ajoute une école dans la BDD par les paramètres {nom} et {groupe}.

    Args:
        nom (str): nom école
        groupe (str): groupe école
    Returns:
        dict: Renvoie l'école qui a été ajoutée
    """
    # TODO a completer
    return 
