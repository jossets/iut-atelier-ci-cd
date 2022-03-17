#!/bin/bash
echo "> Lancement l'environnement virtuel python"
source ./pyvenv/bin/activate
cd server/
echo "> Initialisation de l'environnement virtuel python"
pip install pip --upgrade;
pip install -r requirements.txt;