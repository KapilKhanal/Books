# -*- coding: utf-8 -*-
"""Turing_Machines.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y7mKGnD27NDbSBR3a-nig5e0U8XXAHyC
"""

class Tape(object):
  blank_symbol = " "
  
  def __init__(self,tape_string = ""):
    self.__tape = dict((enumerate(tape_string)))
    
  def __str__(self):
    s = ""
    min_index = min(self.__tape.keys())
    max_index = max(self.__tape.keys())
    
    for i in range(min_index, max_index):
      s+=self.__tape[i]
    return s
  
  def __getitem__(self,index):
    if index in self.__tape:
      return self.__tape[index]
    else:
      return Tape.blank_symbol
    
  def __setitem__(self,pos,char):
    self.__tape[pos] = char
  
  
class TuringMachine(object):
  def __init__(self, 
              tape = "",
              blank_symbol = " ",
              initial_state = "",
              final_states = None,
              transition_function = None):
  
    self.__tape = Tape(tape)
    self.__head_position = 0
    self.__blank_symbol = blank_symbol
    self.__current_state = initial_state

    if transition_function == None:
      self.__transition_function = {}
    else:
      self.__transition_function = transition_function
    if final_states == None:
      self.__final_states = set()
    else:
      self.__final_states = set(final_states)
    
  def get_tape(self):
    return str(self.__tape)
  
  def step(self):
    char_under_head = self.__tape[self.__head_position]
    x = (self.__current_state,char_under_head)
    if x in self.__transition_function:
      y = self.__transition_function[x]
      self.__tape[self.__head_position] = y[1]
      if y[2] == "R":
          self.__head_position+=1
      elif y[2] == "L":
          self.__head_position-=1
          
      self.__current_state = y[0]
      
  def final(self):
    if self.__current_state in self.__final_states:
      return True
    else:
      return False

initial_state = "init",
accepting_states  = ["final"]
transition_function = {("init","0"): ("init","1","R"),
                      ("init","1"):("init","0","R"),
                       ("init"," "):("init"," ","N")}
final_state = {"final"}

t = TuringMachine("010011",
                 initial_state = "init",
                 final_states = final_states,
                 transition_function = transition_function)
print("Input on Tape:" + t.get_tape())

while not t.final():
  t.step()
  
print("Result of Turing Machine Calculation:")
print(t.get_tape())