import tkinter as tk
from tkinter import ttk
 

row=0
column=0

dim = input('Enter the desigred dimensions(LxB): ')
h = int((dim.split('x')[1]))
b = int(dim.split('x')[-1])

file = input('Enter the file name: ')

with open(f'{file}.py', 'w', encoding="utf-8") as f:
    
    f.write('import tkinter as tk\nfrom tkinter import ttk\nimport random\nroot = tk.Tk()\ntvars=[]\n')
    
    for i in range(h*b):
        
        f.write(f"def f{i}():\n\tif s{i}.get() == '⬛':\n\t\trandom.choice(tvars).set('⬛')\n\t\ts{i}.set(' ')\ns{i} = tk.StringVar(value=' ')\ntvars.append(s{i})\nb{i} = tk.Button(root, textvariable=s{i}, width=3, borderwidth=2, command=f{i})\nb{i}.grid(row='{row}', column='{column}')\n")
        
        column+=1
        
        if column>b-1:
            column = 0
            row += 1
        
    f.write("random.choice(tvars).set('⬛')\nroot.mainloop()")
        
print('\nFile successfully generated!')
