from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_health_check():
    """Test the root endpoint returns healthy status"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "Task Management API is running"


def test_health_endpoint():
    """Test the detailed health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "total_tasks" in data


def test_get_tasks_empty():
    """Test getting tasks when none exist"""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task():
    """Test creating a new task"""
    task_data = {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data


def test_get_task_by_id():
    """Test getting a specific task by ID"""
    # First create a task
    task_data = {"title": "Task to fetch", "description": "Test"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    
    # Then fetch it
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Task to fetch"


def test_get_nonexistent_task():
    """Test getting a task that doesn't exist"""
    response = client.get("/tasks/99999")
    assert response.status_code == 404


def test_update_task():
    """Test updating an existing task"""
    # Create a task
    task_data = {"title": "Task to update", "description": "Original"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    
    # Update it
    update_data = {"completed": True, "description": "Updated description"}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True
    assert data["description"] == "Updated description"
    assert data["title"] == "Task to update"


def test_delete_task():
    """Test deleting a task"""
    # Create a task
    task_data = {"title": "Task to delete"}
    create_response = client.post("/tasks", json=task_data)
    task_id = create_response.json()["id"]
    
    # Delete it
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
