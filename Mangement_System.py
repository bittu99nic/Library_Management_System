import pickle

book_list = ["Alice in wonderland", "Alchemist", "The Secrete of Nagas", "Around the world 80 days",
             "One night in the call centre", "Harry Potter Series"
                                             "Witcher", "A song of Ice and Fire"]
file = "Book_list.pkl"
file_obj = open(file, "wb")
pickle.dump(book_list, file_obj)


class Library:
    def add_book(self):
        user_book = input("ENTER THE NAME OF THE BOOK YOU WANT TO ADD: ")
        book_list.append(user_book)
        print("NEW BOOK LIST\n")
        print(book_list)

    def lend_book(self, index_number):
        book_list.pop(index_number)
        print("NEW BOOK LIST\n")
        print(book_list)


lib_obj = Library()
user_ch = 1
print("WELCOME TO SAYANJIN LIBRARY")
print("CHOOSE THE FOLLOWING")
while user_ch == 1:
    print("PRESS L TO SEE THE FULL LIST OF THE BOOK ")
    print("PRESS A TO ADD BOOK ")
    print("PRESS R TO RENT A BOOK ")
    user = input("ENTER YOUR CHOICE ")
    if user == 'L':
        print("BOOK LIST \n")
        file_obj = open(file, "rb")
        pickle.load(file_obj)
        print(book_list)
    elif user == 'A':
        lib_obj.add_book()
    elif user == 'R':
        for i in range(len(book_list)):
            print([i, book_list[i]])
        index_ch = int(input("ENTER THE INDEX NUMBER OF BOOK YOU WANT TO ISSUE "))
        lib_obj.lend_book(index_ch)
    else:
        print("WRONG INPUT")
    user_ch = input("DO YOU WANT TO EXIT 0:YES/ 1: NO ")


file_obj.close()
print("THANK YOU VISIT AGAIN")

