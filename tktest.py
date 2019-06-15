from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import Image, ImageTk


def inference(img):
    den_map = img
    return den_map, 0


# todo: 获取绑定函数的返回值；布局
class App:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        fm_title = Frame(self.master)
        Label(fm_title, text='(1)select model\n(2)upload an image',    # 标签的文字
              bg='green',                 # 背景颜色
              font=('Arial', 12),         # 字体和字体大小
              width=100, height=5).pack()
        fm_title.pack(side=TOP)

        variable = StringVar()
        variable.set(options[0])
        self.intVar = IntVar()
        # 使用Frame增加一层容器
        fm_select = Frame(self.master)
        for i, option in enumerate(options):
            Radiobutton(fm_select, text=option, value=i, variable=self.intVar,
                        command=self.change,).grid(row=i, column=0, sticky=W)
        # Button(fm_select, text='print', command=self.print_radio).grid(row=0, column=1, columnspan=2)
        self.alg_label = Label(fm_select, text=self.options[int(self.intVar.get())])
        self.alg_label.grid(row=0, column=1, columnspan=2)
        fm_select.place(x=50, y=100, anchor=NW)

        fm_upload = Frame(self.master)

        Button(fm_upload, text="选择文件", command=lambda: self.choose_file()).pack(side=LEFT)
        # Button(fm_upload, text="上传", command=self.upload).pack(side=LEFT)
        fm_upload.place(x=300, y=100, anchor=NW)

        # 要展示的图片
        self.photo = None
        self.den_map = None

    def change(self):
        self.alg_label['text'] = self.options[int(self.intVar.get())]

    def choose_file(self):
        fm_img = Frame(self.master)
        filename = tkinter.filedialog.askopenfilename(filetypes=[('All Files', '*')],
                                                      initialdir='~/Pictures')
        # 什么都没选
        if not filename:
            return
        raw_img = Image.open(filename)  # 打开图片

        img = raw_img.resize((400, 300))
        self.photo = ImageTk.PhotoImage(img)
        img_label = Label(fm_img, image=self.photo)
        img_label.pack(side=LEFT, anchor=NW)

        den_map, count = inference(raw_img)
        den_map = den_map.resize((400, 300))
        self.den_map = ImageTk.PhotoImage(den_map)
        dmp_label = Label(fm_img, image=self.den_map)
        dmp_label.pack(side=LEFT, anchor=NW)

        Label(fm_img, text='估计人数: '+str(count)).pack(side=LEFT, anchor=NW)

        fm_img.place(x=0, y=150, anchor=NW)
        print(filename)

    def upload(self):
        pass

    def print_radio(self):
        print(self.options[int(self.intVar.get())])


root = Tk()
root.geometry('1000x800')
root.title("crowd count demo")
model_list = ["csrnet", "new dilated"]

display = App(root, options=model_list)
root.mainloop()
