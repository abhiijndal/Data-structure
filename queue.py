#####################################################################################################################################
queue=[]

#enter the element in a queue



queue.append(56)
queue.append(100)
queue.append(50)
print('*initialise element:\n',queue)

#to dequeue the element from the queue
print('*dequeue the element from the queue:')
print(queue.pop(0))
print(queue.pop(1))


print('*after removing the element:\n'+str(queue))

print(queue.append(34))
print('*after adding the new element in a queue:\n',queue)






##############################################################################################################################################









from queue import Queue


q=Queue(maxsize=5)

print(q.qsize())
#adding element in a queue....>>>>>
#q.put('122')
q.put('788')
q.put('676')
q.put('787')
q.put('90')


#checking that queue is full or not if full than true otherwise false....>>>>>>


print('->the queue is full:',q.full())



#removing the element element from the queue.......>>>>>>.
print('->element dequeue from the queue:')

print(q.get())
print(q.get())
print(q.get())

print('->the queue is empty:\n',q.empty())
print('->full:\n',q.full())

print(q.put(100))
print(q.put(898))
print(q.put(78))
print(q.put(8080))
#print(q.put(100))
print('->empty:\n',q.empty())
print('->dequeue_element:\n',q.get())

print('->full:\n',q.full())
