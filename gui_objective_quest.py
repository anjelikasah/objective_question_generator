import tkinter as tk
from tkinter import filedialog
from img2txt import image_to_text
from pdf2txt_complete import convert_pdf_to_txt


def load_img_file():

        filename = tk.filedialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
        print(filename)
        entry_img.delete(0,tk.END)
        entry_img.insert(0,filename)
        if filename:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % filename)
            return filename

def load_pdf_file():

        filename = tk.filedialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("PDF File" , "*.pdf"),("All Files","*.*")))
        print(filename)
        entry_pdf.delete(0,tk.END)
        entry_pdf.insert(0,filename)
        if filename:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % filename)
            return filename


Height=600
Width=800

window = tk.Tk()

canvas=tk.Canvas(window, height=Height, width=Width)
canvas.pack()
window.title("Objective Question Generator")

# for image to pdf generator

frame1=tk.Frame(window, bg='white')
frame1.place(relx=0.05, rely=0.05,relwidth=0.9, relheight=0.3)

entry_img=tk.Entry(frame1,bg='white', font=40, bd=5)
entry_img.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.3)

open_btn=tk.Button(frame1, text='Browse image file', command=load_img_file)
open_btn.place(relx=0.45,rely=0.1, relwidth=0.2, relheight=0.3)

btn = tk.Button(frame1, text="Conver image file", bg='gray', font =40, command=lambda: image_to_text(entry_img.get()))
# btn.grid(column=1, row=0)
btn.place(relx=0.25,rely=0.45, relwidth=0.2, relheight=0.3)


# for pdf to objective generator

frame2=tk.Frame(window, bg='white')
frame2.place(relx=0.05, rely=0.4,relwidth=0.9, relheight=0.3)

entry_pdf=tk.Entry(frame2,bg='white', font=40, bd=5)
entry_pdf.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.3)

open_pdf_btn=tk.Button(frame2, text='Browse PDF file', command=load_pdf_file)
open_pdf_btn.place(relx=0.45,rely=0.1, relwidth=0.2, relheight=0.3)

btn = tk.Button(frame2, text="Conver image file", bg='gray', font =40, command=lambda: convert_pdf_to_txt(entry_pdf.get()))
# btn.grid(column=1, row=0)
btn.place(relx=0.25,rely=0.45, relwidth=0.2, relheight=0.3)


window.mainloop()




