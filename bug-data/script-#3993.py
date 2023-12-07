# bug reproduction script for bug #3882 of AmazeFileManager
import sys
import time

import uiautomator2 as u2

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    d.app_start("com.amaze.filemanager.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.amaze.filemanager.debug":
            break
        time.sleep(2)
    wait()

    # click the Navigation
    out = d(className="android.widget.ImageButton", description="Open navigation").click()
    if not out:
        print("Success: press Navigation")
    wait()

    # scroll down the Navigation
    out = d(className="android.support.v7.widget.RecyclerView",
            resourceId="com.amaze.filemanager.debug:id/recycler_view").swipe("up")
    if out:
        print("Success: scroll down")
    wait()

     # click the Settings
    out = d(className="android.widget.CheckedTextView", text="Settings").click()
    if not out:
        print("Success: press Settings")
    wait()

    # click Appearence
    out = d(className="android.widget.TextView", text="Appearence").click()
    if not out:
        print("Success: press Appearence")
    wait()

    # click Theme
    out = d(className="android.widget.TextView", text="Theme").click()
    if not out:
        print("Success: press Theme")
    wait()

    # click the Settings
    out = d(className="android.widget.CheckedTextView", text="Daytime").click()
    if not out:
        print("Success: press Daytime")
    wait()

     # click any Folder
    out = d(className="android.widget.TextView", text="Android").click()
    if not out:
        print("Success: press Android")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)