import simplegui

class ShapeAttributes:
    def __init__(self, color):
        self.shape_width = 100
        self.shape_color = color
        self.shape_height = 100

class Circle:
    def __init__(self):
        self.radius = 50
        self.center_point = (50, 100)
        
    def setCenter(self, x, y):
        self.center_point = (x, y)

    
class Character:
    
    def __init__(self, color):
        self.circle_shape = Circle() 
        self.shape_attributes = ShapeAttributes(color)
    
    def setCenter(self, x, y):
        self.circle_shape.setCenter(x, y)
    
    def draw_me(self, canvas):
        canvas.draw_circle( self.circle_shape.center_point, 
                           self.circle_shape.radius,self.shape_attributes.shape_width,
                           self.shape_attributes.shape_color  )

        
cliq = Character("green")
pokemon = Character("blue")
pokemon.setCenter(250, 250)
print type (cliq)
cliq.setCenter(350, 25)
message = "Welcome!"
# Handler for mouse click
def click():
    global message
    message = "Good job!"
# Handler to draw on canvas
def draw(canvas):
    cliq.draw_me(canvas)
    pokemon.draw_me(canvas)
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
# Start the frame animation
frame.start()
