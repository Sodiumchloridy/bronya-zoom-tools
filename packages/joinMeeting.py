import pyautogui
import subprocess
import time
import pandas as pd
from datetime import timedelta
from datetime import datetime

def joinMeeting(meetingId, meetingPswd):
    pyautogui.PAUSE = 0
    subprocess.Popen(r'C:\Users\DELL\AppData\Roaming\Zoom\bin\zoom.exe')

    joinBtn = ("assets\images\joinBtn.png")
    joinBtnPos = pyautogui.locateCenterOnScreen(joinBtn)
    print("Waiting for Zoom to load...")
    while joinBtnPos == None:
        joinBtnPos = pyautogui.locateCenterOnScreen(joinBtn)
        time.sleep(3)
    pyautogui.click(joinBtnPos)

    idTxtfield = ("assets\images\meetingId.png")
    vidCheckbox = ("assets\images\offVideo.png")

    time.sleep(1)
    idTxtfieldLoc = pyautogui.locateCenterOnScreen(idTxtfield, confidence=0.5)
    print("Loading...")
    while idTxtfieldLoc == None:
        idTxtfieldLoc = pyautogui.locateCenterOnScreen(idTxtfield, confidence = 0.5)
        time.sleep(1)

    pyautogui.click(idTxtfieldLoc)
    pyautogui.write(meetingId)

    vidCheckboxLoc = pyautogui.locateCenterOnScreen(vidCheckbox)
    pyautogui.click(vidCheckboxLoc)
    joinRoom = ("assets\images\joinRoom.png")
    joinRoomLoc = pyautogui.locateCenterOnScreen(joinRoom)
    pyautogui.click(joinRoomLoc)

    meetingPswdfieldLoc = pyautogui.locateCenterOnScreen("assets\images\meetingPswd.png", confidence=0.5)
    print("Loading...")
    while meetingPswdfieldLoc == None:
        meetingPswdfieldLoc = pyautogui.locateCenterOnScreen("assets\images\meetingPswd.png", confidence = 0.5)
        time.sleep(1)
        
    pyautogui.click(meetingPswdfieldLoc)
    pyautogui.write(meetingPswd)
    joinMeetingBtn = pyautogui.locateCenterOnScreen("assets\images\joinMeeting.png")
    pyautogui.click(joinMeetingBtn)

def autoJoin():
    df = pd.read_csv("assets\data\meetings.csv")
    print(df.head())
    await_meeting = True
    while await_meeting:
        now = datetime.now()
        day = datetime.now().strftime("%a")
        modtime = now.strftime("%H:%M")
        
        print("Current Time is: " + now.strftime("%H:%M"))
        try:
            row = df.loc[df[day] == modtime]
            meetingId = str(row.iloc[0,7])
            meetingPswd = str(row.iloc[0,8])
            joinMeeting(meetingId,meetingPswd)
            await_meeting = False
        except:
            time.sleep(60)