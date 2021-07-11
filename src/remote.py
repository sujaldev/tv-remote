import pyautogui
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    with open("remote.html", "r") as f:
        html = f.read()
    return html

# PLATFORM BUTTONS


@app.route("/youtube_btn")
def youtube_btn():
    print("YOUTUBE BUTTON PRESSED")
    return "pressed"


@app.route("/netflix_btn")
def netflix_btn():
    print("NETFLIX BUTTON PRESSED")
    return "pressed"


# MEDIA BUTTONS


@app.route("/play_pause_btn")
def play_pause_btn():
    print("PLAY PAUSE BUTTON PRESSED")
    pyautogui.press("space")
    return "pressed"


@app.route("/next_btn")
def next_btn():
    print("NEXT BUTTON PRESSED")
    pyautogui.press("nexttrack")
    return "pressed"


# EXTRA BUTTONS


@app.route("/go_back")
def go_back_btn():
    print("GO BACK BUTTON PRESSED")
    pyautogui.press("backspace")
    return "pressed"


# NAVIGATION BUTTONS


@app.route("/top_btn")
def top_btn():
    print("TOP BUTTON PRESSED")
    pyautogui.press("up")
    return "pressed"


@app.route("/left_btn")
def left_btn():
    print("LEFT BUTTON PRESSED")
    pyautogui.press("left")
    return "pressed"


@app.route("/center_btn")
def center_btn():
    print("CENTER BUTTON PRESSED")
    pyautogui.press("enter")
    return "pressed"


@app.route("/right_btn")
def right_btn():
    print("RIGHT BUTTON PRESSED")
    pyautogui.press("right")
    return "pressed"


@app.route("/bottom_btn")
def bottom_btn():
    print("BOTTOM BUTTON PRESSED")
    pyautogui.press("down")
    return "pressed"


if __name__ == "__main__":
    app.run(port=54321, host="0.0.0.0")
