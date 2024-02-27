with open("identities.txt", "r") as i:
    names = [line.strip() for line in i.readlines()]
i.close
identities = [{"name": name.split()[0], "surname": name.split()[1]} for name in names]

emails = [f"{identity['name'].lower()}.{identity['surname'].lower()}@azmiu.edu.az" for identity in identities]

with open("emails.txt", "w") as e:
    for email in emails:
        e.write(email + "\n")

e.close 
print(emails)
