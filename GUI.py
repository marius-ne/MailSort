from ReadPhone import ReadPhone
import tkinter
import serial
import time


class GUI(object):

    def __init__(self):
        self.gui()

    def _take_photo(self):
        _ = ReadPhone()
        
    def gui(self):
        gui = tkinter.Tk()
        gui.title('PhoneGui')
        msg = tkinter.Label(text='Take photo',
                            foreground='black',
                            background='white',
                            width='60',
                            height='10')
        msg.pack()

        inp_act = tkinter.Button(text='Run',
                                width='20',
                                height='6',
                                command=lambda : self._take_photo())
        inp_act.pack()
        gui.mainloop()

gui = GUI()