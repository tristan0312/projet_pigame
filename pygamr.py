lst = ['Emmy', 'Ahmed', 'Antoine', 'Emma', 'Louan', 'Louka', 'Louan', 'Elouo', 'Candice', 'Tristan', 'Alissa', 'Louka', 'Louka', 'Emma', 'Alissa', 'Antoine', 'Elouo', 'Louan', 'Mathias', 'Candice', 'Antoine', 'Tristan', 'Louka', 'Emma', 'Tristan', 'Mathias', 'Louan', 'Vincent', 'Vincent', 'Ahmed', 'Louka', 'Elouo', 'Ahmed', 'Elouo', 'Candice', 'Louka', 'Mathias', 'Mathias', 'Emmy', 'Candice', 'Tristan', 'Antoine', 'Mathias', 'Ahmed', 'Candice', 'Louka', 'Alissa', 'Vincent', 'Elouo', 'Vincent', 'Antoine', 'Elouo', 'Emmy', 'Hugo', 'Vincent', 'Louan', 'Emmy', 'Emma', 'Vincent', 'Louan', 'Elouo', 'Emmy', 'Emmy', 'Emma', 'Mathias', 'Elouo', 'Louka', 'Hugo', 'Emma', 'Vincent', 'Candice', 'Ahmed', 'Hugo', 'Emma', 'Candice', 'Louan', 'Louka', 'Candice', 'Emma', 'Hugo', 'Mathias', 'Tristan', 'Mathias', 'Tristan', 'Antoine', 'Antoine', 'Hugo', 'Louka', 'Mathias', 'Hugo', 'Alissa', 'Elouo', 'Louka', 'Louka', 'Alissa', 'Vincent', 'Ahmed', 'Emma', 'Hugo', 'Mathias', 'Hugo', 'Mathias', 'Antoine', 'Ahmed', 'Antoine', 'Antoine', 'Vincent', 'Ahmed', 'Candice', 'Mathias', 'Emmy', 'Mathias', 'Emma', 'Antoine', 'Tristan', 'Antoine', 'Tristan', 'Candice', 'Louka', 'Louka', 'Tristan', 'Ahmed', 'Elouo', 'Emmy', 'Antoine', 'Alissa', 'Ahmed', 'Antoine', 'Alissa', 'Louan', 'Emma', 'Elouo', 'Tristan', 'Emmy', 'Elouo', 'Louka', 'Emmy', 'Ahmed', 'Louka', 'Vincent', 'Vincent', 'Antoine', 'Ahmed', 'Ahmed', 'Vincent', 'Tristan', 'Louan', 'Emmy', 'Elouo', 'Louka', 'Emmy', 'Hugo', 'Emmy', 'Emma', 'Emma', 'Hugo', 'Louan', 'Hugo', 'Antoine', 'Ahmed', 'Emmy', 'Vincent', 'Emma', 'Candice', 'Candice', 'Louka', 'Louan', 'Alissa', 'Vincent', 'Vincent', 'Tristan', 'Louka', 'Louan', 'Louka', 'Antoine', 'Tristan', 'Alissa', 'Ahmed', 'Vincent', 'Louka', 'Alissa', 'Mathias', 'Elouo', 'Emmy', 'Ahmed', 'Emmy', 'Vincent', 'Elouo', 'Emma', 'Mathias', 'Ahmed', 'Vincent', 'Mathias', 'Candice', 'Elouo', 'Louan', 'Elouo', 'Vincent', 'Emmy', 'Emma']    
apparition = {}
for prenom in lst:
    if prenom not in apparition:
        apparition[prenom] = 1
    else:
        apparition[prenom]+=1
        
print(apparition)
        



