# Define the booklist
booklist = {
            1: "Getting to Yes by Fisher & Ury",
            2: "Marketing Management by Kotler & Keller",
            3: "The 12 Week MBA by Billhardt & Kracklauer",
            4: "Poor Economics by Banerjee & Duflo",
            5: "The Vegetarian by Han Kang",
            6: "The Tale of Two Cities by Charles Dickens"
           }

# Knowing user's intention
wish = input("Do you want to take a book? (Yes/No): ").lower()

# Loop to borrow books 
while wish == "yes":
    choice = input("Enter the BookID: ")
    if choice.isdigit():  # Check if input is a positive integer
        choice = int(choice)  # Convert to integer only if valid
        if choice in booklist:
            print(f"Wow! You want to take '{booklist[choice]}'. It is a great book. Please return it within 3 weeks.")
        else:
            print(f"Your desired book {choice} is currently not available. Please choose a book from the Booklist.")
    else:
        print("Invalid input. Please enter a number for the BookID.")
    
    # Ask if user wants to continue
    wish = input("Do you want to take another book? (Yes/No): ").lower()

# Thanking visitor
print("Thank you for visiting my library. Hope you enjoyed it!")