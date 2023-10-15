initial_bites = int(input())
queue = []

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        refill_bites = int(command.split()[1])
        initial_bites += refill_bites
    else:
        person_name = command
        bites_wanted = int(input())

        if bites_wanted <= initial_bites:
            print(f"{person_name} take bites")
            initial_bites -= bites_wanted
        else:
            print(f"{person_name} must wait")

print(f"{initial_bites} bites left")
