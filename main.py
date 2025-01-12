import pyautogui
import time

SLEEP_INTERVAL = 7 # 5 for the download and 2 for the window to open and locate the button
SECONDARY_SLEEP = 0.5 #if it doesnt find the button when it should it will wait a little then try again vs waiting the whole SLEEP_INTERVAL


print("STARTING IN 5 SECONDS")
print("Please open the download window")
time.sleep(5)


timesNotFound = 0



while timesNotFound < 10:
    downloadButton = pyautogui.locateCenterOnScreen('download.png')
    while(downloadButton is None):
        downloadButton = pyautogui.locateCenterOnScreen('download.png')
        darkDownloadButton = pyautogui.locateCenterOnScreen('darkDownload.png')
        if(darkDownloadButton is not None):
            downloadButton = darkDownloadButton
            break
        if(downloadButton is not None):
            break

        time.sleep(SECONDARY_SLEEP)


    pyautogui.moveTo(downloadButton)
    pyautogui.click()
    time.sleep(SLEEP_INTERVAL)






