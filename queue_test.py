import collections

# test list of deliveries
# 200.00 10, 400.00 200, 150.00 32, 500.00 45

pricepg_queue = collections.deque()
gas_queue = collections.deque()

user_input = input('''
	Please enter current inventory by price per gallon
	and amounts in the following format:
	5.00 100
	where each pair is separated by a comma and space.
	Do NOT enter dollar signs or commas in your numbers.
''')

# not deliveries but queue
# need to return remaining queue at the end of the month to save

def test_queue(user_input):
	deliveries = user_input.split(', ')
	delivery_count = len(deliveries)
	for delivery in deliveries:
		price_gal_split = delivery.split(' ')
		pricepg_queue.append(float(price_gal_split[0]))
		gas_queue.append(float(price_gal_split[1]))
	return delivery_count

test_queue(user_input)

def display_queue(price_q, gal_q, num):
	for x in range(num):
		print(f'''
		Delivery {x+1}:
		Price per gallon: {pricepg_q.popleft()}
		Gallons: {gal_q.popleft()}
	***''')
	return 'All deliveries have been displayed!'

# print(display_queue(price_queue, gas_queue, delivery_count))

delivery_input = input('''
	Did you receive any deliveries this month?
	Enter Y/N
''')

delivery_gallons = 0
if delivery_input.lower() == 'y':
	delivery_input = input('''
	Please enter the delivery price and amount in
	the following format:
	5.00 100
	with NO dollar signs or commas.
''')
	d_components = delivery_input.split(' ')
	delivery_gallons = float(d_components[1])
	price_per_gallon = float(d_components[0])/float(d_components[1])
	pricepg_queue.append(price_per_gallon)
	gas_queue.append(delivery_gallons)

gallons_start = float(input('''
***
	Please enter the number of gallons you STARTED
	with this month. Enter with no commas or spaces.
'''))

gallons_end = float(input('''
***
	Please end the number of gallons you had at the
	END of this month. Enter with no commas or spaces.
'''))

# print(f'''
# 	full price queue: {full_price_queue}
# 	price per gallon queue: {pricepg_queue}
# 	gallons queue: {gas_queue}''')

gallons_used = float(gallons_start - (gallons_end - delivery_gallons))
price_used = 0
gas_used_dict = {}

while gallons_used:
	gq = gas_queue.popleft()
	if gallons_used >= gq:
		pq = pricepg_queue.popleft()
		price_used += gq * pq
		gallons_used -= gq
		gas_used_dict[pq] = gq
	# this needs to be fixed, this else block
	else:
		pq = pricepg_queue.popleft()
		price_used += gallons_used * pq
		if pq in gas_used_dict.keys():
			gas_used_dict[pq] = gas_used_dict[pq] + gallons_used
		else:
			gas_used_dict[pq] = gallons_used
		pricepg_queue.appendleft(pq)
		gas_queue.appendleft(gq - gallons_used)
		break

gallons_used = float(gallons_start - (gallons_end - delivery_gallons))

print(f'''
	gallons at beginning of month: {gallons_start}
	gallons at end of month: {gallons_end}
	delivery gallons: {delivery_gallons}
	total gallons used: {gallons_used}
	price of gas used: {price_used}
	gas use by price per gallons: {gas_used_dict}
	''')

def queues_to_string(price_per_gallon_q, gas_q):
	return_string = ''
	for x in range(len(price_per_gallon_q)):
		add_on = ' '.join([str(price_per_gallon_q.popleft()), str(gas_q.popleft())])
		return_string = return_string + add_on + ', '
	return return_string[:-2]

print('''Please keep this list for your records! This will be
	next month's input for inventory.''')
print(queues_to_string(pricepg_queue, gas_queue))

# 4.00 500, 4.5 500
# delivery - 1750.00 500
# gallons start - 1250
# gallons end - 750
# gallons used - 1000

# test outline

# a. current price/gal queues

# b. deliveries? Y/N

# c. gallons to start

# d. gallons at the end

# for gas and diesel
# 1. DONE - make current price/gal queues - if delivery, add
# 2. DONE calculate gallons used - gal_beginning - (gal_end - deliveries)
# 3. DONE: price_used = 0
# 4. DONE: gas_used_dict = {}
# 5. while gallons_used:
# 	if gallons_used >= gq1:
# 		price_used += gq1 * pq1
# 		gallons_used -= gq1
# 		remove gq1
# 		remove pq1
# 		gas_used_dict[pq1] = gq1
# 	else:
# 		price_used += gallons_used * pq1
# 		gq1 = gq1 - gallons_used
# 		gas_used_dict[pq1] = gallons_used
# 6. return gased_used_dict
# 7. return price_used
# 8. if delivery:
# 	return delivery
# 9. return gal_beginning, gal_end
# 10. return gallons_used total