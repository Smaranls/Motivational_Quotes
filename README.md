12-Factor FastAPI Microservice



Overview

This is a small FastAPI-based microservice built to demonstrate the application of the 12-Factor App principles.

The app offers a simple utility (e.g., health check endpoint or a basic calculator) and follows best practices including environment-based configuration, containerization, automated testing, CI/CD, and clear documentation.



Features

- Configuration via environment variables using Pydantic
- Clear, modular project structure
- Git with branching strategy and pre-commit hooks
- Unit testing with pytest
- Dockerized for easy deployment
- GitHub Actions for CI (linting, tests, Docker build)
- Basic documentation included


Getting Started



Prerequisites

- Python 3.9+
- Docker (optional, but recommended)
- Git


Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```
cd your-repo-name



Running Locally



### 1. Create a virtual environment and activate it

python -m venv venv

```bash
source venv/bin/activate   # On Windows: venv\Scripts\activate
```


### 2. Install dependencies

```bash
pip install -r requirements.txt
```


### 3. Set environment variables (example)

```bash
export APP_ENV=development
```
```bash
export API_KEY=your_api_key_here
```


### 4. Run the FastAPI app

```bash
uvicorn app.main:app --reload
```


5. Access the app at http://127.0.0.1:8000



6. Open API docs at http://127.0.0.1:8000/docs



Running with Docker



### 1. Build the Docker image

```bash
docker build -t fastapi-12factor-app .
```


### 2. Run the container

```bash
docker run -d -p 8000:8000 --env-file .env fastapi-12factor-app
```


3. Visit http://localhost:8000 or http://localhost:8000/docs



Configuration



All configuration is managed via environment variables and validated using Pydantic settings.



### Example environment variables

- APP_ENV (development, production)
## - API_KEY

- DATABASE_URL (if applicable)


Use a .env file or your system environment to manage these values.



Testing



### Run tests with pytest



```bash
pytest tests/
```


Tests include unit and integration tests to verify functionality.



## CI/CD



### GitHub Actions workflows run automatically on push to

- Lint code with flake8
- Run tests with pytest
- Build Docker image


Check .github/workflows/ci.yml for workflow details.



Project Structure



.

├── app/

│   ├── main.py          # FastAPI entrypoint

│   ├── config.py        # Configuration management with Pydantic

│   ├── api/             # API route modules

│   ├── services/        # Business logic / utility functions

│   └── tests/           # Test cases

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env.example         # Sample env file

├── .pre-commit-config.yaml

├── README.md

└── .github/

└── workflows/

└── ci.yml      # GitHub Actions workflow



VSCode Configuration (Optional)



VSCode settings and recommended extensions are included in .vscode/ for consistent development experience.


Thank you for checking out this 12-Factor FastAPI project! 🚀
