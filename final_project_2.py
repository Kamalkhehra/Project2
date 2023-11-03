import turtle
import random

# Function definitions

def draw_sun(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_cloud(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x + 20, y + 10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

def draw_house(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(250)
        turtle.left(90)
    turtle.end_fill()

    # Draw the roof
    turtle.penup()
    turtle.goto(x, y + 250)
    turtle.pendown()
    turtle.color("darkblue")
    turtle.begin_fill()
    turtle.goto(x + 100, y + 350)
    turtle.goto(x + 200, y + 250)
    turtle.goto(x, y + 250)
    turtle.end_fill()

def draw_window(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def draw_door(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def draw_cherry_blossom_tree(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")  # Change to brown for the stem
    turtle.width(10)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(45)
    turtle.backward(100)

    # Draw cherry blossoms
    turtle.width(1)
    for _ in range(100):
        turtle.penup()
        turtle.goto(x + random.randint(-50, 50), y + random.randint(50, 150))
        turtle.pendown()
        turtle.color("pink")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()

def draw_garden():
    # Get the edges of the canvas
    canvas_width = turtle.window_width()
    canvas_height = turtle.window_height()

    # Set garden dimensions
    garden_width = canvas_width
    garden_height = canvas_height // 4  # Garden takes 1/4 of the height of the canvas

    # Calculate bottom left corner
    bottom_left_x = -garden_width // 2
    bottom_left_y = -canvas_height // 2

    turtle.penup()
    turtle.goto(bottom_left_x, bottom_left_y)
    turtle.pendown()
    turtle.color("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(garden_width)
        turtle.left(90)
        turtle.forward(garden_height)
        turtle.left(90)
    turtle.end_fill()

    return bottom_left_y + garden_height  # Return the y-coordinate of the top of the garden

def draw_flower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # Draw the flower stem
    turtle.color("black")  # Change stem color to black
    turtle.begin_fill()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.end_fill()

    # Draw the flower petals
    turtle.color("red")
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.circle(5)
        turtle.right(90)
    turtle.end_fill()

    # Draw the flower center
    turtle.color("yellow")
    turtle.penup()
    turtle.goto(x, y + 42)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2)
    turtle.end_fill()

# Main scene drawing function

def main():
    turtle.speed(0)
    turtle.bgcolor("lightblue")
    turtle.tracer(0, 0)

    # Set the display size
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    
    # Draw the garden and get the y-coordinate of the top
    top_of_garden_y = draw_garden()

    # Draw sun
    draw_sun(180, 250)

    # Draw clouds
    for i in range(10):  # Reduced number of clouds to 10
        x = random.randint(-screen.window_width()//2, screen.window_width()//2)
        y = random.randint(0, screen.window_height()//2)
        draw_cloud(x, y)

    # Draw house on top of the garden
    house_x = -100
    draw_house(house_x, top_of_garden_y)

    # Draw windows on the house
    draw_window(house_x + 20, top_of_garden_y + 150)
    draw_window(house_x + 130, top_of_garden_y + 150)

    # Draw door on the house
    draw_door(house_x + 75, top_of_garden_y)

    # Draw cherry blossom trees on top of the garden
    # Left side trees
    draw_cherry_blossom_tree(house_x - 220, top_of_garden_y) 
    draw_cherry_blossom_tree(house_x - 340, top_of_garden_y)
    draw_cherry_blossom_tree(house_x - 460, top_of_garden_y) 
    draw_cherry_blossom_tree(house_x - 580, top_of_garden_y) 
    # Right side trees
    draw_cherry_blossom_tree(house_x + 300, top_of_garden_y)   
    draw_cherry_blossom_tree(house_x + 420, top_of_garden_y)  
    draw_cherry_blossom_tree(house_x + 540, top_of_garden_y)   
    draw_cherry_blossom_tree(house_x + 660, top_of_garden_y)  

    # Draw flowers in the garden
    for _ in range(50):
        x = random.randint(-screen.window_width()//2, screen.window_width()//2)
        y = random.randint(-screen.window_height()//2, top_of_garden_y - 20)
        draw_flower(x, y)

    turtle.update()
    turtle.done()

# Running the main function
if __name__ == "__main__":
    main()
