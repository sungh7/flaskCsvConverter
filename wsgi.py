import sys
import os

CURRENT_DIR = os.getcwd()

sys.stdout = sys.stderr
sys.path.insert(0, CURRENT_DIR)

from app import app as applicaiton

if __name__ == "__main__":
    app.run()