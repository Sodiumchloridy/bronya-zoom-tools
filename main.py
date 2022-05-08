import time, os, sys

# Lazy Imports
# from pathlib import Path
# from packages import checkAttendance, joinMeeting

studentnum = 48

def welcome(selection=None):
    print("Welcome to Bronya's Automatic Zoom Tools")
    print("Enter 1 to Automatically Join Meetings")
    print("Enter 2 to Check Participant Attendance")

    #Change Working Directory to File Directory
    from pathlib import Path
    base = Path(__file__).absolute().parent
    os.chdir(base)

    if selection == None:
        selection = input("Your selection: ")
    if selection == "1":
        from packages import joinMeeting
        print("Initiating Auto Join...")
        joinMeeting.autoJoin()
    elif selection == "2":
        from packages import checkAttendance
        print("Checking Attendance...")
        checkAttendance.checkAttendance(studentnum)
        print("Task complete.")
        if input("Do you wish to rerun the attendance check? (y/n): ") == "y":
            checkAttendance.checkAttendance(studentnum)
        else: 
            sys.exit()
    else:
        print("Kindly input a valid option.")
        time.sleep(3)
        welcome()


try:
    if sys.argv[1] == "1":
        welcome(1)
except:
    welcome()