import time
import sys
import colorama

colorama.init()

print("Line 1")
time.sleep(1)
print("Line 2")
time.sleep(1)
print("Line 3 (no eol)", end="")
sys.stdout.flush()
time.sleep(1)
print("\rLine 3 the sequel")
time.sleep(1)
print("\033[ALine 3 the second sequel")
time.sleep(1)
print("\033[A\033[A\033[ALine 1 the sequel")
time.sleep(1)
print()  # skip two lines so that lines 2 and 3 don't get overwritten by the next console prompt
print()