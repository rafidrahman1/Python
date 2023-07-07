from OpenGL.GL import *
from LabTask2 import midpoint_line_algorithm


def zero(a,b,c):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    
    midpoint_line_algorithm(b, b, b, c)
    midpoint_line_algorithm(b, a, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a) 
    midpoint_line_algorithm(a, b, a, c)  

    glEnd()

'''
def one(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glEnd()
'''
def two(a,b,c):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    #vertical
    midpoint_line_algorithm(a, b, b, b)
    midpoint_line_algorithm(b, c, a, c)
    midpoint_line_algorithm(a, b, a, a)
    midpoint_line_algorithm(a, a, b, a)     
   
    glEnd()
'''
def three(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def four(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)
   
    glEnd()  

def five(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()    

def six(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()  

def seven(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)
 
    #horizontal
    glVertex2f(s,x)
    glVertex2f(a,x)
   
    glEnd()

def eight(a,b):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    x=b+20
    z=b-20
    s=a-20
    #vertical    
    glVertex2f(a, b)
    glVertex2f(a, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    glVertex2f(s, b)
    glVertex2f(s, x)
    
    glVertex2f(s, z)
    glVertex2f(s, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)

    glEnd()

def nine(a,b):
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)
    x=b+20
    z=b-20
    s=a-20

    #verticle
    glVertex2f(a, b) 
    glVertex2f(a, x)

    glVertex2f(s, b)
    glVertex2f(s, x)

    glVertex2f(a, z)
    glVertex2f(a, b)

    #horizontal
    glVertex2f(s,b)
    glVertex2f(a,b)

    glVertex2f(s,z)
    glVertex2f(a,z)
    
    glVertex2f(s,x)
    glVertex2f(a,x)
  
    glEnd()  
    ''' 