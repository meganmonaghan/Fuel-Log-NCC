from queue import Queue

# test list of deliveries
# 200.00 10, 400.00 200, 150.00 32, 500.00 45

price_queue = Queue()
gas_queue = Queue()

user_input = input('''
	Please enter all deliveries and amounts in the
	following format:
	5.00 100
	where each pair is separated by a comma and space.
	Do NOT enter dollar signs or commas.
''')

# not deliveries but queue
# need to return remaining queue at the end of the month to save

def test_queue(user_input):
	deliveries = user_input.split(', ')
	delivery_count = len(deliveries)
	for delivery in deliveries:
		price_gal_split = delivery.split(' ')
		price_per_gallon = float(price_gal_split[0])/float(price_gal_split[1])
		price_queue.put(price_per_gallon)
		gas_queue.put(float(price_gal_split[1]))
	return delivery_count

def display_queue(price_q, gal_q, num):
	for x in range(num):
		print(f'''
		Delivery {x+1}:
		Price per gallon: {price_q.get()}
		Gallons: {gal_q.get()}
	***''')
	return 'All deliveries have been displayed!'

delivery_count = test_queue(user_input)
print(display_queue(price_queue, gas_queue, delivery_count))



# test outline

# a. current price/gal queues

# b. deliveries? Y/N

# c. gallons to start

# d. gallons at the end

# for gas and diesel
# 1. make current price/gal queues - if delivery, add
# 2. calculate gallons used - gal_beginning - (gal_end - deliveries)
# 3. price_used = 0
# 4. gas_used_dict = {}
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