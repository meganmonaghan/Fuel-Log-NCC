from queue import Queue

# test list of deliveries
# 20.00 10, 4.00 200, 5.25 32, 10.00 500

price_queue = Queue()
gas_queue = Queue()

user_input = input('''
	Please enter all deliveries and amounts in the
	following format:
	5.00 100
	where each pair is separated by a comma and space.
	Do NOT enter dollar signs or commas.
''')

def test_queue(user_input):
	deliveries = user_input.split(', ')
	delivery_count = len(deliveries)
	for delivery in deliveries:
		price_gal_split = delivery.split(' ')
		price_queue.put(float(price_gal_split[0]))
		gas_queue.put(int(price_gal_split[1]))
	return delivery_count

def display_queue(price_q, gal_q, num):
	for x in range(num):
		print(f'''
		Delivery {x+1}:
		Price: {price_q.get()}
		Gallons: {gal_q.get()}
	***''')
	return 'All deliveries have been displayed!'

delivery_count = test_queue(user_input)
print(display_queue(price_queue, gas_queue, delivery_count))