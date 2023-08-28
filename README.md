# BMICalc

<b>PROJECT TITLE<b></br></br>
BMI CALCULATOR<br></br>
<b>DESCRIPTION</b></br></br>
The BMI Calculator is a GUI program to calculate the user's Body Mass based on their weight and height. The program is written in python programming language and it is in no way to replace the one seen online. This can be used on the Desktop but more features will be added later.
<b>USAGE<b></br></br>
<b>STEP 1:</b> When the application loads, you will see the Graphical User Interface (GUI) as shown below:</br></br>
![BMIINTERFACE](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/dc8113b3-9a36-4942-b0c3-3f732ff4d7da)

STEP 2: Input your Feet, Height, and Weight in each field's respective textbox (See Figure 1 above)</br></br>
STEP 3: Click the Calculate BMI button to show the caculation and remark (Figure 2)</br></br>
![BMICALC](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/f8ce6e35-7f03-4a73-ae55-6f0598b00a5e)

<b>ERROR CORRECTION</b></br></br>
As with any good program, each input is checked first before calculating the BMI and generating the remark.</br></br>
![BMI](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/0c537e43-c32e-4542-b846-ecab48bf08e2)

<b>VERSION UPDATE<b>
The version is BMIC Ver 1 and any update will be shown here.</br></br>  

<b>DEPLOYMENT<b>
To run this file, make sure that pythonis installed (Using Python 3.9 or more) and press F5 using IDLE IDE. But any IDE like Visual Studio Code or any IDE will do. To convert to an executable (.exe), you have two options: </br></br>
<b>STEP1:</b> First install pyinstaller via the command line or terminal by typing...pip install pyinstaller</br></br>
<b>STEP 2:</b> Type the following in the command line.</br></br>
pyinstaller --onefile --windowed --add-data "xi.icon;" BMI.py </br></br>
<b>STEP 3:</b> Allow pyinstaller to compile the file and add all the resources and dependencies needed to create the executable.</br></br>
<b>STEP 4:</b> Check the folder and run the exe in another computer. It will successfully run</br></br>
Alternatively (and even better option), you can use auto-py-to-exe to generate the executable. This normally opens a GUI for compiling your programs. First install auto-py-to-exe by typing the following in the commandline: pip install auto-py-to-exe and then follow the steps as shown below:</br></br>
![i](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/fdfddf15-e666-4177-b836-b58a976c8741)

Notice that python39.dll was added. This will help run the program in older versions of Windows eg Windows 7, 8, 8.1 (probably they have not been updated for a long time. This will avoid generating errors such as the one shown in issues section). 
<b>ISSUES</b></br></br>
Please note that your Windows Defender Antivirus (and some other antimalware programs) may block the application from running. This is a false positive error message. Kindly pause the protection for a while and run again
The dependency python39 must be added to avoid errors such as the one shown below:</br></br>
![python39 error](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/cf518618-3e79-451a-89d2-1d0536a803e6)</br></br>
![Failed Message DLL](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/e1151496-3f4c-469b-8c96-eed3249f8419)</br></br>

The python39 is saved in the AppData folder. As shown in the image below:</br></br>
![python39](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/eef0a52f-d662-4438-a42c-c8c58fc769c4)</br></br>
![i](https://github.com/ObiorahDivineMercy/BMICalc/assets/143182629/4c86b3f8-a685-4af1-8afe-a4471c7b7ee8)


STEP 2: Type the following in the command line
pyinstaller --onefile --windowed --add-data "xi.icon;" BMI.py
STEP 3: Allow pyinstaller to compile the file and add all the resources and dependencies needed to create the executable.
STEP 4: Check the folder and run the exe in another computer. It will successfully run
Alternatively (and even better option), you can use auto-py-to-exe to generate the executable. This normally opens a GUI for compiling your programs. First install auto-py-to-exe by typing the following in the commandline: pip install auto-py-to-exe and then follow the steps as shown below:
ADD IMAGE
Notice that python39.dll was added. This will help run the program in older versions of Windows eg Windows 7, 8, 8.1 (probably they have not been updated for a long time. This will avoid generating errors such as the one shown in issues section). 
ISSUES
Please note that your Windows Defender Antivirus (and some other antimalware programs) may block the application from running. This is a false positive error message. Kindly pause the protection for a while and run again
The dependency python39 must be added to avoid errors such as the one shown below:
ADD IMAGE
The python39 is saved in the AppData folder. As shown in the image below:
ADD IMAGE

