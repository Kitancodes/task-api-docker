from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models import Task, TaskCreate, TaskUpdate
from datetime import datetime
from typing import List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks - DevOps Portfolio Project",
    version="1.0.0"
)

# In-memory storage
tasks_db: List[Task] = []
task_id_counter = 1


@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint"""
    logger.info("Health check endpoint called")
    return {
        "message": "Task Management API is running",
        "version": "1.0.0",
        "status": "healthy"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "total_tasks": len(tasks_db)
    }


@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
async def get_tasks():
    """Get all tasks"""
    logger.info(f"Fetching all tasks. Total count: {len(tasks_db)}")
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
async def get_task(task_id: int):
    """Get a specific task by ID"""
    logger.info(f"Fetching task with ID: {task_id}")
    
    task = next((task for task in tasks_db if task.id == task_id), None)
    
    if not task:
        logger.warning(f"Task with ID {task_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
async def create_task(task_data: TaskCreate):
    """Create a new task"""
    global task_id_counter
    
    logger.info(f"Creating new task: {task_data.title}")
    
    new_task = Task(
        id=task_id_counter,
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        created_at=datetime.now()
    )
    
    tasks_db.append(new_task)
    task_id_counter += 1
    
    logger.info(f"Task created successfully with ID: {new_task.id}")
    return new_task


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
async def update_task(task_id: int, task_data: TaskUpdate):
    """Update an existing task"""
    logger.info(f"Updating task with ID: {task_id}")
    
    task = next((task for task in tasks_db if task.id == task_id), None)
    
    if not task:
        logger.warning(f"Task with ID {task_id} not found for update")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    # Update only provided fields
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed
    
    logger.info(f"Task {task_id} updated successfully")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
async def delete_task(task_id: int):
    """Delete a task"""
    global tasks_db
    
    logger.info(f"Deleting task with ID: {task_id}")
    
    task = next((task for task in tasks_db if task.id == task_id), None)
    
    if not task:
        logger.warning(f"Task with ID {task_id} not found for deletion")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    
    tasks_db = [t for t in tasks_db if t.id != task_id]
    logger.info(f"Task {task_id} deleted successfully")
    
    return None


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Task Management API...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
