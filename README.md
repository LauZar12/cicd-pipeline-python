# cicd-pipeline-python

## Team members
- Laura Danniela Zárate Guerrero
- Esteban Vergara Giraldo
- Jonathan Betancur Espinosa
- Miguel Angel Cock Cano

Repository for Group Workshop Deliverable 2.

## Project Structure

```
app/             -> Flask application (calculator)
tests/           -> Unit and acceptance tests
.github/workflows-> GitHub Actions
requirements.txt -> Python dependencies
```

---

## Setup

```bash
git clone https://github.com/LauZar12/cicd-pipeline-python.git
cd cicd-pipeline-python
python -m venv venv

# Activate venv
# On Windows:
venv\Scripts\activate
# On Linux or Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Run Tests

### General Tests

```bash
pytest -v
pytest --cov=app --cov-report=term-missing
```

### Code Quality Checks

```bash
flake8 app tests
isort --check-only app tests
pylint app tests
```

### Auto-correct Issues (if present)

```bash
black app tests
isort app tests
```

---

## Run the App

```bash
python -m app.app
```

Open in your browser: [http://localhost:5000](http://localhost:5000)

---

