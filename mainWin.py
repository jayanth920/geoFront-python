import os
import time
import requests
from pynput import keyboard
from dotenv import load_dotenv
from win11toast import toast

load_dotenv()

# Backend URL
BACKEND_URL = os.getenv('BACKEND_URL')


# Function to fetch locations
def fetch_locations():
    try:
        response = requests.get(BACKEND_URL)
        response.raise_for_status()
        locations = response.json()
        return locations
    except requests.exceptions.RequestException as e:
        print(f"Error fetching locations: {e}")
        return []

# Function to send notification on Windows
# def send_notification(location):
#     title = "Latest Location"
#     message = f"{location['country']} - {location['state']}"
#     toaster.show_toast(title, message, duration=5)
#     print(f"Notification sent: {message}")


# Function to send notification on Windows
def send_notification(location):
    title = "Latest Location"
    message = f"{location['country']} - {location['state']}"
    toast(message, audio={'silent': 'true'}, scenario='incomingCall')
    print(f"Notification sent: {message}")


# Listener function for key press
def on_press(key):
    try:
        if key.char and key.char.lower() == 'x':  # Check if 'x' is pressed
            print("Key 'x' pressed, fetching the latest location...")
            locations = fetch_locations()
            if locations:
                latest_location = locations[-1]  # Get the latest location
                send_notification(latest_location)  # Send the notification
            else:
                print("No locations available.")
    except AttributeError:
        pass  # Handle special keys

# Main function to listen for 'x' key press
def listen_for_key():
    print("Press 'x' to get the latest location.")
    listener = keyboard.Listener(on_press=on_press)
    try:
        listener.start()
        listener.join()
    except KeyboardInterrupt:
        print("Exiting the application.")
    finally:
        listener.stop()

if __name__ == "__main__":
    listen_for_key()
