import collections
from csv_test import find_gallons_gas, find_gallons_diesel

pricepg_queue = collections.deque()
gas_queue = collections.deque()

gas_type = input('''
	Please enter the type of fuel you are working
	with (either 'gas' or 'diesel').
''').lower()

user_input = input('''
	Please enter current inventory by price per gallon
	and amounts in the following format:
	5.00 100
	where each pair is separated by a comma and space.
	Do NOT enter dollar signs or commas in your numbers.
''')

# add current queue
def test_queue(user_input):
	deliveries = user_input.split(', ')
	delivery_count = len(deliveries)
	for delivery in deliveries:
		price_gal_split = delivery.split(' ')
		pricepg_queue.append(float(price_gal_split[0]))
		gas_queue.append(float(price_gal_split[1]))
	return delivery_count

test_queue(user_input)

# add delivery, if applicable
delivery_input = input('''
	Did you receive any deliveries this month?
	Enter Y/N
''')

delivery_gallons = 0
if delivery_input.lower() == 'y':
	delivery_input = input('''
	Please enter the TOTAL delivery price and amount
	in the following format:
	1500.00 100
	with NO dollar signs or commas.
''')
	d_components = delivery_input.split(' ')
	delivery_gallons = float(d_components[1])
	price_per_gallon = float(d_components[0])/float(d_components[1])
	pricepg_queue.append(price_per_gallon)
	gas_queue.append(delivery_gallons)

# gallons start/end
gallons_start_m = input(f'''
***
	Please enter the measurement of {gas_type} you STARTED
	with this month in the following format:
	14-1/2"
	Don't forget the " sign at the end of the number!
''')

gallons_end_m = input(f'''
***
	Please enter the measurement of {gas_type} you ENDED with
	this month in the following format:
	32-1/2"
	Don't forget the " sign at the end of the number!
''')

if gas_type == 'gas':
	gallons_start = float(find_gallons_gas(gallons_start_m))
	gallons_end = float(find_gallons_gas(gallons_end_m))
elif gas_type == 'diesel':
	gallons_start = float(find_gallons_diesel(gallons_start_m))
	gallons_end = float(find_gallons_diesel(gallons_end_m))

gallons_used = float(gallons_start - (gallons_end - delivery_gallons))
price_used = 0
gas_used_dict = {}

while gallons_used:
	gq = gas_queue.popleft()
	if gallons_used >= gq:
		pq = pricepg_queue.popleft()
		price_used += gq * pq
		gallons_used -= gq
		gas_used_dict['$' + str(pq)] = gq
	# this needs to be fixed, this else block
	else:
		pq = pricepg_queue.popleft()
		price_used += gallons_used * pq
		if pq in gas_used_dict.keys():
			gas_used_dict['$' + str(pq)] = gas_used_dict['$' + str(pq)] + gallons_used
		else:
			gas_used_dict['$' + str(pq)] = gallons_used
		pricepg_queue.appendleft(pq)
		gas_queue.appendleft(gq - gallons_used)
		break

# reiterating gallons_used value for return
gallons_used = float(gallons_start - (gallons_end - delivery_gallons))

# test display
print(f'''
***
	\033[1;3m{gas_type} report\033[0m

	gallons at beginning of month: {gallons_start} gal
	gallons at end of month: {gallons_end} gal
	delivery gallons: {delivery_gallons} gal

	total gallons used: \033[1m{gallons_used}\033[0m gal
	price of {gas_type} used: \033[1m${price_used}\033[0m
	{gas_type} use by price per gallons: \033[1m{gas_used_dict}\033[0m
***
	''')

# display queue for next month
def queues_to_string(price_per_gallon_q, gas_q):
	return_string = ''
	for x in range(len(price_per_gallon_q)):
		add_on = ' '.join([str(price_per_gallon_q.popleft()), str(gas_q.popleft())])
		return_string = return_string + add_on + ', '
	return return_string[:-2]

print(f'''
	Please keep this list for your records! This will be
	next month's input for {gas_type} inventory.
	''')
print(queues_to_string(pricepg_queue, gas_queue))
