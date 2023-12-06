class To_do_list:
    def __init__(self, lst=None):
        self.lst = lst if lst is not None else []
        print("")

    def view(self):
        print("Your To-Do List")
        for i in range(len(self.lst)):
            print(self.lst[i])


    def add(self, work):
        self.lst.append(work)
        print(f"Successfully Added: {work}")
        print('')

    def remove(self, work):
        if work in self.lst:
            self.lst.remove(work)
            print(f'{work} removed from list')
        else:
            print("The given work is not in your list")
        print("")


def main():
    print("To-Do List")
    initial_work = input("Enter Initial work to list:")

    todo = To_do_list([initial_work])

    while True:
        print("_______________________")
        print("")
        print("1. View list")
        print("2. Add")
        print("3. Remove")
        print("4. Exit")
        print("_______________________")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            todo.view()
        elif choice == 2:
            work = input("Enter work to add:")
            todo.add(work)
        elif choice == 3:
            work = input("Enter work to remove:")
            todo.remove(work)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
