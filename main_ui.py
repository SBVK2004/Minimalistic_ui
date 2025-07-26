import tkinter as tk
from ai_agent import ask_gemini  
import re

def clean_generated_code(code):
    
    code = re.sub(r"```(?:python)?", "", code)
    code = code.strip("`").strip()
    return code

def run_task():
    prompt = prompt_entry.get()
    try:
        
        ai_code = ask_gemini(f"Convert the following instruction into Python Selenium code: {prompt}. Do not include explanation.")

        
        clean_code = clean_generated_code(ai_code)
        print("Generated Code:\n", clean_code)  

        
        exec(clean_code)

    except SyntaxError as se:
        print(f"Syntax error: {se}")
    except Exception as e:
        print(f"Automation failed: {e}")


root = tk.Tk()
root.title("Browser Automation Agent")

prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=10)

run_button = tk.Button(root, text="Run", command=run_task)
run_button.pack()

root.mainloop()
