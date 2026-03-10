# GitHub Activity Viewer

A Python CLI tool that fetches and summarizes a GitHub user's recent public activity — sorted and grouped for easy reading.

## Example Output

```
Created branch agenthub in karpathy/autoresearch at 2026-03-09 19:30:05
Created 3 discussions in karpathy/autoresearch at 2026-03-08 23:37:49
Left 5 comments on an issue in karpathy/autoresearch at 2026-03-09 15:08:38
Opened an issue in karpathy/autoresearch at 2026-03-08 23:41:03
Closed 6 pull requests in karpathy/autoresearch at 2026-03-08 16:37:02
Opened 2 pull requests in karpathy/autoresearch at 2026-03-09 19:30:40
Pushed 9 commits to karpathy/autoresearch at 2026-03-09 23:00:56
Pushed 2 commits to karpathy/nanochat at 2026-03-10 06:26:42
```

## Features

- Fetches the latest 10 public events for any GitHub user
- Groups similar actions (e.g. multiple pushes to the same repo become *"Pushed 9 commits to..."*)
- Sorts activity by repo and event type for a clean, structured summary
- Supports a wide range of event types: pushes, pull requests, issues, comments, discussions, branch/repo creation, and more

## Requirements

- Python 3.12+
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

```bash
python main.py
```

You'll be prompted to enter a GitHub username:

```
> Enter username whose activity you'd like to see: karpathy
```

## Project Structure

```
.
├── main.py                      # Entry point
├── activity.py                  # Activity model and formatting logic
└── github_activity_retriever.py # GitHub API client
```

## How It Works

1. **Fetches** the user's latest public events from the GitHub API
2. **Sorts** events by repo name and event type using a custom comparator
3. **Compresses** consecutive same-type events into a single summarized entry (e.g. "Pushed 9 commits")
4. **Prints** each activity in a human-readable format with a timestamp