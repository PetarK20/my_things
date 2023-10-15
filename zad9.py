queue = []

while True:
    command = input()
    if command == "END":
        break
    elif command == "PAID":
        for customer in queue:
            print(customer)
        queue = []
    else:
        queue.append(command)

print(f"{len(queue)} people remaining.")
