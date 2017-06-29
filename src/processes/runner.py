import subprocess

numbers_raw = subprocess.check_output(['python', './randy.py', "7"]).decode('ascii').strip()
numbers = [n for n in numbers_raw.split(' ')]
print("                      NUMBERS: {}".format(numbers))

max_raw = subprocess.check_output(['python', './maxy.py', '3'] + numbers).decode('ascii').strip()
print("                      MAX: {}".format(max_raw))
max_numbers = [n for n in max_raw.split(' ')]

multi_raw = subprocess.check_output(['python', './multi.py'] + max_numbers).decode('ascii').strip()
print("                      MULTI: {}".format(multi_raw))

print("The final result. The top 3 of {} multipled is {:,}.".format(
    numbers, int(multi_raw)
))
