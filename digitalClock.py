
from datetime import datetime
import os

print("\033[1;32m")
while True:
  os.system("clear")
  current_time = datetime.now().strftime("%H:%M:%S")
  print(current_time)

#Not Efficint Don't Run It