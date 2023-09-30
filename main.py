from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

colors = {'white': (255,255,255), 'black': (0,0,0)}
canvas_color = input('Enter canvas background (white/black): ')

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type= input('What do you like to draw (rectangle/square) ? Enter quit to quit.')
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x of the rectangle: '))
        rec_y = int(input('Enter y of the rectangle: '))
        rec_width = int(input('Enter the width of the rectangle: '))
        rec_height = int(input('Enter the height of the rectangle: '))
        red = int(input('How much red should the rectangle have? '))
        green = int(input('How much green should the rectangle have? '))
        blue = int(input('How much blue should the rectangle have? '))

        #Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red,green,blue))
        r1.draw(canvas)

    if shape_type.lower() == 'square':
        sqr_x = int(input('Enter x of the square: '))
        sqr_y = int(input('Enter y of the square: '))
        sqr_width = int(input('Enter the side length of the square: '))
        red = int(input('How much red should the square have? '))
        green = int(input('How much green should the square have? '))
        blue = int(input('How much blue should the square have? '))

        #Create the rectangle
        s1 = Square(x=sqr_x, y=sqr_y, width=sqr_width, color=(red,green,blue))
        s1.draw(canvas)


    if shape_type == 'quit':
        break


canvas.make('/Users/popicavlad/Desktop/Python/files-master/App-3-Project-Math-Painting/files/pic.png')
