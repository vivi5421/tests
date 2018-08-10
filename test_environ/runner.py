import os
import subprocess

os.environ["TOTO"] = "1"
subprocess.call(os.path.dirname(__file__) + "/runner2.sh", shell=True)

try:
    print("runner TOTO="+os.environ["TOTO"])
except:
    print("issue in runner TOTO")

try:
    print("runner TOTO2="+os.environ["TOTO2"])
except:
    print("issue in runner TOTO2")

try:
    print("runner TOTO3="+os.environ["TOTO3"])
except:
    print("issue in runner TOTO3")