# autoFormPy

A set of Python scripts to automatically insert records from a spreadsheet into an HTML form.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python\&logoColor=white)
![Python Libraries](https://img.shields.io/badge/Python%20Libraries-PyAutoGUI%20%7C%20Pandas-lightpurple)
![Status](https://img.shields.io/badge/Status-Finished-green)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Windows-lightgrey)

---

## 📌 Table of Contents

* [1. Summary](#1-summary)

  * [1.1 Tools Used](#11-tools-used)
* [2. Project Structure](#2-project-structure)
* [3. Usage](#3-usage)
* [4. Features](#4-features)
* [5. Why This Project Matters](#5-why-this-project-matters)

---

Live demonstration:

![Adobe Express - 1760382190472512(1)](https://github.com/user-attachments/assets/661afe57-d529-4ace-85a4-29fb770a0ec5)


## 1. Summary

This project consists of Python scripts designed to automate the process of logging into a system, inserting records from a spreadsheet (CSV file) into an HTML form, and displaying them on the same page.
Additionally, there is a script to capture the cursor position on the screen, which helps calibrate the automation for different screen resolutions.


> Note: The CSV file and HTML form used in this project are in Portuguese, but the concepts are applicable to any language.

### 1.1 Tools Used

* **Python** – Chosen for its simplicity and extensive libraries for automation and data manipulation.
* **PyAutoGUI** – Automates mouse clicks, keyboard typing, and other UI interactions.
* **Time** – Native Python library for adding delays, ensuring the automation works smoothly.
* **Pandas** – Handles CSV parsing and data manipulation for the automation process.

---

## 2. Project Structure

```plaintext
autoFormPy/
│
├── tables/
│   └── produtos.csv           # CSV data used for this project
├── main.py                    # Main script - the first one we will run
├── csv_bot.py                 # The module who will do the job (called by main.py)
├── get_cursor_position.py     # captures cursor coordinates for calibration
└── README.md
```

---

## 3. Usage

### 3.1 Install Dependencies

```bash
pip install pyautogui pandas
```

### 3.2 Clone Repository

```bash
git clone https://github.com/yourusername/autoFormPy.git
cd autoFormPy
```

### 3.3 Main Script: `main.py`

1. **Select your browser** inside the script:

```python
selected_browser = browsers[0]  # 0 = Firefox, 1 = Chrome, 2 = Edge...
```

> Make sure to select the correct browser. By default, Firefox (0) is selected. Adjust the index if using another browser.

2. **Run the script**

```bash
python main.py
```

* On **Windows**, the script presses the Win key, types the browser name, and opens it.
* On **macOS**, it uses Cmd + Space (Spotlight) to open the selected browser.

3. **Automation Process**
   Once the form is open, PyAutoGUI will:

* Click each field based on coordinates
* Type data from the CSV file
* Submit the form
* Repeat for all rows

4. **Fails or Glitches**

* If the script fails to select the right fields, recalibrate cursor coordinates.
* Move the cursor to the top-left corner to stop the automation, or stop the process in your editor.
* Run:

```bash
python get_cursor_position.py
```

* Open the test page, move the cursor to the input field, and wait ~5 seconds.
* Copy the new coordinates to `main.py`, replacing lines like:

```python
# Old
pyautogui.click(x=536, y=312)

# New example
pyautogui.click(x=800, y=450)
```

Rerun `main.py` to continue.

Depending on your machine’s performance, waiting 5 seconds for the browser to open might be too long or too short.

If this happens, open the csv_bot.py file and adjust the time.sleep value:

```
 # Inside csv_bot.py
 pyautogui.press("enter")
 time.sleep(5) # <-- Change this value
```
Change the time.sleep to 4 or less, depending on the performance.

This makes the process faster on high-performance systems or slower on older ones.

You may encounter the same issue while searching for the browser...

In the line:
```
# Inside [main.py or csv_bot.py, whichever file has this code]
pyautogui.press("return")
time.sleep(3) # <-- Adjust this value
```

Adjust the time.sleep to >3 secs or <3 secs, depending of the performance of the machine.

On MacOS, it can be interesting if you leave the browser opened, but the all windows closed. This can make the process faster too.

---

## 4. Features

* ⚙️ Automatic HTML form filling from spreadsheet data
* 📄 CSV parsing with Pandas
* 🖱️ Cross-platform automation (Windows & macOS)
* 🎯 Customizable cursor calibration
* 🛑 Failsafe mechanism (move mouse to top-left corner to stop)

---

## 5. Why This Project Matters

This project demonstrates:

* **Practical Python skills** in automation and data manipulation
* **Problem-solving mindset**: handling screen resolution differences and failsafe mechanisms
* **Cross-platform development**
* Ability to streamline repetitive tasks and save significant time in data entry processes

> In short, it’s a concrete example of applying Python to solve real-world productivity challenges.

---

## 6. Limitations and Next Steps

This project uses PyAutoGUI, an approach based on screen coordinates. While effective for quick automation, it is sensitive to variations in screen resolution, window sizing, and other applications.

Possible improvements for a future version (v2.0):

    DOM-Based Automation: Replace PyAutoGUI with tools like Selenium or Playwright. They interact directly with HTML elements (by ID, class, or XPath), making the automation 100% independent of screen resolution and much more robust.

    Image Recognition: Instead of fixed coordinates, use the pyautogui.locateOnScreen() function to find the form fields visually, which would make the script more adaptable to minor interface changes.

> Happy coding! 🚀
