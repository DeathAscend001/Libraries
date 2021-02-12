from zipfile import ZipFile
import requests
import os
import sys
import shutil

class Web:
    def UpdateDriver(Self):
        try:
            SELECTION = 'https://chromedriver.storage.googleapis.com/'
            RELEASE_LINK = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'
            DRIVER_NAME = {'Windows':'chromedriver_win32.zip'}
            CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application'
            CHROME_VER = ''

            # Get Latest Version of Chrome
            for root, dirs, files in os.walk(CHROME_PATH):
                CHROME_VER = dirs[0].split('.')[0]
                break
            # COMPLETE RELEASE LINK
            RELEASE_LINK += CHROME_VER

            # Get Full Release for chromedriver
            GetFullRelease = (requests.get(RELEASE_LINK).content).decode('utf-8')

            # Get chromedriver binary
            Driver_Bin = requests.get(SELECTION + GetFullRelease + '/' + DRIVER_NAME.get('Windows'))

            # Generate Zip File
            with open(DRIVER_NAME.get('Windows'), 'wb') as CreateDriver:
                CreateDriver.write(Driver_Bin.content)

            # Extract To C:\bin
            with ZipFile(DRIVER_NAME.get('Windows'), 'r') as driverZip:
                driverZip.extractall('C:\\bin')

            # Create Copy For Python Scripts
            original = r'C:\\bin\\chromedriver.exe'
            target = r'C:\\Users\\trias\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\chromedriver.exe'
            shutil.copyfile(original, target)

            # CleanUp
            os.remove(DRIVER_NAME.get('Windows'))

            print('ChromeDriver Updated')
        except:
            print('Error')

if __name__ == '__main__':
    print('Please use this as library')
    print('or do not put .py when importing')
    Web().UpdateDriver()
    x = input()
    
