import random
def egg_will_break(n):
	"""
	This function will return the status of the egg after dropping it
	"""
	if n >= egg_breaks_on_level:
		return True
	return False


def get_threshold(data):
	n_start, n_end, _, __ = data.values()
	if n_start >= n_end:
		return n_start
	n_middle = int((n_end + n_start) / 2)
	data['tries'] += 1
	if egg_will_break(n_middle):
		data['waisted'] += 1
		data['n_end'] = n_middle - 1 
		return get_threshold(data)
	if egg_will_break(n_middle + 1):
		data['waisted'] += 1
		return n_middle
	data['n_start'] = n_middle + 1
	return get_threshold(data)

if __name__ == '__main__':
	for i in range(70):
		n_floors = 40
		egg_breaks_on_level = random.randint(1,n_floors)
		data = {'n_start': 0, 'n_end': n_floors, 'tries': 0, 'waisted': 0}
		n = get_threshold(data)
		print("Total number of floors:\t%s\nEgg breaks on level:\t%s" %
		(n_floors, egg_breaks_on_level))
		print("Number of tries:\t%s\nNumber of eggs waisted:\t%s\nThreshold:\t%s\n" %
		(data['tries'], data['waisted'], n))
		print("===================")
