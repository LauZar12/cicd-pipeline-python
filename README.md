# cicd-pipeline-python

## Team members:
- Laura Danniela Zárate Guerrero.
- Esteban Vergara Giraldo.
- Jonathan Betancur Espinosa.
- Miguel Angel Cock Cano.

Repository for Group Workshop Deliverable 2: CI Pipeline with Python, GitHub Actions, Docker, and OSS tools.

Initial structure:
- app/             -> Flask application (calculator)
- tests/           -> unit and acceptance tests (Selenium)
- .github/workflows-> GitHub Actions
- Dockerfile
- requirements.txt

````markdown
# Just a calculator app with tests.

---
Here are the steps in case you want to try it yourself. c:

## Setup
```bash
git clone https://github.com/LauZar12/cicd-pipeline-python.git
cd cicd-pipeline-python
python -m venv venv
# Activate venv.
# On Windows:
venv\Scripts\activate
# On Linux or Mac:
source venv/bin/activate

#Then
pip install -r requirements.txt
````

---

## To run general tests.

```bash
pytest -v
pytest --cov=app --cov-report=term-missing
```

---

## To test code quality.

```bash
flake8 app tests
black app tests
```

---

## Run the App

```bash
python -m app.app
```

Open [http://localhost:5000](http://localhost:5000)
