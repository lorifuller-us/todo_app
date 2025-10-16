import json
from pathlib import Path
import flet as ft

DATA_FILE = Path("tasks.json")  # optional persistence


def main(page: ft.Page):
    page.title = "Minimal To-Do App"
    page.window_width = 420
    page.window_height = 640
    page.padding = 16
    page.theme_mode = "dark"

    # State
    tasks = []  # list of dicts: {"title": str, "done": bool}

    # Optional: load tasks from disk
    def load_tasks():
        nonlocal tasks
        if DATA_FILE.exists():
            try:
                tasks = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            except Exception:
                tasks = []
        else:
            tasks = []

    def save_tasks():
        try:
            DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

    load_tasks()

    # UI controls
    new_task = ft.TextField(
        hint_text="Add a task...",
        expand=True,
        border=ft.InputBorder.OUTLINE,
        autofocus=True,
        on_submit=lambda e: add_task(e.control.value),
    )
    add_btn = ft.IconButton(icon="add", tooltip="Add", on_click=lambda e: add_task(new_task.value))
    header = ft.Row([new_task, add_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    list_view = ft.ListView(expand=True, spacing=6, padding=0, auto_scroll=False)

    # Actions
    def render():
        list_view.controls.clear()
        for i, t in enumerate(tasks):
            checkbox = ft.Checkbox(
                label=t["title"],
                value=t["done"],
                on_change=lambda e, idx=i: toggle_done(idx, e.control.value),
            )
            delete_btn = ft.IconButton(
                icon="delete_outline", tooltip="Delete", on_click=lambda e, idx=i: delete_task(idx)
            )
            row = ft.Row([checkbox, delete_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            list_view.controls.append(row)
        page.update()

    def add_task(title: str):
        title = (title or "").strip()
        if not title:
            return
        tasks.append({"title": title, "done": False})
        new_task.value = ""
        save_tasks()
        render()

    def toggle_done(idx: int, value: bool):
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = value
            save_tasks()
            render()

    def delete_task(idx: int):
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            save_tasks()
            render()

    # Layout
    page.add(header, ft.Divider(opacity=0.1), list_view)
    render()


if __name__ == "__main__":
    ft.app(target=main)