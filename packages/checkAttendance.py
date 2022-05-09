import pyautogui, time, os, cv2, numpy as np, pyperclip as pc
from PIL import ImageGrab

def checkAttendance():
    pyautogui.PAUSE = 0
    participants = []
    
    with open(r"assets\data\attendants.txt", 'r') as f:
        for line in f.readlines():
            participants.append(line.strip())


    participantsdupe = participants.copy()
    print("List of participants: " + str(participantsdupe))
    
    #Temporarily change working directory
    old_working_directory = os.getcwd()
    os.chdir("assets/images")
    img = ("search_box.png")

    searchboxpos = pyautogui.locateCenterOnScreen(img)

    while searchboxpos == None:
        searchboxpos = pyautogui.locateCenterOnScreen(img)
        print("Kindly open participants panel in Zoom.")
        time.sleep(30)

    pyautogui.moveTo(searchboxpos)
    pyautogui.click()

    checkboxpos = (searchboxpos.x-150,searchboxpos.y+20,searchboxpos.x+150,searchboxpos.y+100)
    
    blank = cv2.imread(r"absence_blank.png",0)
    for u in  participants:
        pyautogui.write(u)
        time.sleep(0.05)
        im1 = ImageGrab.grab(bbox=checkboxpos)
        im1.save('im1.png')
        cvim1 = cv2.imread('im1.png',0)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press("backspace")
        if np.array_equal(cvim1, blank):
            print(u + " is absent")
            os.remove('im1.png')
        else:
            participantsdupe.remove(u)
            os.remove('im1.png')

    #Change working directory back to original        
    os.chdir(old_working_directory)

    #Print result
    print("Absentees: " + str(participantsdupe))
    pc.copy(str(participantsdupe))
    print("Absentees are copied to clipboard.")
    print("Ran in: " + str(time.perf_counter()))