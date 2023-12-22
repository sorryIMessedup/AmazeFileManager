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

    # click the .db file detail
    out = d(className="android.widget.ImageButton", description="map_cache.db").click()
    if not out:
        print("Success: press detail")
    wait()

    # click Open with
    out = d(className="android.widget.TextView", text="Open with").click()
    if not out:
        print("Success: press Open with")
    wait()

    # click database
    out = d(className="android.widget.CheckedTextView", text="database").click()
    if not out:
        print("Success: press database")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)