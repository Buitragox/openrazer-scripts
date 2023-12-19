# Openrazer Scripts

Python scripts to display information about razer peripherals.

## Requirements

- [Openrazer](https://github.com/openrazer/openrazer)
- Python 3

## Usage

You can simply call the scripts in the /scripts folder with python3:

```bash
$ python3 scripts/razer_battery.py
Found 1 Razer devices
-----------------------------------------
Razer DeathAdder V2 Pro (Wireless)
Is charging: False
Battery: 80%s
```

I suggest creating aliases for these scripts for ease of use on your terminal. For example:

```bash
#on your .bash_aliases or .bashrc file
alias rbat='python3 ~/openrazer-scripts/scripts/razer_battery.py'
```
