# WEEK 3. EXERCISES 2. venv, pip & requirements

## Part 1. Create an environment using venv

Create a folder on your computer and open a terminal/command prompt in that folder.

> The command `pwd` prints the current directory to the terminal on unix-like systems. If you
> use Windows CMD you can use `cd` to print the current directory.
>
> To change the current directory to the newly created directory, use 
> 
> `cd path_to_new_directory`

In the new folder, run `python -m venv venv`
This should create a new folder in the current directory called `venv`.

## Part 2. Activate the environment

| Shell      | Command to activate the virtual environment |
|------------|---------------------------------------------|
| bash/zsh   | `$ source <venv>/bin/activate`              |
| csh/tcsh   | `$ source <venv>/bin/activate.csh`          |
| cmd        | `C:\> <venv>\Scripts\activate.bat`          |
| PowerShell | `PS C:\> <venv>\Scripts\activate.ps1`       |

The table shows the commands for activating the newly created environment. If you followed
the instructions under part 1 and use bash/zsh, the command for activating the environment
becomes: `source venv/bin/activate`

If you named your environment something other than `venv`, use that name instead.

## Part 3. Install a package in the environment

After activating the environment, you can install a package in it. If you, for example, want to
install pandas, you can use: `pip install pandas`.

If you now start a Python interpreter, you should be able to import pandas. Try this out using:
`import pandas as pd`

You can add some additional package of your choosing with pip.
* Quit the Python interpreter by typing `quit()` 
* look for some package on pypi.org
* follow the instructions you find for adding it to your environment using pip. Typically `pip install package-name`

## Part 4. Create a requirements.txt

Create a `requirements.txt` file to document your environment:

`pip freeze > requirements.txt`

Take a look at the file `requirements.txt`.
It should list the packages you installed and the necessary dependencies for those
packages.

## Part 5. Deactivate, remove and recreate the environment

Deactivate your environment using `deactivate`

You can now delete the `venv` folder to delete the environment.

To confirm that you can recreate the environment using the `requirements.txt` file:
* Create a new environment `python -m venv venv`
* Activate the environment following the steps in Part 2
* install the requirements using `pip install -r requirements.txt`

You can now check that you can start the Python interpreter, activate the new
environment and import the installed packages. Finally, you can deactivate and delete
the new environment as well.

Read more here:
https://docs.python.org/3/library/venv.html
