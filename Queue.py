# Очередь

queue = [] # создание очереди с помощью списка

queue.append(0)     # наполнение стека [0, 1, 3, 5, 15, 1563]
queue.append(1)
queue.append(3)
queue.append(5)
queue.append(15)
queue.append(1563)

print(queue)     # получившаяся очередь

queue.pop(0)  # удаление элемента из очереди

is_empty = len(queue)  # количество элементов очереди
print(is_empty)

print(queue[0]) # отображение первого элемента очереди