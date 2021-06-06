class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None

def add(list, element):
    new_node = Node()
    new_node.value = element
    
    new_node.nextNode = list.head
    
    list.head = new_node
    return 

def search(list, element):
    if list.head == None:
        return None
    
    current_node = list.head
    while True:
        # se encuentra elemento, se devuelve posicion
        if current_node.value == element:
            return current_node
        # se llega al fin de la lista sin encontrar el elemento, se devuelve None
        if current_node.nextNode == None:
            return None
        current_node = current_node.nextNode

def insert(list, element, index):
    # index out of bounds, return None
    if index > length(list):
        return None

    if list.head == None:
        add(list, element)
        return 0

    new_node = Node()
    new_node.value = element
    
    current_node = list.head
    counter = 0
    prior_node = None
    while True:
        # si se desea insertar en la primer posic. se invoca add.
        if index == 0:
            add(list, element)
            return index
        elif index == counter:
        # se inserta el nuevo nodo enlazando como corresponde.
            prior_node.nextNode = new_node
            prior_node.nextNode.nextNode = current_node
            return index
        counter += 1
        prior_node = current_node
        current_node = current_node.nextNode

def delete(list, element):
    if list.head == None:
        return None

    counter = 0
    current_node = list.head
    prior_node = None
    while True:
        # caso especial cuando el elemento a borrar es el primero.
        if counter == 0:
            if current_node.value == element:
                list.head = current_node.nextNode
                return counter
        else:
            if current_node.value == element:
                # se elimina el vinculo de la lista con el elemento en cuestion
                prior_node.nextNode = current_node.nextNode
                return counter
        counter += 1
        prior_node = current_node
        current_node = current_node.nextNode

        if current_node == None:
            return None

def length(list):
    if list.head == None:
        return 0 

    current_node = list.head
    counter = 0
    
    while True:
        counter += 1
        current_node = current_node.nextNode
        if current_node == None:
            return counter

def access(list, index):
    if index >= length(list):
        return None

    current_node = list.head
    counter = 0
    while True:
        if counter == index:
            return current_node
        counter += 1
        current_node = current_node.nextNode

def update(list, element, replcmnt):
    current_node = list.head
    while current_node:
        if current_node.value == element:
            current_node.value = replcmnt
            return
        current_node = current_node.nextNode

def printlist(L, index = 0):
    
    list_len = length(L)

    if index == 0 or index >= list_len:
        index = list_len
    
    current_node = L.head

    if not current_node:
        print("None")
        return
        
    for i in range(index):
        if current_node.nextNode:
            print(current_node.value,"->", end = " ")
        else: 
            print(current_node.value)
        current_node = current_node.nextNode

def add_toend(l, element):
    if l.head == None:
        add(l, element)
        return

    new_node = Node()
    new_node.value = element
    current_node = l.head 

    while current_node:
        if not current_node.nextNode: 
            current_node.nextNode = new_node
            return
        current_node = current_node.nextNode