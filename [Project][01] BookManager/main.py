import os
import json

# წიგნის კლასი: ინახავს ინფორმაციას ერთი წიგნის შესახებ
class Book:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # განსაზღვრავს, თუ როგორ უნდა გამოიტანოს ობიექტი ტექსტური სახით
        return f"\n{'ID:':<15} {self.id}, \n{'დასახელება:':<15} {self.title}, \n{'ავტორი:':<15} {self.author}, \n{'გამოცემის წელი:':<15} {self.year}"


class BookManager:
    def __init__(self, filename='books.json'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.books = []
        self.current_id = 0  # მაქსიმალური ID-ს საცავი
        self.load_from_json()  # ტვირთავს მონაცემებს ფაილიდან

    def add_book(self, book_data):
        self.current_id += 1  # ID-ის გაზრდა
        book = Book(id=self.current_id, **book_data)
        self.books.append(book)
        self.reassign_ids()  # ID-ების ხელახლა გადანომრვა
        self.save_to_json()  # მონაცემების შენახვა

    def list_books(self):  # გამოიტანს ბიბლიოთეკის ფონდში არსებულ წიგნებს
        print("\n" + "=" * 65)
        print(f" {'ID':<5} {'დასახელება':<20} {'ავტორი':<20} {'გამოცემის წელი':<15}")
        print("=" * 65)
        for book in self.books:
            print(f" {book.id:<5} {book.title:<20} {book.author:<20} {book.year:<15}")
            print("-" * 65)

    def find_book_by_title(self, title):  # ეძებს წიგნს დასახელებით
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def remove_book_by_id(self, book_id):  # წაშლის წიგნს ID-ის მიხედვით
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.reassign_ids()  # ID-ების ხელახლა გადანომრვა
                self.save_to_json()
                return True
        return False
    
    def reassign_ids(self):  # ხელახლა გადაანაწილებს ID-ებს
        for index, book in enumerate(self.books, start=1):
            book.id = index

    def save_to_json(self):  # ინახავს JSON ფაილში მონაცემებს
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4, ensure_ascii=False)

    def load_from_json(self):  # JSON ფაილიდან მონაცემების ჩატვირთვა
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for book_data in data:
                    if 'id' not in book_data:  # თუ ID არ არის, შექმენით
                        self.current_id += 1
                        book_data['id'] = self.current_id
                    else:
                        self.current_id = max(self.current_id, book_data['id'])
                    book = Book(**book_data)
                    self.books.append(book)
        except FileNotFoundError:
            print("ფაილი ვერ მოიძებნა. იქმნება ახალი ფაილი...")

def main():
    book_manager = BookManager()

    while True:
        print("\nმთავარი მენიუ:\n")
        print("1. არსებული წიგნების სია")
        print("2. წიგნის ძებნა დასახელებით")
        print("3. ახალი წიგნის დამატება")
        print("4. წიგნის წაშლა ID-ის მიხედვით")
        print("5. პროგრამის დახურვა")
        choice = input("\nშეიყვანეთ ციფრი: ")

        if choice == "1":
            book_manager.list_books()
        elif choice == "2":
            title = input("შეიყვანეთ დასახელება: ")
            book = book_manager.find_book_by_title(title)
            if book:
                print(book)
            else:
                print("\nმითითებული წიგნი, არ არის ბაზაში.")
        elif choice == "3":
            while True:
                title = input("წიგნის დასახელება: ")
                if not title:
                    print("დასახელება აუცილებელი ველია და ის არ უნდა იყოს ცარიელი!")
                    continue
                else:
                    break
            while True:    
                author = input("ავტორი: ")
                if not author:
                    print("თუ ავტორი უცნობია, ჩაწერე - \"უცნობი ავტორი\"")
                    continue
                else:
                    break
            while True:
                try:
                    year = int(input("გამოცემის წელი: "))
                    if year < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("დაფიქსირდა შეცდობა! გთხოვთ შეიყვანოთ წიგნის გამოცემის წელი.")
            book_data = {"title": title, "author": author, "year": year}
            book_manager.add_book(book_data)
            print("\nწიგნი წარმატებით დაემატა!")

        elif choice == "4":
            try:
                book_id = int(input("შეიყვანეთ წიგნის ID წასაშლელად: "))
                if book_manager.remove_book_by_id(book_id):
                    print("\nწიგნი წარმატებით წაიშალა.")
                else:
                    print("\nმითითებული ID არ მოიძებნა.")
            except ValueError:
                print("გთხოვთ, შეიყვანოთ ვალიდური ID.")

        elif choice == "5":
            print("პროგრამა დაიხურა.")
            break
        else:
            print("გთხოვთ შეიყვანოთ კონკრეტული მენიუს შესაბამისი ციფრი.")

if __name__ == "__main__":
    main()
