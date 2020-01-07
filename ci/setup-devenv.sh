#!/bin/bash
# Set up development env.

echo Start: set up Python environment.

devenv=assetlogger

# Packages for development
pkgs=(django flake8 ipython)

# Create virtual environment. python3-venv is required.
# Use _venv/. Spacemacs cannot even handle the presence of .venv/.
python3 -m venv --clear ~/_venv/assetlogger
. ~/_venv/assetlogger/bin/activate

# Install support packages
if [ ${#pkgs[@]} -ne 0 ]; then
    pip3 install ${pkgs[@]}
fi

echo End: set up Python environment.
