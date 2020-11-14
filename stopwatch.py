__author__ = 'Srkn'
# ödev olarak yolladığım:http://www.codeskulptor.org/#user39_RPTsk428iaCThoI.py

# mükemmel stopwatch böyle olur diyerek 2.cisini yaptım =))

#http://www.codeskulptor.org/#user39_sCiYESQON1_9.py

#template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
trial = 0
success = 0
counter = 0
started = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    A = t / 600
    B = (t / 10) % 60 / 10
    C =  (t / 10) % 60 % 10
    D =  t % 10
    return str(A) + ":" + str(B) + str(C)+ "." + str(D)

def score():
    return str(success) + " / " + str(trial)

def reset():
    global started
    started = False


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global started
    started = True
    return

#n your stop_handler() function when you check the value of
#the boolean "started" and it's True you must change the value
#of that boolean to False when you stop the timer. That will
#stop the score from increasing when you keep hitting the stop
#button when it's already stopped.

def stop_handler():

    timer.stop()
    if started and (counter % 10) != 0:
        global trial
        trial += 1
    elif started and (counter % 10) == 0:
        global success
        success += 1
        trial += 1
    return reset()


def reset_handler():
    timer.stop()
    global t, trial, success, counter
    t = 0
    trial = 0
    success = 0
    counter = 0

# define event handler for timer with 0.1 sec interval
def timer():
    global t, counter
    t += 1
    counter += 1
    if t == 10000:
        timer.stop()
    else:
        return

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [100, 115], 40, "Black")
    canvas.draw_text("score: " + str(score()), [180, 32], 20, "Blue")


# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200, 150)
frame.add_button('Start', start_handler, 150)
frame.add_button('Stop', stop_handler, 150)
frame.add_button('Reset', reset_handler, 150)
frame.set_draw_handler(draw)
frame.set_canvas_background('White')

# register event handlers
timer = simplegui.create_timer(100, timer)

# start frame
frame.start()

