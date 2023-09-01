name = input("Enter your name: ")
company_name = input("Enter company name: ")

with open("sample.txt", mode="r") as sample:
    cover_letter = sample.read()

cover_letter = cover_letter.replace("[Your Name]", f"{name}")
cover_letter = cover_letter.replace("[Company Name]", f"{company_name}")

with open("sample.txt", mode="w") as sample:
    sample.write(cover_letter)
