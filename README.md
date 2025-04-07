# calculatorApi-Python – API Calculatrice en Flask

Une API web simple développée avec Flask (Python 3.11), permettant d'effectuer des opérations mathématiques de base (`add`, `sub`, `mul`, `div`) via HTTP.

## Lancer en local

### 1. Installer les dépendances

```bash
pip install -r requirements.txt

python run.py

docker build -t flask-calc-api .
docker run -p 8081:8081 flask-calc-api
