# SalesManager
Sale Manager designed for CSGO skins, can be utilized for something else by repurposing the itemnames file.
This is designed to be a tool for managing multiple items stored in different locations, to keep track of them and of your sale statistics.

# Installation

No installation required, download the files, extract them and run SalesApp.exe inside the dist folder.

# Ease of use

The system requires you to use decimal points (".") for float numbers, using a comma (",") may result in errors.

Currently does not support unregistering items from sales, be careful and double check your data when registering sales, if you make a mistake, you may delete
the sale record from total_sales.json

# Updating

To update to a newer version without losing previous sales, overwriting SalesApp.exe with the newer version should be enough.

# Compiling from source

There seems to be an issue where pyinstaller cannot find the babel.numbers import, the complete line for a clean install is:

---

pyinstaller --onefile --hidden-import babel.numbers --noconsole  SalesApp.py

---
