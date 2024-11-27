# გამოიცანი შემთხვევითი რიცხვი, შენ მიერ განსაზღვრულ დიაპაზონში

from random import randint # შემოგვაქვს random მოდულის randint ფუნქცია;
print("="*60)
print("\nგამარჯობა, \n\n ეს არის თამაში, სადაც შენ უნდა გამოიცნო ჩაფიქრებული რიცხვი. \nშენ, თავად უნდა გადაწყვიტო, თუ რა დიაპაზონში ჩავიფირო ის.\n")
print("(ერთი პირობა მაქვს მხოლოდ - დიაპაზონი უნდა იყოს 2-ზე მაღალი!}\n")
# მომხმარებლისგან ზედა ზღვრის მიღება და შესაძლო შეცდომების დამუშავება
while True:
    try:
        n = int(input("შეიყვანე ზედა ზღვარი: "))
        if not n or n < 3:  # თუ რიცხვი 2-ზე ნალკებია, ხდება შეცდომის გენერირება
            raise ValueError
        break
    except ValueError:
        print("\nდაფიქსირდა შეცდობა! \n\nშეიყვანეთ 2-ზე მაღალი დადებითი მთელი რიცხვი.\n")


print(f"\nშენი დიაპაზონია 1 - {n}")

# ცდების რაოდენობის განსაზღვრა დიაპაზონის მიხედვით

trying = 0
if 10 < n <= 100:
    trying = 7
elif 2 < n <= 10:
    trying = 3
elif 100 < n <= 1000:
    trying = 10
else:
    print("\nდაფიქსირდა მაღალი რიცხვი! \n\nგაითვალისწინე, ყველაზე ოპტიმალური არჩევანი არის 0-დან 100-მდე.")
    trying = 12


# შემთხვევითი რიცხვის გენერირება და თამაშის დაწყება
secret_number = randint(1, n)
i=trying

print(f"\nგამოიცანი ჩაფიქრებული რიცხვი 1-დან {n}-მდე")
print()

# მთავარი ციკლი, სადაც ხდება რიცხვების შეყვანა/შემოწმება/დამოწმება
while i > 0:
    if i == 1: # თუ მომხმარებელს დარჩა ბოლო შანსი
        guess = int(eval(input(f"\nშენ გაქვს ბოლო {i} ცდა, გამოიცანი რიცხვი: ")))
        if guess == secret_number: # თუ მომხმარებელმა გამოიცნო
            print(f"გილოცავ! შენ შეძელი ეს ბოლო ცდაზე! ჩაფიქრებული რიცხვია - {guess}")
            break
        else:
            print("\nშენ ისევ შეცდი და ცდაც აღარ დაგრჩა!")
            break
    else:
        guess = int(eval(input(f"\nშენ გაქვს {i} ცდა, გამოიცანი რიცხვი: ")))

        if guess == secret_number: # თუ მომხმარებელმა გამოიცნო
            print(f"გილოცავ! სწორად გამოიცანი. ეს არის {guess}")
            break
        elif guess > secret_number:
            print("ნაკლებია ჩანაფიქრი, კიდევ სცადე! ;)")
        else:
            print("ჩანაფიქრი უფრო მაღალია, სცადე უფრო დიდი რიცხვი!")
        i -= 1

print("\nთამაში დასრულებულია!")       