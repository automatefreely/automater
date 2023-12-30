from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from handler.storage.objsVariables.condition import Condition

from handler.storage.objsVariables.situation import Situations

from objects.ActionObjects import (
    FindImage, FindImageScrolling, MouseClick, MoveMouse, PressKey, 
    ReleaseKey, Screenshot, Scroll, Speak, Wait, Write)

from objects.ConditionObjects import IfImageCondition
from objects.SituationObjects import IfSituation
from objects.dowhati import Listener

from handler.storage.mainObject import MainObject

from handler.models.text import Text

import time


def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class ActionBuilder():
    def __init__(self):
        self.mainObject=MainObject()
    def clear(self):
        self.mainObject.clear()
    def backspace(self):
        self.mainObject.popAction()
    def save(self, file_name):
        self.mainObject.save(file_name=file_name+".af")
    def load(self, file_name, append=False):
        self.mainObject.load(file_name=file_name+".af", append=append)
    @timeit
    def run(self):
        self.mainObject.run()
    def print(self):
        for action in self.mainObject.actionList():
            print(action)
    def moveMouse(self, to, scrolling=False, grayscale=False, confience=0.9):
        if to=="point":
            MoveMouse().record().saveTo(self.mainObject)
            return
        if scrolling==False:
            FindImage().record(grayscale, confience).saveTo(self.mainObject)
            return
        FindImageScrolling().record(grayscale= grayscale, confience= confience, x_scroll=0, y_scroll=1, scroll_time=0.2).saveTo(self.mainObject)
    def wait(self, time):
        Wait().record(time = time).saveTo(self.mainObject)
    def speak(self,text):
        Speak().record(Text(text)).saveTo(self.mainObject)
    def click(self, clicks,interval):
        MouseClick().record(clicks=clicks, interval=interval).saveTo(self.mainObject)
    def scroll(self, noOfRolls):
        Scroll().record(x = 0, y = noOfRolls).saveTo(self.mainObject)
    def write(self, text, interval):
        Write().record(text=Text(text), interval=interval).saveTo(self.mainObject)
    def key(self, press):
        if press==True:
            key = PressKey().record()
            key.saveTo(self.mainObject)
            return key
        ReleaseKey().record().saveTo(self.mainObject)
    def takeScreenshot(self, image_name):
        Screenshot().record().saveTo(self.mainObject)
    @timeit
    def dowhati(self):
        listen=Listener()
        listen.start()
        self.mainObject.extend(listen.mainObject)


class SituationsBuilder():
    def __init__(self):
        self.situations = Situations()
        self._condition = None
        self._action_object = None
        
    def get_action(self, gui):
        gui.calling(True)
        actionBuilder = ActionBuilder()
        collect_action = CollectActions(actionBuilder = actionBuilder)
        collect_action.mainloop()
        collect_action.destroy()
        self._action_object = actionBuilder.mainObject
        gui.calling(False)
        
    def get_condition(self, condition: Condition = IfImageCondition):
        self._condition = condition().record(grayscale= False, confience=1)
        
    def create_situation(self):
        if_situation = IfSituation().directRecord(condition=self._condition, action_object=self._action_object)
        
        self.situations.append(if_situation)

        print(f"Situation appended to Situations: {if_situation}")

    def saveTo(self, mainObject: MainObject):
        self.situations.saveTo(mainObject=mainObject)


class CollectActions(Tk):
    """docstring for Automate"""
    def __init__(self, actionBuilder: ActionBuilder):
        super().__init__()
        self.actionBuilder = actionBuilder
        self.bind('<Escape>', lambda e: self.quit())
        
        
        # Constant defination
        self._main_bg_color="#dcdcde"
        self._main_image = "main_image.png"
        self.height = 400
        self.width = 750

        # Setting constant
        self.title("Automater")
        self.geometry(f"{self.width}x{self.height}")
        self.configure(bg=self._main_bg_color)
        ##comment this line will make conditin option work
        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(self._main_image).copy()))
        
        self.l1=Label(self,text="Automator")
        self.l1.config(anchor=CENTER,font=('Helvetica bold',30),bg=self._main_bg_color)
        self.l1.pack()

        self.frame1=LabelFrame(self,text="",bg=self._main_bg_color)
        self.frame1.pack(padx=5,pady=5)
        # ------
        self.frame11=LabelFrame(self.frame1,text="Options",bg=self._main_bg_color)
        self.frame11.grid(padx=5,pady=5)
        b_click=Button(self.frame11, text="Click", command=self.clicker)
        b_click.grid(row=1,column=0,padx=5,pady=5,sticky=(W,E))
        b_wait=Button(self.frame11, text="Wait", command=self.waitfor)
        b_wait.grid(row=1,column=1,padx=5,pady=5,sticky=(W,E))
        b_speak=Button(self.frame11, text="Speak", command=self.speak)
        b_speak.grid(row=1,column=2,padx=5,pady=5,sticky=(W,E))
        b_dowhati=Button(self.frame11, text="Do What I",fg="white", bg="blue",command=self.listenAllActions)
        b_dowhati.grid(row=1,column=3,padx=5,pady=5,sticky=(W,E))
        b_print=Button(self.frame11, text="print",fg="white", bg="black",command=lambda: self.actionBuilder.print())
        b_print.grid(row=1,column=4,padx=5,pady=5,sticky=(W,E))
        b_if=Button(self.frame11, text="if",command=self._if)
        b_if.grid(row=1,column=5,padx=5,pady=5,sticky=(W,E))

        b_write=Button(self.frame11, text="Write", command=self.writer)
        b_write.grid(row=2,column=0,padx=5,pady=5,sticky=(W,E))
        b_key=Button(self.frame11, text="Key", command=self.key)
        b_key.grid(row=2,column=1,padx=5,pady=5,sticky=(W,E))
        b_scroll=Button(self.frame11, text="Scroll", command=self.scroller)
        b_scroll.grid(row=2,column=2,padx=5,pady=5,sticky=(W,E))
        b_screenshot=Button(self.frame11, text="Screenshot", command=self.screenshotTaker)
        b_screenshot.grid(row=2,column=3,padx=5,pady=5,sticky=(W,E))
        b_moveto=Button(self.frame11, text="Move To", command=self.move)
        b_moveto.grid(row=2,column=4,padx=5,pady=5,sticky=(W,E))
        b_untill=Button(self.frame11, text="untill", command=lambda: self._untill)
        b_untill.grid(row=2,column=5,padx=5,pady=5,sticky=(W,E))
        # ---------
        self.frame12=LabelFrame(self.frame1,text="Settings",bg=self._main_bg_color)
        self.frame12.grid(row=0,column=1,padx=5,pady=5)
        b_clear=Button(self.frame12, text="clear",command=lambda: self.actionBuilder.clear())
        b_clear.grid(row=0,column=0,padx=5,pady=5,sticky=(W,E))
        b_save=Button(self.frame12, text="save",command=self.saving)
        b_save.grid(row=0,column=1,padx=5,pady=5,sticky=(W,E))
        b_app=Button(self.frame12, text="app",command=lambda: whatnext("app"))
        b_app.grid(row=0,column=2,padx=5,pady=5,sticky=(W,E))
        b_run=Button(self.frame12, text="run",command=self.runit)
        b_run.grid(row=1,column=0,padx=5,pady=5,sticky=(W,E))
        b_repeat=Button(self.frame12, text="repeat",command=lambda: whatnext("repeat"))
        b_repeat.grid(row=1,column=1,padx=5,pady=5,sticky=(W,E))
        b_setting=Button(self.frame12, text="setting",command=lambda: whatnext("settings"))
        b_setting.grid(row=1,column=2,padx=5,pady=5,sticky=(W,E))
        b_load=Button(self.frame12, text="load",command=self.loader)
        b_load.grid(row=0,column=3,padx=5,pady=5,sticky=(W,E))
        b_backspace=Button(self.frame12, text="backspace",command=lambda: whatnext("backspace"))
        b_backspace.grid(row=1,column=3,padx=5,pady=5,sticky=(W,E))
        self.frame2=LabelFrame(self,padx=5,pady=5)
        self.frame3=LabelFrame(self,padx=5,pady=5)

    def _if(self):
        self.frame3.pack()
        situationsBuilder = SituationsBuilder()
            
        l_if=Label(self.frame3,text='if       ').grid(row=0,column=0,rowspan=3)
        b_image=Button(self.frame3,text="image", command= lambda: situationsBuilder.get_condition())
        b_image.grid(row=0,column=1,sticky=(W,E))
        b_color=Button(self.frame3,text="color",command=lambda: situationsBuilder.get_condition())
        b_color.grid(row=1,column=1,sticky=(W,E))
        b_else=Button(self.frame3,text="else",command=lambda: situationsBuilder.get_condition())
        b_else.grid(row=2,column=1,sticky=(W,E))
        b_click=Button(self.frame3,text="click",command=lambda: situationsBuilder.get_condition())
        b_click.grid(row=3,column=1,sticky=(W,E))
        Label(self.frame3,text='     then       ').grid(row=0,column=4,rowspan=3)
        Button(self.frame3,text="Do",
               command=lambda: situationsBuilder.get_action(self)
               ).grid(row=0,column=3,rowspan=4,sticky=(N,S))

        Label(self.frame3,text='     now    ').grid(row=0,column=2,rowspan=3)
        
        Button(self.frame3,text="save",
                command=lambda: situationsBuilder.create_situation()
                ).grid(row=0, column=5, rowspan=4, sticky=(N,S))
        
        Button(self.frame3,text="Done",fg="white", bg="black",
                 command = lambda: situationsBuilder.saveTo(self.actionBuilder.mainObject)
                 ).grid(row=4, columnspan=4,sticky=(W,E))
    def _untill(self):
        pass
    def calling(self,a):
        if a==True:
            self.withdraw()
        elif a==False:
            self.deiconify()

    def comming(self,a):
        if a==True:
            for child in self.frame2.winfo_children():
                child.grid_forget()
            self.frame2.pack()
        elif a==False:
            for child in self.frame2.winfo_children():
                child.grid_forget()
            self.frame2.pack_forget()

    def waitfor(self):
        def mo():
            self.actionBuilder.wait(float(e.get()))
            self.comming(False)
        self.comming(True)
        l=Label(self.frame2,text="tell the time").grid(row=0,column=0)
        e=Entry(self.frame2)
        e.grid(row=0,column=1)
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=1, columnspan=3,sticky=(W,E))
    
    def screenshotTaker(self):
        def mo():
            self.comming(False)
            self.actionBuilder.takeScreenshot(image_name=e_name.get(), time=e_time.get(), size=size.get())
        self.comming(True)
        size=StringVar()
        l_time=Label(self.frame2,text="After how mmany secons").grid(row=0,column=0)
        e_time=Entry(self.frame2)
        e_time.grid(row=0,column=1)
        e_time.insert(0,"0")
        l_name=Label(self.frame2,text="number of rouns").grid(row=1,column=0)
        e_name=Entry(self.frame2)
        e_name.grid(row=1,column=1)
        e_name.insert(0,"Screen")
        b_partly=Radiobutton(self.frame2,text="Partly", variable=size, value="partly")
        b_partly.grid(row=2,column=0)
        b_full=Radiobutton(self.frame2,text="Full screen", variable=size, value='full screen')
        b_full.grid(row=2,column=1)
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=3, columnspan=3,sticky=(W,E))
        size.set("full screen")

    def runit(self):
        self.calling(True)
        self.actionBuilder.run()
        self.calling(False)

    def speak(self):
        
        self.comming(True)
        def mo():
            self.actionBuilder.speak(e.get())
            # action_list[j[:5]+str(temp)]=e.get()
            self.comming(False)
        l=Label(self.frame2,text="Tell the text").grid(row=0,column=0)
        e=Entry(self.frame2)
        e.grid(row=0,column=1)
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=1, columnspan=3,sticky=(W,E))
    
    def move(self):
        self.comming(True)
        radio = StringVar()
        radio.set("point")
        def c(value):
            global grayscale,e_tolerance
            if value==True:
                grayscale = IntVar()
                grayscale.set(0)
                l_grayscale=Label(self.frame2,text="grayscale").grid(row=1,column=0)
                b_true=Radiobutton(self.frame2,text="true", variable=grayscale, value=1)
                b_true.grid(row=1,column=1)
                b_false=Radiobutton(self.frame2,text="false", variable=grayscale, value=0)
                b_false.grid(row=1,column=2)


                l_tolerance=Label(self.frame2,text="confience").grid(row=2,column=0)
                e_tolerance=Entry(self.frame2)
                e_tolerance.grid(row=2,column=1)
                e_tolerance.insert(0,"1")
        def mo():
            s=radio.get()
            if s=='point':
                self.calling(True)
                self.actionBuilder.moveMouse(to='point')
                self.calling(False)
            elif s=='image':
                self.calling(True)
                self.actionBuilder.moveMouse( 
                    to='image', 
                    scrolling=False, 
                    grayscale=bool(grayscale.get()), 
                    confience=float(e_tolerance.get()))
                self.calling(False)
            elif s=='image scrolling':
                self.calling(True)
                self.actionBuilder.moveMouse( 
                    to='image', 
                    scrolling=True, 
                    grayscale=bool(grayscale.get()), 
                    confience=float(e_tolerance.get()))
                self.calling(False)
            self.comming(False)
        b_point=Radiobutton(self.frame2,text="Point", variable=radio, value="point")
        b_point.grid(row=0,column=0)
        b_image=Radiobutton(self.frame2,text="Image", variable=radio, value='image',command=lambda:c(True))
        b_image.grid(row=0,column=1)
        b_image_scrolling=Radiobutton(self.frame2,text="Image Scrolling", variable=radio, value='image scrolling',command=lambda:c(True))
        b_image_scrolling.grid(row=0,column=2)
        go = Button(self.frame2, text="Ok", fg="white", bg="black", command=mo)
        go.grid(row=3, columnspan=3,sticky=(W,E))

    def clicker(self):
        def mo(clicks,interval):
            self.actionBuilder.click(clicks,interval)
            self.comming(False)
        self.comming(True)
        l_type=Label(self.frame2,text="which click").grid(row=0,column=0)
        l_no=Label(self.frame2,text="number of clicks").grid(row=1,column=0)
        e_no=Entry(self.frame2)
        e_no.grid(row=1,column=1)
        e_no.insert(0,"1")
        l_time=Label(self.frame2,text="Time gap between clicks").grid(row=2,column=0)
        e_time=Entry(self.frame2)
        e_time.grid(row=2,column=1)
        e_time.insert(0,"0")
        b_ok=Button(self.frame2,text="Ok", fg="white", bg="black",command=lambda: mo(clicks=int(e_no.get()),interval=float(e_time.get()))).grid(row=3, columnspan=2,sticky=(W,E))

    def scroller(self):
        def mo():
            self.actionBuilder.scroll(int(e.get()))
            self.comming(False)
        self.comming(True)
        l=Label(self.frame2,text="number of rouns").grid(row=0,column=0)
        e=Entry(self.frame2)
        e.grid(row=0,column=1)
        e.insert(0,"0")
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=1, columnspan=3,sticky=(W,E))

    def writer(self):
        self.comming(True)
        def mo():
            print(1111)
            self.actionBuilder.write(text=str(e.get()),interval=float(e_time.get()))
            self.comming(False)
        l=Label(self.frame2,text="text to enter").grid(row=0,column=0)
        e=Entry(self.frame2)
        e.grid(row=0,column=1)
        l_time=Label(self.frame2,text="Time gap between latter insertion").grid(row=2,column=0)
        e_time=Entry(self.frame2)
        e_time.grid(row=2,column=1)
        e_time.insert(0,"0")
        b_ok=Button(self.frame2,text="Ok", fg="white", bg="black",command=mo).grid(row=3, columnspan=2,sticky=(W,E))

    def key(self):
        self.comming(True)
        radio = StringVar()
        radio.set("point")
        def keydetect(dowhat):
            if dowhat=="press":
                try:
                    lrelease.pack_forget()
                except Exception as e:
                    print(e)
                lpress=Label(self.frame2, text="To press ")
                lpress.grid(row=1, columnspan=2,sticky=(W,E))
            if dowhat=="release":
                try:
                    lpress.pack_forget()
                except Exception as e:
                    print(e)
                lrelease=Label(self.frame2, text="To release ")
                lrelease.grid(row=1, columnspan=2,sticky=(W,E))
        def mo():
            s=radio.get()
            if s=='press':
                self.actionBuilder.key(press=True)
            elif s=='release':
                self.actionBuilder.key(press=False)
            self.comming(False)
        b_point=Radiobutton(self.frame2,text="Press", variable=radio, value="press", command=lambda:keydetect("press"))
        b_point.grid(row=0,column=0)
        b_image=Radiobutton(self.frame2,text="Release", variable=radio, value='release', command=lambda:keydetect("release"))
        b_image.grid(row=0,column=1)
        go = Button(self.frame2, text="Ok", fg="white", bg="black", command=mo)
        go.grid(row=2, columnspan=3,sticky=(W,E))

    def listenAllActions(self):
        self.calling(True)
        res = messagebox.askquestion('dowhati', 'Automater will recor your action on clicking Yes')
        if res=="yes":
            self.actionBuilder.dowhati()
        self.calling(False)
    
    def saving(self):
        def mo():
            self.actionBuilder.save(e.get())
            self.comming(False)
        self.comming(True)
        l=Label(self.frame2,text="name of file").grid(row=0,column=0)
        e=Entry(self.frame2)
        e.grid(row=0,column=1)
        e.insert(0,"automater1")
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=1, columnspan=3,sticky=(W,E))

    def loader(self):
        def mo():
            self.calling(True)
            self.actionBuilder.load(e_save.get())
            self.calling(False)
            self.comming(False)
        self.comming(True)
        l_save=Label(self.frame2,text="name of file")
        l_save.grid(row=0,column=0)
        e_save=Entry(self.frame2)
        e_save.grid(row=0,column=1)
        b=Button(self.frame2,text="ok",fg="white", bg="black",command=mo).grid(row=3, columnspan=3,sticky=(W,E))
