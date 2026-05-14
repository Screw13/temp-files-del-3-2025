import pyautogui as pp
import time as tt

x = 0
g = 0

def runt():
    global x
    pp.hotkey("super","r")
    tt.sleep(0.1)
    x = 1 + x
    runt2()

def type(write):
    pp.typewrite(write,0.01)
    pp.hotkey("enter")

def runt2():
    while True:
        run = pp.locateOnScreen('run.png',confidence=0.8)
        if run != None:
            print("Run terminal HTHFC protocol")
            if x == 1:
                type("temp")
                fdel()
            elif x == 2:
                type("%temp%")
                fdel()
                tick()
            elif x == 3:
                type("shell:recyclebinfolder")
                fdel()
            else:
                pp.hotkey("esc")
                print('HTHFC')
                tt.sleep(0.1)
                print("saper last no 3361")
                tt.sleep(0.1)
                print("terminating.")
                tt.sleep(0.5)
                quit()
        else:
            print("Run terminal protocol 3361")
            tt.sleep(1)

def fdel():
    tt.sleep(0.5)
    while True:
        fdel2 = pp.locateOnScreen("fdel2.png",confidence=0.8)
        if fdel2 != None:
            tt.sleep(0.1)
            pp.moveTo(fdel2)
            pp.moveRel(0,35)
            pp.click()
            pp.hotkey("ctrl","a")
            tt.sleep(0.2)
            pp.hotkey('delete')
            tt.sleep(1)
            if x < 3:
                tick()
            else:
                rbc()
                pp.hotkey("enter")
                close()
        else:
            print("file explorer protocol 3361")
            tt.sleep(1)

def close():
    global g
    g = 0
    while True:
        x2 = pp.locateOnScreen("x.png",grayscale=True)
        if x2 != None:
            pp.click(x2)
            runt()
        else:
            tt.sleep(0.1)

def tick():
    global g
    while g < 15:
        tic = pp.locateOnScreen("tickbox.png")
        if tic != None:
            pp.click(tic)
            pp.click(pp.locateOnScreen("skip.png",confidence=0.8))
            break
        else:
            g = 1 + g
            tt.sleep(0.1)
    close()

def rbc():
    while True:
        rbc = pp.locateOnScreen("rbc.png",confidence=0.8)
        if rbc != None:
            break
        else:
            tt.sleep(0.2)
            print("locating rbc")

runt()