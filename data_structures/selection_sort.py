# working - selection sort (own idea) might be possible to optimize
numbers = [10, 7, 5, 1, 2, 3, 0]


min_index = 0
loop_count = 0

while True:
	swap_needed = False
	min = numbers[loop_count]
	for i in range(loop_count+1, len(numbers)):
		if numbers[i] < min:
			min = numbers[i]
			min_index = i
			swap_needed = True
	if swap_needed:
		swapper = numbers[loop_count]
		numbers[loop_count] = min
		numbers[min_index] = swapper
	if (loop_count>=len(numbers)-1):
		break
	else:
		loop_count+=1

print(numbers)