# Стек

stack = [] # создание стека с помощью списка

stack.append(1)      # наполнение стека [1, 3, 5, 15, 1563, 0]
stack.append(3)
stack.append(5)
stack.append(15)
stack.append(1563)
stack.append(0)

print(stack)     # получившийся стек

stack.pop()  # удаление последнего элемента стека

is_empty = len(stack)  # количество элементов стека
print(is_empty)

print(stack[is_empty-1]) # значение верхнего элемента