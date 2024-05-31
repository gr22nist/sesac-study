import random

# def __init__(self):
#     self.lname = []
#     self.fname = []

    # with open('lnames.txt', 'r', encoding='utf-8') as file:
    #     self.lname = file.read().split(',')

    # with open('fnames.txt', 'r', encoding='utf-8') as file:
    #     self.fname = file.read().split(',')

    # # return self.lname, self.fname

def gnrt_name():
    names = []
    
    with open('../fnames.txt', 'r', encoding='utf-8') as file:
        names = file.read().split(',')
        
    return random.choice(names)


a = gnrt_name()
print(a)