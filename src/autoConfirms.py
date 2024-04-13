import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def save_keywords():
    with open('keywords.txt', 'w') as f:
        keywords = listbox.get(0, tk.END)
        f.write('\n'.join(keywords))

def load_keywords():
    try:
        with open('./database/keywords.txt', 'r') as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        open('keywords.txt', 'w').close()  # Crea el archivo si no existe

def run_selenium_script(excluded_keywords):
    driver = webdriver.Chrome('./dependencies/chromedriver.exe')
    driver.get('file:///C:/Users/Ale/OneDrive/PROGRAMMING/PYTHON/EmailConfirms/confirms.html#')
    time.sleep(1)  # Asegura que la página esté completamente cargada
    companias = driver.find_elements(By.CSS_SELECTOR, '.company')
    for compania in companias:
        nombre_compania = compania.find_element(By.CSS_SELECTOR, 'strong').text
        if not any(keyword.lower() in nombre_compania.lower() for keyword in excluded_keywords):
            trades = compania.find_elements(By.CSS_SELECTOR, '.trade')
            for trade in trades:
                boton_enviar = trade.find_element(By.CSS_SELECTOR, 'a')
                driver.execute_script("arguments[0].click();", boton_enviar)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(1)  # Espera para la confirmación del envío del email
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
    driver.quit()
    messagebox.showinfo("Completion", "Script ejecutado correctamente!")

def add_keyword():
    keyword = entry.get()
    if keyword and keyword not in listbox.get(0, tk.END):
        listbox.insert(tk.END, keyword)
    entry.delete(0, tk.END)
    save_keywords()

def remove_keyword():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        save_keywords()

def execute_script():
    excluded_keywords = list(listbox.get(0, tk.END))
    run_selenium_script(excluded_keywords)

root = tk.Tk()
root.title("Configuración de Compañías para AutoConfirmaciones de Trades")

frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, padx=(0, 10))

scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.LEFT, fill="y")

listbox.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=53)
entry.pack(pady=(0, 10))

add_button = tk.Button(root, text="Añadir Palabra Clave", command=add_keyword)
add_button.pack()

remove_button = tk.Button(root, text="Remover Palabra Clave Seleccionada", command=remove_keyword)
remove_button.pack()

run_button = tk.Button(root, text="Ejecutar Script", command=execute_script)
run_button.pack(pady=20)

load_keywords()  # Carga las palabras clave al iniciar la aplicación
root.mainloop()
