# Robot-Code-2020
Welcome to the Infinite Recharge Code for FRC!
There are a few files that are in here since this was our working directory to upload code to be able to work at home.
The files that are useful in this repo are Full Code V2 and Random Things. 
Feel free to poke around at the code and upload commits where they are needed.
Thank you,
Stephen Derenski

----------------------------------------------------------------------------------------------------------------------------------

Installing packages onto the host computer(programming laptop):

py -3 -m pip install [Package]

Downloading and installing packages onto the RoboRIO (IPK packages):

py -3 -m robotpy_installer download-opkg [Package]

py -3 -m robotpy_installer install-opkg [Package]

Deploying code to the roboRIO. Open command line go to where the file/folder is located at.

py -3 robot.py deploy --skip-tests --no-version-check

