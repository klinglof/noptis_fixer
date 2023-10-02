# Install dependencies
DEPENDENCIES="yapf"
sudo apt-get update
sudo apt-get install -y "$DEPENDENCIES"

# Setup installation yapf path for use with pycharm
if [ ! -e "/usr/local/bin/yapf" ]; then
  ln -s "$(command -v yapf)" /usr/local/bin/yapf
fi

# Install pre-commit
pip install pre-commit

# Setup git commit hooks
pre-commit install
