# Translation Frontend

### How to Run
Execute the following series of commands and you may find happiness:
```bash
git clone https://github.com/Agent-Artificial/translation-frontend.git
cd translation-frontend # Clone and cd into this repository
poetry install # Install dependencies with poetry
poetry run fastapi run frontend/main.py # Run the fastapi with poetry
```

### How to build
Simply:

```
docker build . -t Agent-Artificial/translation-frontend:dev
docker run -p 8000:8000 Agent-Artificial/translation-frontend:dev
```