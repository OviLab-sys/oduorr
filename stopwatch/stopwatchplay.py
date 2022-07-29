import turtle as t
from countingstopwatchpy import CountingStopwatch

timer = CountingStopwatch()

def draw_watch(sw):
     """renders the stopwatch object sw in a digital hr: min: sec format."""

     #compute time in hours, minutes, and seconds
     seconds = round(sw.elapsed())
     time = ""
     hours = seconds // 3600   # computing total hours
     seconds %= 3600           # update the remaining seconds
     minutes = seconds // 60   # compute minutes
     seconds %= 60             # update seconds remaining

     time = "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)

     #Draw graphical string
     t.clear()
     t.penup()
     t.setposition(-200, 0)
     t.pendown()
     t.write(time, font=("Ariel", 64, "normal"))
     t.penup()
     t.setposition(-50, -50)
     t.pendown()
     t.write("vicoduorr@runnit.inc", font=("Arial", 24, "normal"))


def quit():
     """quits the program."""           
     t.bye()

def update():
     """updates the program's view of the global stopwatch object."""
     draw_watch(timer)             #draw the digital display
     t.ontimer(update, 500)        #call the update function again after one-half second

t.title("Vicoduorr Stopwatch project")       #set window's titlebar text
t.onkey(timer.start, 's')          #call start method of the timer if uaer presses 's'
t.onkey(timer.stop, 't')           #call stop method of timer if the user presses 't'
t.onkey(timer.reset, 'r')          #call reset method of timer if user presses r
t.onkey(quit, 'q')                 #call quit function if user presses 'q'
t.listen()                         #ensure window recieves keyboard events
t.delay(0)                         #draw as fast as possible
t.speed(0)                         #fastest turtle actions
t.ontimer(update, 500)             #call update function every one-half second
t.hideturtle()                     #donot show the pen when drawing
t.mainloop()                       #start the show