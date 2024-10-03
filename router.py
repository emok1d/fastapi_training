from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"message": "Task added successfully", "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}