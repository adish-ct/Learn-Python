"""
"adcd" "acdb" - consider duplicates passwords, 
show only distinct passwords

""" 

passwords = ['abcd', 'adcb', 'asdf', 'bcda', 'jhgf', 'jghf', 'afds']

new_passwords = ["".join(sorted(s)) for s in passwords]

print(new_passwords)

print(set(new_passwords))