# Minimalistic_ui
## A minimalistic UI with ai agent
### This project is a simple AI agent that takes natural language instructions from the user (like “Open Google and search for YouTube”) and automatically performs them in a browser using Python and Selenium, with help from Gemini 1.5 Flash for converting natural language into executable Python code.

###  Key Features
#### Converts plain English instructions into working Python code using Google's Gemini API (1.5 Flash).

#### Automates browser actions (like searching, clicking) using Selenium.

#### Built with a minimal Tkinter GUI for beginner-friendly use.

#### Can be compiled to .exe using PyInstaller.

### Project Structure

#### main_ui.py	The main UI window with prompt input and Run button.
#### ai_agent.py	Communicates with Gemini API to generate code.
#### run_task.py	Executes the generated code safely using exec() and Selenium.

### Tech Stack
#### Python 3.11+
#### Selenium – for browser automation
#### Tkinter – for GUI
#### Google Generative AI SDK – for Gemini 1.5 Flash API access
#### PyInstaller – to generate .exe file

### Steps
#### 1.Go to command prompt and type the following for installation
##### pip install openai google-generativeai selenium PyQt5 playwright
##### playwright install
##### set GEMINI_API_KEY=your-api-key-here
##### For getting the free api key visit the link https://aistudio.google.com/apikey
#### 2.Then copy codes which is given in your system
#### 3.Convert to .EXE
##### pip install pyinstaller
##### pyinstaller --onefile --noconsole main_ui.py
#### 4.To run this you need to go to command prompt and visit the folder where you saved all others files and then run the following command
##### python main_ui.py

