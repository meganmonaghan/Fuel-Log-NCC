import collections

pricepg_queue = collections.deque()
gas_queue = collections.deque()

alphabet_list = [100, 200, 300, 400, 500]
for x in [1.0, 2.0, 3.0, 4.0, 5.0]:
	pricepg_queue.append(x)
for x in alphabet_list:
	gas_queue.append(x)

def queues_to_string(price_per_gallon_q, gas_q):
	return_string = ''
	for x in range(len(price_per_gallon_q)):
		add_on = ' '.join([str(price_per_gallon_q.popleft()), str(gas_q.popleft())])
		return_string = return_string + add_on + ', '
	return return_string[:-2]

# print(f'''
# 	price per gallon queue: {pricepg_queue}
# 	length of queue: {len(pricepg_queue)}
# 	gallon queue: {gas_queue}
# 	length of queue: {len(gas_queue)}
# 	''')
print(queues_to_string(pricepg_queue, gas_queue))