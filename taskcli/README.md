# Tasker CLI

A simple command-line task manager that stores tasks in a local JSON file.

## Setup

```bash
python main.py
```

No dependencies required — uses only the Python standard library.

## Usage

Run the app and type commands at the `>` prompt.

```
> add Buy groceries
Task added successfully (ID: 1)

> list
1 Buy groceries todo
```

## Commands

| Command | Description |
|---|---|
| `add <description>` | Add a new task |
| `update <id> <description>` | Update a task's description |
| `delete <id>` | Delete a task |
| `mark-in-progress <id>` | Mark a task as in-progress |
| `mark-done <id>` | Mark a task as done |
| `list` | List all tasks |
| `list todo` | List tasks with status `todo` |
| `list in-progress` | List tasks with status `in-progress` |
| `list done` | List tasks with status `done` |
| `exit` | Save and quit |

## Data

Tasks are saved to `db.json` in the same directory. Each task has the following fields:

- `id` — auto-incremented integer
- `description` — task text
- `status` — `todo`, `in-progress`, or `done`
- `createdAt` — UTC timestamp
- `updatedAt` — UTC timestamp

## Project Structure

```
.
├── main.py      # CLI loop and input parsing
├── tasker.py    # Task logic and JSON persistence
└── db.json      # Auto-generated task database
```