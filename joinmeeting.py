from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from time import sleep
from subprocess import Popen

tm_path = r'C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe'

def enter_meeting(cid, pwd, uname):
    Popen(tm_path, shell=True)
    dlg = Desktop(backend="uia").window(title="腾讯会议(LoadingWnd)")
    dlg.wait('visible ready')
    sleep(1)
    # dlg.print_control_identifiers()
    dlg['加入会议'].click_input()
    sleep(1)
    dlg = Desktop(backend="uia").window(title="腾讯会议(JoinWnd)")
    sleep(1)
    if dlg['入会开启麦克风'].get_toggle_state():
        dlg['入会开启麦克风'].click_input()
    sleep(1)
    if dlg['入会开启摄像头'].get_toggle_state():
        dlg['入会开启摄像头'].click_input()
    sleep(1)
    dlg['会议号Edit'].click_input()
    sleep(1)
    send_keys("c^a{BACKSPACE}")
    sleep(1)
    send_keys(str(cid))
    sleep(1)
    dlg['Join_meeting_Join_meeting'].click_input()
    sleep(1)
    dlg = Desktop(backend="uia").window(title="")
    sleep(1)
    send_keys(str(pwd)+"{ENTER}")
    sleep(1)
    dlg = Desktop(backend="uia").window(title="腾讯会议(InMeetingWnd)")
    print("[Done] joined meeting {} with name = {} .".format(cid,uname))

