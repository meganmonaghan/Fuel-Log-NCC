import collections

pricepg_queue = collections.deque()
full_price_queue = collections.deque()
gas_queue = collections.deque()

user_input = input('''
	Please enter current deliveries and amounts in the
	following format:
	5.00 100
	where each pair is separated by a comma and space.
	Do NOT enter dollar signs or commas.
''')

# add current queue
def test_queue(user_input):
	deliveries = user_input.split(', ')
	delivery_count = len(deliveries)
	for delivery in deliveries:
		price_gal_split = delivery.split(' ')
		price_per_gallon = float(price_gal_split[0])/float(price_gal_split[1])
		pricepg_queue.append(price_per_gallon)
		full_price_queue.append(float(price_gal_split[0]))
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
	Please enter the delivery price and amount in
	the following format:
	5.00 100
	with NO dollar signs or commas.
''')
	d_components = delivery_input.split(' ')
	delivery_gallons = float(d_components[1])
	price_per_gallon = float(d_components[0])/float(d_components[1])
	pricepg_queue.append(price_per_gallon)
	full_price_queue.append(d_components[0])
	gas_queue.append(delivery_gallons)

# gallons start/end
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

gallons_used = float(gallons_start - (gallons_end - delivery_gallons))
price_used = 0
gas_used_dict = {}

# calculating gallons used/price used etc.
while gallons_used:
	gq = gas_queue.popleft()
	if gallons_used >= gq:
		pq = pricepg_queue.popleft()
		full_price_queue.popleft()
		price_used += gq * pq
		gallons_used -= gq
		gas_used_dict[pq] = gq
	# this needs to be fixed, this else block
	else:
		pq = pricepg_queue.popleft()
		price_used += gallons_used * pq
		gas_used_dict[pq] = gallons_used
		pricepg_queue.appendleft(pq)
		gas_queue.appendleft(gq - gallons_used)

# reiterating gallons_used value for return
gallons_used = float(gallons_start - (gallons_end - delivery_gallons))

# test display
print(f'''
	gallons at beginning of month: {gallons_start}
	gallons at end of month: {gallons_end}
	delivery gallons: {delivery_gallons}
	total gallons used: {gallons_used}
	price of gas used: {price_used}
	gas use by price per gallons: {gas_used_dict}
	***
	''')

print(f'''
	current price queue: {full_price_queue}
	current gallon queue: {gas_queue}
	please keep these lists for your records!
	''')

# 2000.00 500, 2250.00 500
# delivery - 1750.00 500
# gallons start - 1250
# gallons end - 750
# gallons used - 1000
