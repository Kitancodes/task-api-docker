from typing import List
from app.models.task import Task
from datetime import datetime

class TaskService:
    def __init__(self):
        self.tasks: List[Task] = [
            Task(
                id=1,
                title="Deploy new staging environment",
                description="Provision VPS cluster and configure Nginx reverse proxy",
                completed=False,
                created_at=datetime.utcnow()
            ),
            Task(
                id=2,
                title="Set up CI/CD pipeline",
                description="Implement test, build, and push stages for Docker images",
                completed=False,
                created_at=datetime.utcnow()
            )
        ]
        self.counter = 3

    def get_tasks(self):
        return self.tasks

    def create_task(self, task: Task):
        task.id = self.counter
        task.created_at = datetime.utcnow()
        self.tasks.append(task)
        self.counter += 1
        return task
