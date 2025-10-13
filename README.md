# autoFormPy
A couple of Python scripts which inserts automatically registers from a table to a HTML form

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Python Libraries](https://img.shields.io/badge/Python%20Libraries-PyAutoGui%20%7C%20Pandas%20%7CTime-lightpurple)
![License](https://img.shields.io/badge/Free-License-green)
![Status](https://img.shields.io/badge/Status-Finished-green)
![Contributions](https://img.shields.io/badge/Contributions-Welcome!-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Windows%20%7C-lightgrey)

---

## 📌 Sections

- [1. Summary](#1-summary)
  - [1.1 What tools are used?](#11-what-tools-are-used-?)
- [2. How it works?](#2-how-it-works-?)
  - [2.1 Estrutura](#21-estrutura)
- [3. Funcionalidades](#3-funcionalidades)
- [4. Packages Utilizados](#4-packages-utilizados)

---

## 1. Summary

This is a couple of scripts made to automate the process of inserting records from a spreadsheet (CSV file) to a database, via HTML form and display them at the same page. 
And also, we have a simple script to capture the position of the cursor from screen to calibrate and adjust the autoFormPy, once we may face some issues or flaws
for the variety of screen resolutions of the devices. 

### 1.1 What tools are used?

All scripts were written in Python, in due to its simplicity and the libraries focused on automation and complexive process manipulating large of data and databases.
In adittion, we'll use the libraries: 
    - ✅ PyAutoGui - It creates dynamic automations with no efforts. With a single line, we can allow the script to press the Win button from the PC, for example. 
    - ✅ Time - Native library from Python. We'll use to create some "delays" in the processing, in order to maintain the usability of the code
    - ✅ Pandas - It is responsible for read and manipulate data from spreadsheets, databases. In this case, We'll read a CSV file.

---

## 2. How it works?


<img width="659" height="98" alt="Captura de Tela 2025-10-13 às 13 32 53" src="https://github.com/user-attachments/assets/1781f699-4e13-405e-ac39-195718abf131" />

Let's take a look in autoform_py.py. It's the file we'll run.

First, make sure to select the correct browser to to the process in the script.
By default, it's selected to the first browser on the list - Firefox. But, if you have another one of the browsers listed, you can change the 0 to 1...2..3, according to the position on the list. Ex: If you have Edge, then change: selected_browser = browsers[0] to selected_browser = browsers[2].

After running him, He will act according to the operating system of your machine. If Windows, he will use PyAutoGui to press Win and type the browser on the search to open it.
If MacOS, He will press cmd + space and type the browser and open.

If after some time you note something glitchy or the script did not select correctly the fields and fill them, probably it's in due to the cursor of the machine did not select correctly some fields. So, we may need to adjust him on the PyAutoGui. PyAutoGui clicks with cursor according to the coordinates we pass to it. Not all the screens will have the same resolutions, so we need to fix it.
If the script is currently running, we can stop the process by positioning the cursor to the left top of the screen. It it doesn't work, you can stop the process into the VS Code directly.

For this, we'll open get_cursor_position.py and run it. After running, open the login page provided on the code, use any email or password to enter (once it's for tests purposes). Put the cursor above the first field to be filled and wait 5 seconds until terminal gives the coordinates.

An then:

<img width="941" height="65" alt="Captura de Tela 2025-10-13 às 13 40 09" src="https://github.com/user-attachments/assets/2a96c3c1-c8a6-46b0-84a2-755e3d258db6" />

Change the pyautogui.click(x=536, y=312) to the coordinates you got from the get_cursor_position.py.

After this, run again the autoform_py.py and try again and see if it's all working.

> Happy coding!

