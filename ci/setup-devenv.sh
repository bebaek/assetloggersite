#!/bin/bash
# Set up development env.

echo Start: set up Python environment.

devenv=assetlogger

# Packages for development
pkgs=(django flake8 ipython)

# Create env. python3-venv is required.
python3 -m venv --clear ~/.venv/assetlogger
. ~/.venv/assetlogger/bin/activate

# Install support packages
if [ ${#pkgs[@]} -ne 0 ]; then
    pip3 install ${pkgs[@]}
fi

echo End: set up Python environment.
