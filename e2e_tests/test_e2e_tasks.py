import requests

BASE_URL = "http://127.0.0.1:8000"


# создание задачи
def test_user_creates_task():
    response = requests.post(
        f"{BASE_URL}/tasks/",
        json={
            "title": "E2E Task",
            "description": "task from end to end test"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "E2E Task"
    assert data["completed"] == False


# завершение задачи
def test_user_completes_task():
    tasks_resp = requests.get(f"{BASE_URL}/tasks/")
    assert tasks_resp.status_code == 200

    tasks = tasks_resp.json()
    task_id = tasks[0]["id"]

    complete_resp = requests.put(f"{BASE_URL}/tasks/{task_id}")
    assert complete_resp.status_code == 200

    completed_task = complete_resp.json()

    assert completed_task["completed"] == True


# удаление задачи
def test_user_deletes_task():
    tasks_resp = requests.get(f"{BASE_URL}/tasks/")
    tasks = tasks_resp.json()
    task_id = tasks[0]["id"]

    delete_resp = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert delete_resp.status_code == 200

    result = delete_resp.json()
    assert result["message"] == "Task deleted"
