# FCP-CW3

· Please read this README file first before running the program! Thank you.


· In the FCP-CW3 folder, you will find 4 items: 
1. Folder "grids",  which contain some unmodified original sudokus. Please note the extension of these files, some of them are ".txt" and some don't have extension.

2. Folder "output", if you use flag"--file", completed Sudoku will be output to this folder.

3. CW3.py, This is the main program, please run it in the terminal, we recommend "Git Bash".

4. README.md



· How to run the program:
1. Please make sure you are using Windows operating system to run this program. We do not ensure that this program will run under linux, and this program can not running on the Apple computer (Mac)!

2. Make sure you install python 3.8 or newer version and these libraries are installed in the computer(Some of these are built into python):  copy, time, matplotlib.pyplot, numpy, random, sys, os, os.path, re.

3. Open terminal, type "python + CW3.py" "python + CW3.py + flags", for instance:
"python CW3.py"  (no flag)
"python CW3.py --explain" (With explain flag)
"python CW3.py --file hard1"  (With file flag and the no extension filename)
"python CW3.py --file easy1.txt"  (With file flag and the file with extension)
"python CW3.py --explain --hint2 --file hard1"  (With multiple flags)
......
etc.

4. If you you not using flag, you will see the 6 solved grids printed in the terminal,  the running time of CW2 solver (it shows as Default solver) and the running time of Wavefront solver.

5. If you want to use flags, please take a look at the introduction below.



· Introduction of flags:
1. --explain: This flag is using to tell you how to fill the original Sudoku into a completed Sudoku , it will interact with other flags.

2. --file: This flag allows you to input a file from folder "grids", you can use it like this: "python CW3.py --file filename". Please input the right filename(include extension if the file have), and leave a space between "--file" and "filename". Don't worry, the program will tell you if you make a mistake. And it will output the right answer and explanation (if you use --explain) to folder "output". It will interact with other flags.

3. --hint: This flag allows you to input a number, the program will show the grid which have filled the number you inputed. Also this flag can used with the --file and --explain, the --explain will show the number will be filled in where, and with the flag of --file can choose the grid by yourself. For example, when you input --hint 3(leave a space between "--hint" and "number"), it will output the grid after filled 3. 

4. --profile：This flag is using to plot a gragh to compare two different solver's average solving time for different size of grids(i.e. 2*2,2*3,3*3). If this flag running, the other three flags is ignored automaticly. It will not interact with other three flags.
