def IDE():

    IDE = Tk()

    file_path = ""

    def set_file_path(path):
        global file_path
        file_path = path

    def open_file():
        path = askopenfilename(filetypes=[("Python Files", "*.py")])
        with open(path , 'r') as file:
            code = file.read()
            editor.delete("1.0" , END)
            editor.insert("1.0" , code)
            set_file_path(path)  

    def save_as():
        if file_path == '':
            path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
        else:
            path = file_path
        with open(path , "w") as file:
            code = editor.get("1.0" , END)
            file.write(code)
            set_file_path(path)

    def run():
        if file_path ==  '':
            save_prompt = Toplevel()
            text = Label(save_prompt , text="plesae save the file ")
            text.pack()
            return
        command = f'Python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE ,stderr=subprocess.PIPE , shell=True)
        output , error = process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0', error)

    menu_bar = Menu(IDE)

    run_bar = Menu(menu_bar , tearoff=0)
    run_bar.add_command(label="Run" , command=run)
    menu_bar.add_cascade(label="Run" , menu=run_bar)
    IDE.config(menu=menu_bar)

    file_bar = Menu(menu_bar , tearoff=0)
    file_bar.add_command(label="save" , command=save_as)
    file_bar.add_command(label="open" , command=open_file)
    file_bar.add_command(label="save as" , command=save_as)
    file_bar.add_command(label="Exit" , command=exit)
    menu_bar.add_cascade(label="File" , menu=file_bar)
    IDE.config(menu=menu_bar)

    IDE.title("NashIDE")
    editor = Text(bg="blue" , fg="red")
    editor.pack()

    code_output = Text(height=10 , bg="black" , fg="lightgreen")
    code_output.pack()

    IDE.mainloop()