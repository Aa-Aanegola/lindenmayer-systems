import turtle
import random
from datetime import datetime
from PIL import Image
import os

class Rule:
    def __init__(self, repl, prob=1):
        self.repl = repl
        self.prob = prob
        
class Lsystem:
    def __init__(self, start="F", ruleset={}):
        self.start = start
        self.ruleset = ruleset
        self.gen = 0
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.window = turtle.Screen()
        self.window.setup(1080, 1080)
        
    
    def process(self):
        transformed = ""
        for char in self.start:
            if char in self.ruleset:
                transformed += self.apply_rule(char)
            else:
                transformed += char
        self.gen += 1
        self.start = transformed
        
    def generate(self, gen=1):
        for i in range(gen):
            self.process()
    
    def reset(self, start):
        self.start = start
        gen = 0
    
    def apply_rule(self, char):
        try:
            prob = random.uniform(0, 1)
            cur = 0
            for r in self.ruleset[char]:
                cur += r.prob
            
            if abs(cur - 1.0) > 0.001:
                print(f"Rule for {char} is invalid (Probabilities do not sum to 1).")
                exit()
                
            for r in self.ruleset[char]:
                cur += r.prob
                if prob < cur:
                    return r.repl
            
        except:
            print(f"No rule has been defined for {char}.")
            exit()
    
    def set_all(self, char_a, char_b='F'):
        self.start = self.start.replace(char_a, char_b)
    
    def get_turtle(self):
        return {"heading":self.turtle.heading(), "position":self.turtle.position()}
    
    def set_turtle(self, state):
        self.turtle.up()
        self.turtle.setheading(state["heading"])
        self.turtle.setposition(state["position"][0], state["position"][1])
        self.turtle.down()
        self.turtle.hideturtle()
        
        
    def draw(self, angle=30, dist=2.5, save=True, file="", fast=True):
        if fast:
            self.window.tracer(0, 0)
            
        stack = []
        for instr in self.start:
            if instr == 'F':
                self.turtle.forward(dist)
            elif instr == 'B':
                self.turtle.backward(dist)
            elif instr == '+':
                self.turtle.right(angle)
            elif instr == '-':
                self.turtle.left(angle)
            elif instr == '[':
                state = self.get_turtle()
                stack.append(state)
            elif instr == ']':
                state = stack.pop()
                self.set_turtle(state)
        turtle.update()
            
        if save:
            if not file:
                date = (datetime.now()).strftime("%d%b%Y-%H%M%S") 
                file = 'img-' + date
                self.turtle.getscreen().getcanvas().postscript(file=file+'.eps')
                img = Image.open(file + '.eps') 
                os.remove(file+'.eps')
                img.save(file + '.jpg')
                