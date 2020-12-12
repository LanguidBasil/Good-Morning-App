import sys
import os
import webbrowser
import json
import tkinter as tk
from tkinter import filedialog as fd

def Main ():

    def focus (event):
        event.widget.focus()

    def site_focus():
        for index, site in enumerate(site_radiobuttons):
            if (root.focus_get() == site):
                site_frames[index].config(bg = "#334166")
                site_radiobuttons[index].config(bg = "#334166", fg = "#ef8354", activebackground = "#334166", activeforeground = "#ef8354", selectcolor = "#334166")
            else:
                site_frames[index].config(bg = "#ffffff")
                site_radiobuttons[index].config(bg = "#ffffff", fg = "#000000", activebackground = "#ffffff", activeforeground = "#000000", selectcolor = "#ffffff")
        root.focus()

    def sites_update():
        for index, site in enumerate(sites):
            if site:
                site_frame = tk.Frame(main_frame, bg = "#ffffff")
                site_frames.append(site_frame)
                site = tk.Radiobutton(site_frame, text=f"{sites[index]}", height = 2, font = ("Times new roman", 10), bg = "#ffffff", indicatoron = 0, bd = 0, variable = active_var, value = index, command = site_focus)
                site_radiobuttons.append(site)
                site.pack(side = tk.LEFT)
                site_frame.grid(row = index, column = 0, sticky = "nswe")
            else:
                del sites[index]

    def add():
        new_site = str(adder_entry.get())
        adder_entry.delete(0, "end")
        sites.append(new_site)
        sites_update()
        root.focus()

    def delete():
        if root.focus_get():
            nonlocal sites
            del sites[active_var.get()]

            for widget in main_frame.winfo_children():
                widget.destroy()
            
            site_radiobuttons.clear()
            site_frames.clear()
            root.focus()
            sites_update()

    def run():
        for site in sites:
            webbrowser.open_new_tab(site)
        root.focus()

    def my_open():
        pass

    def save():
        file_name = fd.asksaveasfilename(
                defaultextension='.json', filetypes=[("json files", '*.json')],
                title="Choose filename")

        with open(file_name, "w", encoding="UTF-8") as f:
            data = {}
            for index, site in enumerate(sites):
                data[index] = site

            json.dump(data, f, indent=4, 
                        sort_keys=True, separators=(',',': '), 
                        ensure_ascii=False)
        root.focus()

    #def my_open():
    #    nonlocal sites
    #    for widget in main_frame.winfo_children():
    #        widget.destroy()
            
    #    site_radiobuttons.clear()
    #    site_frames.clear()

    #    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("text", "*.txt"), ("all files", "*.*")))
    #    with open(filename, "r") as f:
    #        temp_sites = f.read()
    #        sites = temp_sites.split(", ")

    #    root.focus()
    #    sites_update()


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
    main_frame.columnconfigure(0, minsize = 402)

    bottom_frame = tk.Frame(root, relief = tk.RAISED, bd = 1, bg = "#4f5d75")
    bottom_frame.rowconfigure(0, minsize = 40)
    bottom_frame.columnconfigure((0, 1, 2, 3, 4), minsize = 80)


    adder_entry = tk.Entry(upper_frame, font = ("Times new roman", 10), bg = "#d8d9d9", fg = "#000000")
    adder_entry.grid(row = 0, column = 2, columnspan = 2, pady = (5, 0), sticky = "w")
    adder_entry.focus_set()

    add_button = tk.Button(upper_frame, text = "Add", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = add)
    add_button.grid(row = 0, column = 4, pady = (5, 0), sticky = "w")

    delete_button = tk.Button(upper_frame, text = "Delete", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = delete)
    delete_button.grid(row = 0, column = 0, pady = (5, 0), sticky = "e")

    run_button = tk.Button(bottom_frame, text = "Run", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = run)
    run_button.grid(row = 0, column = 4, pady = 6, sticky = "w")
    
    save_button = tk.Button(bottom_frame, text = "Save", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340", command = save)
    save_button.grid(row = 0, column = 1, pady = 6, sticky = "e")
    
    open_button = tk.Button(bottom_frame, text = "Open", font = ("Times new roman", 10), width = 6, bg = "#d8d9d9", fg = "#e57340")
    open_button.grid(row = 0, column = 0, pady = 6, sticky = "e")
    

    active_var = tk.IntVar()
    active_var.set(0)

    sites = []
    site_radiobuttons = []
    site_frames = []
    sites_update()

    upper_frame.grid(row = 0, column = 0, columnspan = 5, sticky = "nswe")
    main_frame.grid(row = 1, column = 0, columnspan = 5, sticky = "nswe")
    bottom_frame.grid(row = 2, column = 0, columnspan = 5, sticky = "nswe")

    root.mainloop()
    

if __name__ == "__main__":
    Main()

