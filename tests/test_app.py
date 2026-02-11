import pytest
from fastapi.testclient import TestClient
import sys
import app

client = TestClient(app.app)

# Automatically clear tasks before each test
@pytest.fixture(autouse=True)
def clear_tasks():
    app.tasks_db.clear()  # reset the in-memory task list
    app.task_id_counter = 1

def test_root_health_check():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "Task Management API is running"

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_create_task():
    task_data = {"title": "Test Task", "description": "This is a test task", "completed": False}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Task"

def test_get_task_by_id():
    task_data = {"title": "Fetch Task"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_update_task():
    task_data = {"title": "Update Task"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    update_data = {"completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["completed"] is True

def test_delete_task():
    task_data = {"title": "Delete Task"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

def test_get_nonexistent_task():
    response = client.get("/tasks/999")
    assert response.status_code == 404
