from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Rigth')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disk = int(input('\nHow many disks do you want to play with?\n'))
print(num_disk)

while num_disk <= 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disk, 0, -1):
  left_stack.push(disk)

num_optimal_moves = pow(2, num_disk) - 1
print("\nThe fastest you can solve this game is in " + str(num_optimal_moves) + " moves")