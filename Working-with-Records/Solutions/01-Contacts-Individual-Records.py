from dataclasses import dataclass

def setupRecordAddData():
    
    @dataclass
    
    class Contact:
        
        Name: str
        Age: int
        PhoneNumber: str
        WhatsApp: bool
        Rating: float

    Contact1 = Contact("Bruce Taylor", 14, "01123298567", bool(1), 7.6)
    Contact2 = Contact("Gina Williams", 15, "0112175684", bool(0), 4.9)
    Contact3 = Contact("Trevor Youngson", 15, "0112081056", bool(0), 6.1)
    Contact4 = Contact("Penny Davies", 13, "0112665472", bool(1), 9.1)

    return Contact1, Contact2, Contact3, Contact4

def displayAllContacts(Contact1, Contact2, Contact3, Contact4):

    print ("All Contacts...")
    print ()
    print (Contact1.Name,"(",Contact1.Rating,") - On WhatsApp",Contact1.WhatsApp,"- Number",Contact1.PhoneNumber)
    print (Contact2.Name,"(",Contact2.Rating,") - On WhatsApp",Contact2.WhatsApp,"- Number",Contact2.PhoneNumber)
    print (Contact3.Name,"(",Contact3.Rating,") - On WhatsApp",Contact3.WhatsApp,"- Number",Contact3.PhoneNumber)
    print (Contact4.Name,"(",Contact4.Rating,") - On WhatsApp",Contact4.WhatsApp,"- Number",Contact4.PhoneNumber)

    return

def FourteenOrUnder(Contact1, Contact2, Contact3, Contact4):
    print ()
    print ("Contacts 14 years old or younger...")

    if Contact1.Age <= 14:
        print (Contact1.Name," ",Contact1.PhoneNumber)

    if Contact2.Age <= 14:
        print (Contact2.Name," ",Contact2.PhoneNumber)

    if Contact3.Age <= 14:
        print (Contact3.Name," ",Contact3.PhoneNumber)

    if Contact4.Age <= 14:
        print (Contact4.Name," ",Contact4.PhoneNumber)

    return
  
def main():
  Contact1, Contact2, Contact3, Contact4 = setupRecordAddData()
  displayAllContacts(Contact1, Contact2, Contact3, Contact4)
  FourteenOrUnder(Contact1, Contact2, Contact3, Contact4)

main()

