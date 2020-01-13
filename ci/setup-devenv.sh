#!/bin/bash
# Set up development env.

echo Start: set up Python environment.

devenv=assetlogger

# Packages for development
pkgs=(django flake8 ipython)

# Create virtual environment. python3-venv is required.
# Use _venv/. Spacemacs cannot even handle the presence of .venv/.
echo Creating virtual environment...
python3 -m venv --clear ~/_venv/assetlogger
. ~/_venv/assetlogger/bin/activate

# Installing wheel first helps install certain packages (e.g., backcall)
echo Installing wheel by pip first...
pip3 install wheel

# Install support packages
echo Installing required pip packages...
if [ ${#pkgs[@]} -ne 0 ]; then
    pip3 install ${pkgs[@]}
fi

echo End: set up Python environment.
