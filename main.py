def stats():
    print("Statistics Calculator")


    def select_operation():
        while True:
            try:
                operation = int(input("Select an operation: "))
                if operation == 1:
                    print("Basic Statistics (Mean, Median, Mode )")
            
            except ValueError:
                print("Invalid input. Please enter a number.")