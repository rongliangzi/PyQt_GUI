from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk


def inference(img):
    den_map = img
    return den_map, 0


# todo: inference函数和模型的连接
class App:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        fm_title = Frame(self.master, relief='ridge', bd=3, padx=2)
        Label(fm_title, text='(1)select model\n(2)upload an image',    # 标签的文字
              font=('Arial', 12),         # 字体和字体大小
              bg='green',
              width=100, height=5).pack()
        fm_title.place(x=50, y=0, anchor=NW)

        self.intVar = IntVar()
        fm_select = Frame(self.master, relief='sunken', bd=3, pady=2)
        # 循环添加radiobutton
        for i, option in enumerate(options):
            Radiobutton(fm_select, text=option, value=i, variable=self.intVar,
                        command=self.change,).grid(row=i, column=0, sticky=W)
        # Button(fm_select, text='print', command=self.print_radio).grid(row=0, column=1, columnspan=2)
        self.alg_label = Label(fm_select, text=self.options[int(self.intVar.get())])
        self.alg_label.grid(row=0, column=1, columnspan=2)
        fm_select.place(x=50, y=100, anchor=NW)

        fm_upload = Frame(self.master, relief='sunken', bd=3)

        Button(fm_upload, text="选择文件", command=lambda: self.choose_file()).pack(side=LEFT)
        # Button(fm_upload, text="上传", command=self.upload).pack(side=LEFT)
        fm_upload.place(x=300, y=100, anchor=NW)

        # 要展示的图片
        self.photo = None
        self.den_map = None

    # radio button 改变的响应函数，更新alg_label显示内容
    def change(self):
        self.alg_label['text'] = self.options[int(self.intVar.get())]

    # 选择图片，并将原图，生成的密度图，估计的人数，同时显示在界面下方
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

        fm_img.place(x=50, y=150, anchor=NW)
        fm_img.pack()
        print(filename)


if __name__ == '__main__':
    cfg = {'size': '1000x800', 'title': 'crowd count demo', 'model_list': ["csrnet", "new dilated"]}

    root = Tk()
    root.geometry(cfg['size'])
    root.title(cfg['title'])
    model_list = cfg['model_list']

    display = App(root, options=model_list)
    root.mainloop()
