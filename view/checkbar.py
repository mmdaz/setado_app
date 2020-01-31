from tkinter import *
class CheckBar:
   def __init__(self, parent, picks=[], side=LEFT, anchor=W):
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(parent, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)