import sys
import os
import webbrowser
import json
import validators
import pickle
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog as fd

def Main ():

    def focus (event):
        event.widget.focus()
        
    def site_focus():
        for site, site_frame in zip(site_radiobuttons, site_frames):
            if (root.focus_get() == site):
                site_frame.config(bg = "#334166")
                site.config(bg = "#334166", fg = "#ef8354", activebackground = "#334166", activeforeground = "#ef8354", selectcolor = "#334166")
            else:
                site_frame.config(bg = "#ffffff")
                site.config(bg = "#ffffff", fg = "#000000", activebackground = "#ffffff", activeforeground = "#000000", selectcolor = "#ffffff")
        root.focus()

    def sites_update():
        for index, site in enumerate(sites):
            if site:
                site_frame = tk.Frame(main_frame, bg = "#ffffff")
                site_frames.append(site_frame)
                site = tk.Radiobutton(site_frame, text=f"{sites[index]}", height = 2, font = ("Times new roman", 10), bg = "#ffffff", indicatoron = 0, bd = 0, variable = focused_site_var, value = index, command = site_focus)
                site_radiobuttons.append(site)
                site.pack(side = tk.LEFT)
                site_frame.grid(row = index, column = 0, sticky = "nswe")
            else:
                del sites[index]

    def clear_sites():
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        sites.clear()
        site_radiobuttons.clear()
        site_frames.clear()
        sites_update()
        
    # ---------------------------------------------------- Buttons functions ------------------------------------------------------

    def button_add():
        new_site = str(adder_entry.get())
        is_valid = validators.url(new_site)
        if (is_valid):
            adder_entry.delete(0, "end")
            sites.append(new_site)
            sites_update()
        else:
            tk.messagebox.showwarning(title="Warning", message="This URL is not valid")
        root.focus()

    def button_delete():
        if root.focus_get() and sites:
            del sites[focused_site_var.get()]

            for widget in main_frame.winfo_children():
                widget.destroy()
            
            site_radiobuttons.clear()
            site_frames.clear()
            sites_update()
        root.focus()

    def button_delete_all():
        if sites:
            clear_sites()
        root.focus()

    def button_run():
        for site in sites:
            webbrowser.open_new_tab(site)
        root.focus()
        if (auto_close_var.get):
            sys.exit()

    def button_auto_close():
        auto_close_var.set(not auto_close_var.get())
        root.focus()

    def button_save():
        file_name = fd.asksaveasfilename(
                defaultextension='.json', filetypes=[("json files", '*.json')],
                title="Choose filename")

        with open(file_name, "w", encoding="UTF-8") as f:
            data = []
            for site in sites:
                data.append(site)

            json.dump(data, f, indent=4, 
                        sort_keys=True, separators=(',', ": "), 
                        ensure_ascii=False)

            last_used_path = file_name
            with open(SETTINGSFILENAME, "w") as _f:
                _f.write(last_used_path)
        root.focus()

    def button_open(*args):

        if args:
            clear_sites()
            with open(args[0], "r") as f:
                data = json.load(f)
                for site in data:
                    #print(site)
                    sites.append(site)
        else:
            file_name = fd.askopenfilename(initialdir = "/", title = "Select File", filetypes=[("json files", '*.json')])
            if file_name:
                clear_sites()
                with open(file_name, "r") as f:
                    data = json.load(f)
                    for site in data:
                        #print(site)
                        sites.append(site)
                last_used_path = file_name
                with open(SETTINGSFILENAME, "w") as _f:
                    _f.write(last_used_path)

        root.focus()
        sites_update()
        
    # ---------------------------------------------------- Creating layout ------------------------------------------------------

    root = tk.Tk()
    root.title("Good morning app")

    root.resizable(False, False)
    root.rowconfigure((0, 2), minsize = 40)
    root.rowconfigure(1, minsize = 360)
    root.bind("<Button-1>", focus)


    upper_frame = tk.Frame(root, relief = tk.RAISED, bd = 1, bg = "#4f5d75")
    upper_frame.rowconfigure(0, minsize = 40)
    upper_frame.columnconfigure((0, 1, 2, 3, 4), minsize = 80)

    main_frame = tk.Frame(root, bg = "#ffffff")
    main_frame.rowconfigure((0,1,2,3,4,5,6,7), minsize = 40)
    main_frame.columnconfigure(0, minsize = 400)

    bottom_frame = tk.Frame(root, relief = tk.RAISED, bd = 1, bg = "#4f5d75")
    bottom_frame.rowconfigure(0, minsize = 40)
    bottom_frame.columnconfigure((0, 1, 2, 3, 4), minsize = 80)


    adder_entry = tk.Entry(upper_frame, font = ("Times new roman", 10), bg = "#d8d9d9", fg = "#000000")
    adder_entry.grid(row = 0, column = 2, columnspan = 2, padx = (10, 10), pady = (5, 0), sticky = "w")
    adder_entry.focus_set()

    add_button = tk.Button(upper_frame, text = "Add", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = button_add)
    add_button.grid(row = 0, column = 4, pady = (5, 0), sticky = "w")

    delete_button = tk.Button(upper_frame, text = "Delete", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = button_delete)
    delete_button.grid(row = 0, column = 0, pady = (5, 0), sticky = "e")

    delete_all_button = tk.Button(upper_frame, text = "Delete All", font = ("Times new roman", 10), width = 8, bg = "#d8d9d9", fg = "#e57340", command = button_delete_all)
    delete_all_button.grid(row = 0, column = 1, pady = (5, 0), sticky = "e")

    run_button = tk.Button(bottom_frame, text = "Run", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = button_run)
    run_button.grid(row = 0, column = 4, pady = 6, sticky = "w")

    auto_close_button = tk.Checkbutton(bottom_frame, text = "auto-close", command = button_auto_close)
    auto_close_button.configure(activebackground = "#4f5d75", activeforeground = "#e57340", bg = "#4f5d75", fg = "#e57340")
    auto_close_button.select()
    auto_close_button.grid(row = 0, column = 3, padx = (0, 5), pady = 6, sticky = "w")
    
    save_button = tk.Button(bottom_frame, text = "Save", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = button_save)
    save_button.grid(row = 0, column = 1, pady = 5, sticky = "e")
    
    open_button = tk.Button(bottom_frame, text = "Open", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = button_open)
    open_button.grid(row = 0, column = 0, pady = 5, sticky = "e")

    # ---------------------------------------------------- Prepairing to launch ------------------------------------------------------
    
    SETTINGSFILENAME = "Good_Morning_App_settings"
    last_used_path = ""

    auto_close_var = tk.BooleanVar()
    auto_close_var.set(True)
    focused_site_var = tk.IntVar()
    focused_site_var.set(0)

    sites = []
    site_radiobuttons = []
    site_frames = []

    if (os.path.exists("Good_Morning_App_settings")):
        with open(SETTINGSFILENAME, "r") as f:
            last_used_path = f.read()
    else:
        print("Can't find settings")

    if last_used_path:
        button_open(last_used_path)

    upper_frame.grid(row = 0, column = 0, columnspan = 5, sticky = "nswe")
    main_frame.grid(row = 1, column = 0, columnspan = 5, sticky = "nswe")
    bottom_frame.grid(row = 2, column = 0, columnspan = 5, sticky = "nswe")


    root.mainloop()
    

if __name__ == "__main__":
    Main()

