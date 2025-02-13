# Todo List Application

This is a simple Todo List application built with Flask and SQLAlchemy. It allows you to add, edit, and delete tasks.

## Project Structure

```
__pycache__/
    app.cpython-310.pyc
    test_app.cpython-310-pytest-8.3.4.pyc
.gitignore
.pytest_cache/
    .gitignore
    CACHEDIR.TAG
    README.md
    v/
        cache/
            lastfailed
            nodeids
            stepwise
.vercel/
    .vercel/project.json
    .vercel/README.txt
app.py
requirements.txt
tasks.db
templates/
    templates/add_task.html
    templates/edit_task.html
    templates/index.html
test_app.py
vercel.json
```

## Prerequisites

- Python 3.10 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/vivekthoke/todo-list.git
cd todo-list
```

2. Create a virtual environment:

```sh
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```sh
venv\Scripts\activate
```


4. Install the required packages:

```sh
pip install -r requirements.txt
```

## Running the Application

1. Initialize the database:

```sh
python -c "from app import db; db.create_all()"
```

2. Run the Flask application:

```sh
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000` to see the application.

## Running Tests

To run the tests, use `pytest`:

```sh
pytest
```
