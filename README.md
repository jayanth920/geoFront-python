# Location Notifier

This Python script listens for a specific key press (default: 'e') and fetches the latest location from a backend URL. When the key is pressed, it sends a macOS notification with the latest location (country and state).

## Features

- Fetches location data from a backend URL (configured using environment variables).
- Listens for a key press and sends a notification with the latest location.
- Sends notifications using `pync` on macOS.
- Environment variables are loaded securely using `python-dotenv`.

## Prerequisites

- Python 3.x
- `python-dotenv` to load environment variables from `.env` file.
- `pync` for macOS notifications.
- `requests` for making HTTP requests.

## Installation

1. Clone this repository or download the script.

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project with the following contents:
    ```
    BACKEND_URL=your_backend_url
    ```

   Replace `your_backend_url` with the actual URL of your backend endpoint that provides location data.

## Usage

1. Run the script:
    ```bash
    python location_notifier.py
    ```

2. Press the `e` key while running the script to fetch the latest location and receive a notification.

3. The notification will display the `country` and `state` of the latest location.

## Example Output

When you press `e`, the script will fetch the latest location and send a notification. For example:

