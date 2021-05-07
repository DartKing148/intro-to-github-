import random
people = int(input("Enter the number of friends joining (including you):\n"))
friends = {}

if people <= 0:
    print("\nNo one is joining for the party")
    exit()
print("\nEnter the name of every friend (including you), each on a new line:")

for i in range(people):
    friends[input()] = 0
bill = int(input("\nEnter the total bill value:\n"))
lucky_input = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if lucky_input == "Yes":
    lucky = random.choice(list(friends.keys()))
    print(f"\n{lucky} is the lucky one!\n")
    friends = dict.fromkeys(friends, round(bill / (people - 1), 2))
    friends[lucky] = 0
    print(friends)
else:
    friends = dict.fromkeys(friends, round(bill / people, 2))
    print("\nNo one is going to be lucky\n")
    print(friends)
