# How To Execute Test Cases

---

## Prerequisites

- **Environment Setup**:
  - Python 3.x installed.
  - Install dependencies using `pip install -r requirements.txt`.
- **API Keys and Configuration**:
  - Set the `OPENAI_API_KEY` environment variable.
  - Ensure `config.py` is properly configured.

## Running the Application

1. **Start the Flask Server**:

   ```bash
   python app.py
   ```

2. **Access the Application**:

   - Open a web browser and navigate to `http://localhost:5001`.

## Executing Tests

- **Setup**:
  - Tests are written using `unittest` or `pytest`.
  - Ensure test scripts are located in the `tests/` directory.

- **Running Tests**:

  ```bash
  pytest tests/
  ```

- **Interpreting Results**:
  - Check the console output for passed and failed tests.
  - Review any errors or stack traces for debugging.

## Expected Outcomes

- **All tests pass**: Indicates the application is functioning as expected.
- **Failed tests**: Investigate and fix issues in the corresponding components.
- **Performance metrics**: Note any tests that take unusually long to execute.

--- 