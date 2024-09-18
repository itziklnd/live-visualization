# Live Visualization Dashboard

This project is a real-time dashboard to display completed and incomplete tasks (referred to as "SMs"). It provides a dynamic, motivational interface for users, showcasing completed and pending tasks with real-time updates using AJAX.

## Features

- Real-time updates of task statuses.
- Tasks are separated into two categories: completed and incomplete.
- Highlighting feature for newly completed/incomplete tasks.
- Fully responsive design with Bootstrap.
- Visualization of completed and incomplete tasks using cards.
- Animations for transitions between task statuses.

## Technologies Used

- Python (Flask)
- HTML, CSS, JavaScript
- Bootstrap 4.5
- jQuery
- AJAX for real-time updates

## Installation

### Clone the repository

```bash
git clone https://github.com/itziklnd/live-visualization.git
cd live-visualization
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

After installing the dependencies, run the Flask server:

```bash
python3.10 app.py
```

Visit the app at `http://127.0.0.1:5000/`.

## How It Works

The dashboard fetches the list of completed and incomplete tasks (referred to as SMs) from the server and displays them in two separate sections:

- Completed SMs: Displayed in green, these are tasks that have been successfully completed.
- Incomplete SMs: Displayed in red, these are tasks that have yet to be completed.

## Changing Task Statuses

You can modify the task data sources by updating the completed and incomplete lists in your technologies.txt file.


## Future Features

- User authentication and login system.
- Task assignment by users.
- More customization options for the dashboard.

## License

This project is open-source and available under the [MIT License](LICENSE).
