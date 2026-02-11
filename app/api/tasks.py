from fastapi import APIRouter
from app.models.task import Task
from app.services.task_service import TaskService

router = APIRouter(tags=["tasks"])

task_service = TaskService()

@router.get("/tasks")
def list_tasks():
    """
    List all tasks
    """
    return task_service.get_tasks()


@router.post("/tasks")
def create_task(task: Task):
    """
    Create a new task
    """
    return task_service.create_task(task)
