# Code Runner

Code Runner is a lightweight Flask-based microservice designed to execute Python scripts and run unit tests for the RPL service application. It is primarily used to facilitate the exercise delivery functionality by allowing users to submit scripts along with test cases and receive automated test results.

## Features

- Accepts Python scripts and corresponding test cases via a JSON API.
- Runs unit tests using `pytest` in a sandboxed environment.
- Returns structured test results including success and failure reports.
- Minimal dependencies (only Flask and Pytest required).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/WillyTonkas/code-runner.git
   cd code-runner
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```

## API Usage

### Endpoint: `/run-tests`

#### Request Format

Send a `POST` request with a JSON body containing:

```json
{
  "script": "def add(a, b):\n    return a + b",
  "tests": "from script import add\ndef test_add():\n    assert add(2, 3) == 5\n    assert add(-1, 1) == 0"
}
```

#### Response Format

```json
{
  "stdout": "...",  
  "stderr": "...",  
  "returncode": 0  
}
```

- `stdout`: Standard output from `pytest`.
- `stderr`: Error messages if any.
- `returncode`: Exit code (0 means success, non-zero indicates failure).

## Deployment

This application is containerized and can be deployed via Docker. To build and run the container:

```sh
# Build the Docker image
docker build -t code-runner .

# Run the container
docker run -p 5000:5000 code-runner
```

## License

This project is licensed under the MIT License.
