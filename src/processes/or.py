import subprocess

rand_number_text = subprocess.check_output(['python', 'randy.py', '20'])
rand_number_text = rand_number_text.strip().decode('ascii')

rand_numbers = [
   n # what items to select
   for n in rand_number_text.split() # what items are we using?
]

# rand_numbers = []
# for n in rand_number_text.split() :
#     rand_numbers.append(n)


max_number_text = subprocess.check_output(['python', 'maxy.py', '5'] + rand_numbers)
max_number_text = max_number_text.strip().decode('ascii')

to_multiply = max_number_text.split(' ')

multi_number_text = subprocess.check_output(['python', 'multi.py'] + to_multiply)
multi_number_text = multi_number_text.strip().decode('ascii')
num = int(multi_number_text)

print("The multiplication of the number is {:,}".format(num))
