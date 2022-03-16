from linkedin_api import Linkedin

#temporary data
companyList = ['Goldman Sachs', 'J.P. Morgan', 'Credit Suisse']
linkedInMessage = "Hello [FirstName]. I found your profile via [Company] LinkedIn page. Looking forward to connecting!"
emailMessage = "Hello [FirstName], I was wondering if you have any interest/availability for a quick chat.  Thank you for your time, John Stamos"

#ask user for LinkedIn username/password
username = input("Enter LinkedIn username: ")
password = input("Enter LinkedIn password: ")

api = Linkedin(username, password)

for company in companyList:
    #get company search results
    companyResults = api.search_people(keywords=company, limit=1)

    #get public id
    publicId = companyResults[0]['public_id']

    #get first name and last name
    personResult = api.get_profile(publicId)
    firstName = personResult['firstName']
    lastName = personResult['lastName']

    #configure linkedin message
    tempLinkedInMessage = linkedInMessage
    tempLinkedInMessage = tempLinkedInMessage.replace("[FirstName]", firstName)
    tempLinkedInMessage = tempLinkedInMessage.replace("[Company]", company)

    print("Sending connection to " + firstName + " " + lastName)

    #send linkedin connection
    #api.add_connection(profile_public_id=publicId, message=tempLinkedInMessage)
