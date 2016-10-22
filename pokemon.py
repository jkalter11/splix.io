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
    def update_x(self, shift_x):
        self.center_point = (
            self.center_point[0] + shift_x,
            self.center_point[1]
        )
        
    
class Character:
    key_map = {
        "left":37,
        "right":39,
        "up":38,
        "down": 40,
        }
    
    
    
    def __init__(self, color):
        self.circle_shape = Circle() 
        self.shape_attributes = ShapeAttributes(color)
        self.move_dist = 10
    def setCenter(self, x, y):
        self.circle_shape.setCenter(x, y)
    
    def draw_me(self, canvas):
        canvas.draw_circle( self.circle_shape.center_point, 
                           self.circle_shape.radius,self.shape_attributes.shape_width,
                           self.shape_attributes.shape_color  )
    def move(self,key):
            if key == 39:
                self.circle_shape.update_x(self.move_dist)
            print key
        
cliq = Character("green")
pokemon = Character("blue")
pokemon.setCenter(250, 250)
print type (cliq)
cliq.setCenter(350, 250)
message = "Welcome!"
# Handler for mouse clic_k
def click():
    global message
    message = "Good job!"
    frame.set_keydown_handler(draw)
# Handler to draw on canvas
def draw(canvas):
    cliq.draw_me(canvas)
    pokemon.draw_me(canvas)
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)
# Start the frame animation
frame.start()
