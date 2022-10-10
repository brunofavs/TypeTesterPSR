# TypeWriterPSR

This program is called "TypeWriterPSR" and was done as a project for the class "Robotic Systems Programming".

The program can work in two distinct ways: the first one is the counted mode, in which the test has a maximum letter value defined and ends as soon as the limit is reached; the seconde one is the timed mode, in which the user does it until the time runs out.
The mode of the test is defined right at the beginning, when calling the function, where the user will have to define at least one variable, the '*--maximum_value*'. This variable represents the maximum number of letter or seconds of the test. If this is the only variable defined, the test will start in the counted mode by default. If we want to switch to the timed mode, we just have to write the variable '-utm', or '*--user_timed_mode*'.
To start the exam, the user just need to press any key and it will start automatically. After that, a countdown will appear and then will appear text with the letter to type. The user will try to write the requested letter as fastest as they can and the answered letter will appear bellow the requested one. If the typed letter is right, the answer text will appear green, but if not, will be red. 
After finishing, the test statistics will appear.
It is also possible to interrupt the test at any point after it started, by pressing the **space bar**.

![Type Writer Example](typewritterpsr.png)

For it to work, 4 different functions were defined: the *main* function, where we used argparse for the mandatory inputs, checks which mode, calls the other functions and prints the test statistics; the *modoTimed*, where was used a for loop for the time countdown and then a while loop for the timed function and returns the correct key, the typed key and the reaction time variables; the *modoCounted*, that uses a for loop for the letter countdown and returns the same variables as the *modoTimed*, that are stored in a namedTuple; and the *buildDict, that uses the namedTuples list to build the test statistics. 
