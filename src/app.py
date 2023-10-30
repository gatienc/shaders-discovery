
# ---Section 1---


def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)  # Begin the sketch
    glVertex2f(100, 100)  # Coordinates for the bottom left point
    glVertex2f(200, 100)  # Coordinates for the bottom right point
    glVertex2f(200, 200)  # Coordinates for the top right point
    glVertex2f(100, 200)  # Coordinates for the top left point
    glEnd()  # Mark the end of drawing

# This alone isn't enough to draw our square

# ---Section 2---


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    # Remove everything from screen (i.e. displays all white)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset all graphic/shape's position
    iterate()
    glColor3f(1., 0.3, 0.8)  # Set the color to pink
    square()  # Draw a square using our function

    glutSwapBuffers()

# ---Section 3---


def app():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
    glutInitWindowSize(w, h)   # Set the w and h of your window
    # Set the position at which this windows should appear
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice")  # Set a window title
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)  # Keeps the window open
    glutMainLoop()  # Kee   ps the above created window displaying/running in a loop
