width=800
height=800
nx=8
ny=5
l=40
var = 1
b=[245,86,0,80,152,251,197,11,222,219,205,64,50,251,110]

def setup():
    size (width,height)

def draw():
    q=0
    for i in range(ny):
        for k in range(nx):
            x=((k+1)*width/nx)-((width/nx)/2)
            y=((i+1)*height/ny)-((height/ny)/2)
            fill(color(245,95,14))
            if var == 0:
                line (x,y-(l/2),x, y+(l/2))
            if var == 1 :
            
                    fill(color(b[q],b[q+1],b[q+2]))
                    rect (x-l/2,y-l/2,l,l)
            if var ==2:
                ellipse(x,y,l,l)
        q=q+3
