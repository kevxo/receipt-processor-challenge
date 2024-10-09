# Receipt Processor Service

### Run Service Requirements
    - With Docker:
        docker build -t my_fastapi_service .
        docker run -d -p 80:80 --name fastapi-container my_fastapi_service

    - Run local
        Make sure you have python3.11
            - Be sure to be in virtual environment `python -m venv .venv` or `python3.11 -m venv .venv`
            - `pip install -r requirements.txt`
            - `fastapi dev main.py`
        Run Tests
            - python -m pytest tests

    Make sure you head to `http://0.0.0.0/docs` when using docker or `http://127.0.0.1:8000/docs` locally



### Quick Demo


https://github.com/user-attachments/assets/88060e72-6dd5-42a3-9dcb-be7e63eb841e


