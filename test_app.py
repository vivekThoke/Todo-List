import pytest

from app import TodoList  # assuming your main app file is named app.py

@pytest.fixture
def todo_list():
    """Fixture to create a fresh TodoList instance for each test"""
    return TodoList()

def test_todo_list_initialization():
    """Test that TodoList is initialized with an empty list"""
    todo = TodoList()
    assert len(todo.tasks) == 0

def test_add_task():
    """Test adding a task to the list"""
    todo = TodoList()
    todo.add_task("Test task")
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["task"] == "Test task"
    assert todo.tasks[0]["completed"] is False