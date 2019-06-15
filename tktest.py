from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import Image, ImageTk


def upload():

    pass





class App:
    def __init__(self, master, options):

        fm_title = Frame(master)
        Label(fm_title, text='(1)select model\n(2)upload an image',    # 标签的文字
              bg='green',                 # 背景颜色
              font=('Arial', 12),         # 字体和字体大小
              width=100, height=5).pack()
        fm_title.pack(side=TOP)

        variable = StringVar()
        variable.set(options[0])
        # 使用Frame增加一层容器
        fm_select = Frame(master)
        for i, option in enumerate(options):
            Radiobutton(fm_select, text=option, value=i).pack(anchor=W)
        fm_select.place(x=50, y=100, anchor=NW)

        fm_upload = Frame(master)
        # 要展示的图片
        self.photo = None
        Button(fm_upload, text="选择文件", command=lambda:self.choose_file(fm_upload)).pack(side=LEFT)
        Button(fm_upload, text="上传", command=upload).pack(side=LEFT)
        fm_upload.place(x=200, y=100, anchor=NW)

    def choose_file(self, fm):
        filename = tkinter.filedialog.askopenfilename(filetypes=[('All Files', '*')],
                                                      initialdir='~/Pictures')
        img = Image.open(filename)  # 打开图片
        img = img.resize((400, 300))
        self.photo = ImageTk.PhotoImage(img)
        img_label = Label(fm, image=self.photo)
        img_label.pack(side=TOP)
        print(filename)


root = Tk()
root.geometry('800x600')
root.title("crowd count demo")
model_list = ["csrnet", "new dilated"]

display = App(root, options=model_list)
root.mainloop()
