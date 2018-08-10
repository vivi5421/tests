import os
import random

folder = "test_chmod/temp" + str(random.randint(1, 100))
print(folder)
os.mkdir(folder)
os.chmod(folder, 0777)