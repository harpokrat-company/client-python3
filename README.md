# Command line interface - python3

The command line interface of Harpokrat allows you to manage your HPK passwords directly in your terminal.

## Prerequisites
You will need to have the HCL library installed on your computer. If not, you can find a link to it at #TODO Add link#

## Installation
The `requirements.txt` contains all the necessary packages to the proper functioning of cli.
    
    # pip3 install -r requirements.txt
## Usage
    # ./cli.py [args] username
The cli provides a `--help` argument in order to explore every usage.
However, you will find below useful argument in order to use the CLI.
- `--shell` activates the shell mode (you can prompt multiple commands)
- `--list` or `-l` allows you to list all your passwords 
- `--add` or `-a` allows you to add a new password
- `--delete` or `-d` allows you to delete a password 
- `--modify` or `-m` allows you to modify any field of a password
- `--info` or `-i` give information about your account 


## Way of improvement :steam_locomotive:
- Add a way to pipe the password (eg. `./cli.py --pipe username | ./any_kind_of_services`)

## FAQ

#### Is it possible to create on HPK account using the CLI ?
No, it is not. However you can create an account using our web platform that is available at https://www.harpokrat.com/

---
#### Is it possible to contribute or to propose ideas to improve the project ?
Yes sure ! You can freely contribute to the project and if you any idea you want to share with us, do not hesitate to contact us :rocket:.

---
#### Other problems
Please feel free to contact@haprokrat.com or to write an issue :smiley:.