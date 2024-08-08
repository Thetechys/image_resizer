import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
import os
import unlimited_file


class prompt():



    labels = [
        ("Input path:", 1, 1),
    ]



    def __init__(self):


        self.dimension = width, height = 650, 125
        self.boxroot = tk.Tk()
        self.boxroot.title("Image resizer")
        self.boxroot.geometry(f"{str(width)}x{str(height)}")


        self.create_labels_and_entries()
        self.create_command_buttons()


        self.boxroot.mainloop()



    

    def create_labels_and_entries(self):

        labels = self.labels

        for text, row, column in labels:
            label = tk.Label(self.boxroot, text=text)
            label.grid(row=row, column=column)


        self.input_path = tk.StringVar()
        self.input_entry = tk.Entry(self.boxroot,textvariable=self.input_path, width=70)
        self.input_entry.grid(row=1, column=2)



    # call this function in __init__, buttons initialize when instance called
    def create_command_buttons(self):

        command_buttons = [
            ("Browse", self.browse_inputfolder, 1, 3),
            ("Resize!",self.img_resize, 3, 3),
            ("Quit", self.quit_function, 6, 3),

        ]

        for text, command, row, column in command_buttons:
            button = tk.Button(self.boxroot, text=text, command=command, width=18, height=1)
            button.grid(row=row, column=column)







    # decorator that open up a new thread to execute original function with thread
    # so tkinter GUI won't crash / freeze
    ''' ESSENTIAL '''
    def thread_wrapper(func):

        def thread_function(*args,**kwargs):

            func_thread = threading.Thread(target=func,args=args,kwargs=kwargs)
            func_thread.start()

        return thread_function
    

    # prompts warning if somethings not right
    def msg_prompt(self,errTitle='Invalid Path', errMsg='Please provide a valid path.'):
        messagebox.showwarning(title=errTitle,message=errMsg)


    #check if directory in entry box exits
    #if not: an error windows prompted
    def check_directory(self, dir):
        if not os.path.isdir(dir):
            self.msg_prompt()
        else:
            return True

    
    #call function "resize_images_in_folder" from unlimited_file if
    #check_directory returns True
    @thread_wrapper
    def img_resize(self):

        input_path = self.input_path.get()
        output_path = f'{self.input_path.get()}/resized_output'

        if self.check_directory(input_path):
            unlimited_file.resize_images_in_folder(input_path, output_path)
        
    #function for "browse" button
    @thread_wrapper
    def browse_inputfolder(self):
        folder_path = filedialog.askdirectory()

        if folder_path:
            self.input_path.set(folder_path)
   
    # quit gracefully, instead of "boxroot.destroy"
    @thread_wrapper
    def quit_function(self):
        print('Quitting app')
        self.boxroot.quit()




if __name__ == '__main__':

    app1 = prompt()
