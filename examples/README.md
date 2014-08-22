How to run example scripts
==========================

There are two ways to run examples without installing the whole package:

1. You could add path to project to the `PYTHONPATH` environment variable. In Linux OS you could use `realpath` to retrieve path of the project:
   
        export PYTHONPATH=$PYTHONPATH:`realpath ../..`
       
    (assuming, the project is two levels upper than current directory)
    
    After that you could simply run scripts using your python interpreter:
    
        python main.py
        
2. You could copy script files to the project directory (i.e. _api_ folder and the script file should be places at the same directory.