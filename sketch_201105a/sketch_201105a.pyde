
a=10
b=10
l=10
width=180
height=190
def setup():
    size(width,height)
def draw():
     for t in range(a):
        for i in range(b): 
           x=(i+1)*width/b-(width/b)/2
           y=(t+1)*height/a-(height/a)/2
           line(x,y-(l/2),x,y+(l/2))
    
    
    
