import tkinter
import tkinter.messagebox, tkinter.filedialog
from fileUtils import FileUtils
from filechecking import FileCheck
from ziputils import ZipUtils


class UITool(object):
    select_path = None

    def __init__(self):
        super(UITool, self).__init__()

    def on_start(self):
        root = tkinter.Tk()

        root.grid()
        root.geometry("400x500")
        root.wm_title("ui tool")
        top = tkinter.Toplevel()
        top.title
        self.select_path = tkinter.Entry(root)
        self.select_path.insert(0, "请选择文件路径...")
        self.select_path.grid(row=0,column=1)
        btn = tkinter.Button(root, text="选择目标文件", command=self.file_select_dialog)
        btn.grid(row=1,column=1)
        data_btn = tkinter.Button(root, text="data文件修改", command=self.file_modify)
        data_btn.grid(row=2, column=1)
        check_data_btn = tkinter.Button(root, text="目标文件校验", command=self.check_file)
        check_data_btn.grid(row=3, column=1)
        json_data_btn = tkinter.Button(root, text="json文件生成", command=self.create_json)
        json_data_btn.grid(row=4, column=1)
        zip_data_btn = tkinter.Button(root, text="zip文件生成", command=self.create_zip)
        zip_data_btn.grid(row=5, column=1)
        root.mainloop()

    def show(self, msg):
        tkinter.messagebox.showinfo("msg prompt", msg)

    def file_select_dialog(self):
        # 选择文件
        # filename = tkinter.filedialog.askopenfilename()
        dirname = tkinter.filedialog.askdirectory()
        str = self.select_path.get()
        self.select_path.delete(0, len(str))
        self.select_path.insert(0, dirname)

    def check_file(self):
        msg = FileCheck.check(self.select_path.get())
        self.show(msg)

    def file_modify(self):
        msg = FileUtils.file_modify(self.select_path.get())
        self.show(msg)

    def create_json(self):
        FileUtils.read_file(self.select_path.get())
        self.show("success")

    def create_zip(self):
        msg = ZipUtils.zip(self.select_path.get())
        self.show(msg)


if __name__ == '__main__':
    uitool = UITool()
    uitool.on_start()
