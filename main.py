import os
import pync
import time
import requests
from pynput import keyboard
from dotenv import load_dotenv

load_dotenv()

# Backend URL
BACKEND_URL = os.getenv('BACKEND_URL')

# Function to fetch locations
def fetch_locations():
    try:
        response = requests.get(BACKEND_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        locations = response.json()
        return locations
    except requests.exceptions.RequestException as e:
        print(f"Error fetching locations: {e}")
        return []

# Function to send notification (macOS specific using osascript)
def send_notification(location):
    title = "Latest Location"
    message = f"{location['country']} - {location['state']}"
    pync.notify(f"{message}")
    print(f"Notification sent: {message}")

# Listener function for key press
def on_press(key):
    try:
        if key.char and key.char.lower() == 'x':  # Check if 'K' is pressed
            print("Key 'x' pressed, fetching the latest location...")
            locations = fetch_locations()
            if locations:
                latest_location = locations[-1]  # Get the latest location
                send_notification(latest_location)  # Send the notification
            else:
                print("No locations available.")
    except AttributeError:
        # Handle special keys that don't have a 'char' attribute
        pass

# Main function to listen for 'K' key press
def listen_for_key():
    print("Press 'x' to get the latest location.")
    listener = keyboard.Listener(on_press=on_press)
    try:
        listener.start()
        listener.join()  # Wait for key press events
    except KeyboardInterrupt:
        print("Exiting the application.")
    finally:
        listener.stop()  # Properly stop the listener


if __name__ == "__main__":
    listen_for_key()
