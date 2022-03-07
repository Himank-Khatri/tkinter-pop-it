import tkinter as tk
from tkinter import ttk

master = tk.Tk()
master.geometry('185x109')

h = tk.StringVar()
b = tk.StringVar()
file = tk.StringVar()
st = tk.StringVar(value='Click on generate')

def generate():
    row=0
    column=0

    ht = int(h.get())
    bt = int(b.get())
    
    with open('grid.py', 'w', encoding="utf-8") as f:
        
         
        f.write('import tkinter as tk\nfrom tkinter import ttk\nimport random\nmaster = tk.Tk()\ntvars=[]\n')
        
        for i in range(ht*bt):
            
            f.write(f"def f{i}():\n\tif s{i}.get() == '⬛':\n\t\trandom.choice(tvars).set('⬛')\n\t\ts{i}.set(' ')\ns{i} = tk.StringVar(value=' ')\ntvars.append(s{i})\nb{i} = tk.Button(master, textvariable=s{i}, width=3, borderwidth=0, command=f{i})\nb{i}.grid(row='{row}', column='{column}')\n")
            
            column+=1
            
            if column>bt-1:
                column = 0
                row += 1
            
        f.write("random.choice(tvars).set('⬛')\nmaster.mainloop()")
        
    master.destroy()
    

entries = ttk.Frame(master)
entries.grid(row='0')

height = ttk.Label(entries, text='Height:')
height.grid(row='0', column='0', padx='10', pady='10')

height_entry = ttk.Entry(entries, textvariable=h, width=8)
height_entry.grid(row='0', column='1', sticky='NW', pady=10)

breadth = ttk.Label(entries, text='Width:')
breadth.grid(row='1', column=0, sticky='NW', padx='10')

breadth_entry = ttk.Entry(entries, textvariable=b, width=8)
breadth_entry.grid(row='1', column='1', sticky='NW')

buttons = ttk.Frame(master, padding=(0,10,0,10))
buttons.grid(row='1')

generate_button = ttk.Button(buttons, text='Play', command=generate)
generate_button.grid(row='0', column='0', sticky='W', padx='9')

exit_button = ttk.Button(buttons, text='Exit', width='12', command=master.destroy)
exit_button.grid(row='0', column='1', sticky='NE')


master.mainloop()

with open('grid.py', 'r', encoding='utf-8') as f:
    app = f.read()
    exec(app)
    
with open('grid.py', 'w') as f:
    f.write('#######################################\n')
