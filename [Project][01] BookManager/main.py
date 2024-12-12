import os
import json

# წიგნის კლასი: ინახავს ინფორმაციას ერთი წიგნის შესახებ
class Book:
    def __init__(self, roll_number, title, author, year, id):
        self.roll_number = roll_number  # იდენტიფიკატორი, რომელიც ხელახლა ინომრება
        self.title = title
        self.author = author
        self.year = year
        self.id = id  # უნიკალური და განუმეორებელი იდენტიფიკატორი

    def __str__(self):
        # განსაზღვრავს, თუ როგორ უნდა გამოიტანოს ობიექტი ტექსტური სახით
        return (
            f"\n{'N:':<15} {self.roll_number}, "
            f"\n{'დასახელება:':<15} {self.title}, "
            f"\n{'ავტორი:':<15} {self.author}, "
            f"\n{'წელი:':<15} {self.year}, "
            f"\n{'ID:':<15} {self.id}"
        )


class BookManager:
    def __init__(self, filename='books.json'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.books = []
        self.current_roll_number = 0  # მაქსიმალური Roll Number-ის საცავი
        self.next_unique_id = 1  # უნიკალური ID-ს საცავი
        self.load_from_json()  # ტვირთავს მონაცემებს ფაილიდან

    def add_book(self, book_data):
        self.current_roll_number += 1  # Roll Number-ის გაზრდა
        book = Book(
            roll_number=self.current_roll_number,
            id=self.next_unique_id,
            **book_data,
        )
        self.next_unique_id += 1  # უნიკალური ID-ის გაზრდა
        self.books.append(book)
        self.save_to_json()  # მონაცემების შენახვა

    def list_books(self):  # გამოიტანს ბიბლიოთეკის ფონდში არსებულ წიგნებს
        print("\n" + "=" * 75)
        print(
            f" {'N:':<5} {'დასახელება':<20} {'ავტორი':<20} {'წელი':<15}{'ID':<10} "
        )
        print("=" * 75)
        for book in self.books:
            print(
                f" {book.roll_number:<5} {book.title:<20} {book.author:<20} {book.year:<15} {book.id:<10} "
            )
            print("-" * 75)

    def find_book_by_title(self, title):  # ეძებს წიგნს დასახელებით
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def remove_book_by_roll_number(self, roll_number):  # წაშლის წიგნს Roll Number-ის მიხედვით
        for book in self.books:
            if book.roll_number == roll_number:
                self.books.remove(book)
                self.reassign_roll_numbers(start_roll_number=roll_number)  # Roll Number-ების გადანომრვა
                self.save_to_json()
                return True
        return False

    def reassign_roll_numbers(self, start_roll_number):  # ხელახლა გადაანაწილებს Roll Number-ებს კონკრეტული წერტილიდან
        for book in self.books:
            if book.roll_number >= start_roll_number:
                book.roll_number -= 1
        self.current_roll_number -= 1

    def save_to_json(self):  # ინახავს JSON ფაილში მონაცემებს
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4, ensure_ascii=False)

    def load_from_json(self):  # JSON ფაილიდან მონაცემების ჩატვირთვა
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for book_data in data:
                    self.current_roll_number = max(self.current_roll_number, book_data["roll_number"])
                    self.next_unique_id = max(self.next_unique_id, book_data["id"] + 1)
                    book = Book(**book_data)
                    self.books.append(book)
        except FileNotFoundError:
            print("ფაილი ვერ მოიძებნა. ახალი ფაილი...")

def main():
    book_manager = BookManager()

    while True:
        print("\nმთავარი მენიუ:\n")
        print("1. არსებული წიგნების სია")
        print("2. წიგნის ძებნა დასახელებით")
        print("3. ახალი წიგნის დამატება")
        print("4. წიგნის წაშლა რიგის ნომრის მიხედვით")
        print("5. პროგრამის დახურვა")
        choice = input("\nშეიყვანეთ ციფრი: ")

        if choice == "1":  # არსებული ბიბლიოთეკა
            book_manager.list_books()
        elif choice == "2":  # ძებნა დასახელებით
            while True:
                title = input("წიგნის დასახელება: ")
                if not title:
                    print("მოსაძებნად, გთხოვთ შეიყვანეთ წიგნის დასახელება!")
                    continue
                else:
                    break
            book = book_manager.find_book_by_title(title)
            if book:
                print(book)
            else:
                print("\nმითითებული წიგნი, არ არის ბაზაში.")
        elif choice == "3":  # წიგნის დამატება
            while True:
                title = input("წიგნის დასახელება: ")
                if not title:
                    print("დასახელება აუცილებელი ველია და ის არ უნდა იყოს ცარიელი!")
                else:
                    break

            while True:
                author = input("ავტორი: ")
                if not author:
                    print("თუ ავტორი უცნობია, ჩაწერე - \"უცნობი ავტორი\"")
                else:
                    break
                
            while True:
                try:
                    year = int(input("გამოცემის წელი: "))
                    if year < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("დაფიქსირდა შეცდომა! გთხოვთ შეიყვანოთ წიგნის გამოცემის წელი.")
            book_data = {"title": title, "author": author, "year": year}
            book_manager.add_book(book_data)
            print("\nწიგნი წარმატებით დაემატა!")
        elif choice == "4":  # წაშლა Roll Number-ის მიხედვით
            try:
                roll_number = int(input("შეიყვანეთ Roll Number წასაშლელად: "))
                if book_manager.remove_book_by_roll_number(roll_number):
                    print("\nწიგნი წარმატებით წაიშალა.")
                else:
                    print("\nმითითებული რიგის არ მოიძებნა.")
            except ValueError:
                print("გთხოვთ, შეიყვანოთ ვალიდური რიგის.")
        elif choice == "5":  # პროგრამის დახურვა
            print("პროგრამა დაიხურა.")
            break
        else:
            print("გთხოვთ, შეიყვანოთ კონკრეტული მენიუს შესაბამისი ციფრი.")

if __name__ == "__main__":
    main()
