import tkinter as tk
from tkinter import ttk
from tkinter import Menu
import tkinter.messagebox
from tkinter  import filedialog
from PIL import ImageTk,Image
import os

import scipy.io as scio


class GUI:
    filename='hhh'
    v1=1
    v2=2
    file_counts=5
    auto_change=0


    def __init__(self):
        self.root = tk.Tk()
        self.root.title('回环检测数据处理')
        self.root.geometry("1700x800")
        # 创建主菜单实例
        self.menubar = Menu(self.root)
        # 显示菜单,将root根窗口的主菜单设置为menu
        self.root.config(menu=self.menubar)
        self.interface()

    def interface(self):
        """"界面编写位置"""
        # 在 menubar 上设置菜单名，并关联一系列子菜单
        self.menubar.add_cascade(label="文件", menu=self.papers())
        # self.menubar.add_cascade(label="查看", menu=self.about())
        self.wClose1=tk.Button(self.root,text='不保存关闭',command=self.root.destroy)
        self.wClose1.place(relx=0.95,rely=0.95)
        self.wClose2=tk.Button(self.root,text='保存并关闭',command=self.save_and_close)
        self.wClose2.place(relx=0.9,rely=0.95)
        self.dcm_save=tk.Button(self.root,text='保存',command=self.save_mat)
        self.dcm_save.place(relx=0.85,rely=0.95)
        self.dcm_open=tk.Button(self.root,text='选择文件夹',command=self.get_dir)
        self.dcm_open.place(relx=0.8,rely=0.95)

    def save_and_close(self):
        self.save_mat()
        self.root.destroy()

    def papers(self):
        """
        fmenu = Menu(self.menubar): 创建子菜单实例
        tearoff=1: 1的话多了一个虚线,如果点击的话就会发现,这个菜单框可以独立出来显示
        fmenu.add_separator(): 添加分隔符"--------"
        """
        fmenu = Menu(self.menubar, tearoff=0)
        # 创建单选框
        # for item in ['新建', '打开', '保存', '另存为']:
        #     fmenu.add_command(label=item)
        fmenu.add_command(label='打开文件夹',command=self.get_dir)
        fmenu.add_command(label='保存',command=self.save_mat)
        fmenu.add_command(label='保存并关闭',command=self.save_and_close)
        fmenu.add_command(label='关闭',command=self.root.destroy)

        return fmenu

    def about(self):
        amenu = Menu(self.menubar, tearoff=0)
        # 添加复选框
        for item in ['项目复选框', '文件扩展名', '隐藏的项目']:
            amenu.add_checkbutton(label=item)

        return amenu
    
    def get_dir(self):
        self.filename = filedialog.askdirectory() #获得选择好的文件夹
        for dirpath, dirnames, filenames in os.walk(self.filename):
            self.file_counts = len(filenames)
        self.file_counts-=1
        self.mat_name=self.filename+'/0aa.mat'
        self.mat_data=scio.loadmat(self.mat_name)
        self.mat_arr=self.mat_data['truth']
        # print(self.mat_arr[0][0])
        # print(type(self.mat_arr))
        # self.mat_arr[0][0]=False
        # self.mat_arr[1][1]=True
        
        # self.t1=tk.Entry(self.root,width=20,textvariable=self.v1)
        # self.t1.place(relx=0.25,rely=0.05,relwidth=0.05,relheight=0.05)
        # self.lb1 = tk.Label(self.root,text='id_1')
        # self.lb1.place(relx=0.2,rely=0.05)
        
        # self.t2=tk.Entry(self.root,width=20,textvariable=self.v2)
        # self.t2.place(relx=0.45,rely=0.05,relwidth=0.05,relheight=0.05)
        # self.lb2 = tk.Label(self.root,text='id_2')
        # self.lb2.place(relx=0.4,rely=0.05)
        self.scl = tk.Scale(self.root,orient=tk.HORIZONTAL,length=600,from_=1,to=self.file_counts,label='id1',tickinterval=100,resolution=1,variable=self.v1,command=self.show)
        self.scl.place(relx=0.1,rely=0.7)
        self.sc2 = tk.Scale(self.root,orient=tk.HORIZONTAL,length=600,from_=1,to=self.file_counts,label='id2',tickinterval=100,resolution=1,variable=self.v2,command=self.show)
        self.sc2.place(relx=0.6,rely=0.7)
        self.scl.set(self.v1)
        self.sc2.set(self.v2)
        # self.button2=tk.Button(self.root,text='确认',command=self.show)
        # self.button2.place(relx=0.8,rely=0.8)
        self.button3=tk.Button(self.root,text='id1-1',command=self.id1_minus1)
        self.button3.place(relx=0.25,rely=0.85)
        self.button4=tk.Button(self.root,text='id1-10',command=self.id1_minus10)
        self.button4.place(relx=0.2,rely=0.85)
        self.button5=tk.Button(self.root,text='id1-100',command=self.id1_minus100)
        self.button5.place(relx=0.15,rely=0.85)
        self.button6=tk.Button(self.root,text='id1+1',command=self.id1_add1)
        self.button6.place(relx=0.3,rely=0.85)
        self.button7=tk.Button(self.root,text='id1+10',command=self.id1_add10)
        self.button7.place(relx=0.35,rely=0.85)
        self.button8=tk.Button(self.root,text='id1+100',command=self.id1_add100)
        self.button8.place(relx=0.4,rely=0.85)
        self.button13=tk.Button(self.root,text='id2-1',command=self.id2_minus1)
        self.button13.place(relx=0.75,rely=0.85)
        self.button14=tk.Button(self.root,text='id2-10',command=self.id2_minus10)
        self.button14.place(relx=0.7,rely=0.85)
        self.button15=tk.Button(self.root,text='id2-100',command=self.id2_minus100)
        self.button15.place(relx=0.65,rely=0.85)
        self.button16=tk.Button(self.root,text='id2+1',command=self.id2_add1)
        self.button16.place(relx=0.8,rely=0.85)
        self.button17=tk.Button(self.root,text='id2+10',command=self.id2_add10)
        self.button17.place(relx=0.85,rely=0.85)
        self.button18=tk.Button(self.root,text='id2+100',command=self.id2_add100)
        self.button18.place(relx=0.9,rely=0.85)
        self.dir1=self.filename+'/{}.jpg'.format(self.v1)
        self.dir2=self.filename+'/{}.jpg'.format(self.v2)
        self.img_open1 = Image.open(self.dir1)
        # self.img_open1=self.img_open1.resize((240,360))
        self.img_png1 = ImageTk.PhotoImage(self.img_open1)
        self.label_img1 = tk.Label(self.root, image = self.img_png1)
        self.label_img1.place(relx=0.1,rely=0.1)
        self.img_open2 = Image.open(self.dir2)
        # self.img_open2=self.img_open2.resize((240,360))
        self.img_png2 = ImageTk.PhotoImage(self.img_open2)
        self.label_img2 = tk.Label(self.root, image = self.img_png2)
        self.label_img2.place(relx=0.6,rely=0.1)
        self.loop_flag=tk.StringVar()
        self.info=tk.StringVar()
        if(abs(self.v1-self.v2)<100):
            self.info.set('|id1-id2|<100,默认为非回环')
        else:
            self.info.set('|id1-id2|>=100,需要人工标记')
        
        if(self.mat_arr[max(self.v1,self.v2)-1][min(self.v1,self.v2)-1]==0):
            self.loop_flag.set('不是回环')
        else:
            self.loop_flag.set('是回环')
        # self.loop_flag = self.mat_arr[self.v1][self.v2]

        self.loop_label = tk.Label(self.root, textvariable=self.loop_flag,     # 设置文本内容
                    width=7,               # 设置label的宽度：30
                    height=1,              # 设置label的高度：10
                    justify='left',         # 设置文本对齐方式：左对齐
                    anchor='nw',            # 设置文本在label的方位：西北方位
                    font=('微软雅黑',26),    # 设置字体：微软雅黑，字号：18
                    fg='red',             # 设置前景色：白色
                    bg='grey',              # 设置背景色：灰色
                    padx=2,                # 设置x方向内边距：20
                    pady=1)                # 设置y方向内边距：10
        
        self.loop_label.place(relx=0.5,rely=0.2)
        self.info_label = tk.Label(self.root, textvariable=self.info,     # 设置文本内容
                    width=25,               # 设置label的宽度：30
                    height=1,              # 设置label的高度：10
                    justify='left',         # 设置文本对齐方式：左对齐
                    anchor='nw',            # 设置文本在label的方位：西北方位
                    font=('微软雅黑',16),    # 设置字体：微软雅黑，字号：18
                    fg='blue',             # 设置前景色：白色
                    bg='grey',              # 设置背景色：灰色
                    padx=2,                # 设置x方向内边距：20
                    pady=1)                # 设置y方向内边距：10
        self.info_label.place(relx=0.45,rely=0.05)
        self.button21=tk.Button(self.root,text='自动搜索回环',command=self.sear_loop)
        self.button21.place(relx=0.52,rely=0.35)
        self.button19=tk.Button(self.root,text='标记为是',command=self.mark_true)
        self.button19.place(relx=0.52,rely=0.45)
        self.button20=tk.Button(self.root,text='标记为否',command=self.mark_false)
        self.button20.place(relx=0.52,rely=0.55)
        self.button21=tk.Button(self.root,text='处理下一帧',command=self.mark_next)
        self.button21.place(relx=0.52,rely=0.65)
        self.v = tk.IntVar()
        self.v.set(0)
        self.autochange=tk.Checkbutton(self.root, text="自动切换下一帧",  variable=self.v,command=self.funChooseP)
        self.autochange.place(relx=0.52,rely=0.75)

    def sear_loop(self):
        tmp_1=self.scl.get()-1
        for id in range(self.sc2.get(),self.file_counts,1):
            # print(id)
            if(self.mat_arr[max(tmp_1,id)][min(tmp_1,id)]!=0):
                self.sc2.set(id+1)
                print('搜索成功')
                # break
                return True
            if id==self.file_counts-1:
                tkinter.messagebox.showinfo('提示','没有找到回环')
                return False
        
        self.show(self)


    def mark_next(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1+1)
        self.sc2.set(1)
        self.show(self)
        while(not self.sear_loop()):
            self.v1=self.scl.get()
            self.scl.set(self.v1+1)
            print("next")
            if(self.v1==self.file_counts):
                break
        # self.sear_loop()
        



    def funChooseP(self):
        # print(self.v)
        if(self.v.get()):
            self.auto_change=1
        else:
            self.auto_change=0
        # self.show()

    def mark_true(self):
        
        self.v1=self.scl.get()
        self.v2=self.sc2.get()
        self.mat_arr[max(self.v1,self.v2)-1][min(self.v1,self.v2)-1]=True
        self.sc2.set(self.v2+self.auto_change)
        self.show(self)

    def mark_false(self):
        
        self.v1=self.scl.get()
        self.v2=self.sc2.get()
        self.mat_arr[max(self.v1,self.v2)-1][min(self.v1,self.v2)-1]=False
        self.sc2.set(self.v2+self.auto_change)
        self.show(self)
    
    def save_mat(self):
        scio.savemat(self.mat_name,{'truth':self.mat_arr})
        print("保存成功")
        

    def show(self,zo):        
        self.v1=self.scl.get()
        self.v2=self.sc2.get()
        if(abs(self.v1-self.v2)<100):
            self.info.set('|id1-id2|<100,默认为非回环')
        else:
            self.info.set('|id1-id2|>=100,需要人工标记')
        if(self.mat_arr[max(self.v1,self.v2)-1][min(self.v1,self.v2)-1]==0):
            self.loop_flag.set('不是回环')
        else:
            self.loop_flag.set('是回环')
        self.loop_label.textvariable=self.loop_flag
        self.info_label.textvariable=self.info
        # print(self.v1)
        # print(self.v2)
        self.dir1=self.filename+'/{}.jpg'.format(self.v1)
        self.dir2=self.filename+'/{}.jpg'.format(self.v2)
        self.img_open1 = Image.open(self.dir1)
        # self.img_open1=self.img_open1.resize((240,360))
        self.img_png1 = ImageTk.PhotoImage(self.img_open1)
        self.img_open2 = Image.open(self.dir2)
        # self.img_open2=self.img_open2.resize((240,360))
        self.img_png2 = ImageTk.PhotoImage(self.img_open2)
        self.label_img1.config(image=self.img_png1)  # 设置按钮事件
        self.label_img1.image=self.img_png1
        self.label_img2.config(image=self.img_png2)
        self.label_img2.image=self.img_png2
    
    def id1_minus1(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1-1)
        self.show(self)
    def id1_minus10(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1-10)
        self.show(self)
    def id1_minus100(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1-100)
        self.show(self)

    def id1_add1(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1+1)
        self.show(self)
    def id1_add10(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1+10)
        self.show(self)
    def id1_add100(self):
        self.v1=self.scl.get()
        self.scl.set(self.v1+100)
        self.show(self)

    def id2_minus1(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2-1)
        self.show(self)
    def id2_minus10(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2-10)
        self.show(self)
    def id2_minus100(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2-100)
        self.show(self)

    def id2_add1(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2+1)
        self.show(self)
    def id2_add10(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2+10)
        self.show(self)
    def id2_add100(self):
        self.v2=self.sc2.get()
        self.sc2.set(self.v2+100)
        self.show(self)
        
        



if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()
