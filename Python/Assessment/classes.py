
import random
import string

class Mainevent():

    def genid(self): #Unique ID for attendees
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) #Generate a random string of alpha numerical characters of length 8 to use an a unique ID
        while id in self.attendees.keys(): #If the ID already exists it will keep generating new ID's until it generates one that doesn't already exist
            id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return id #Returns unique ID


    def __init__(self, name, time, location,id): # Initialise Mainevent class
        self.name = name
        self.time = time
        self.location = location
        self.id = id
        self.attendees = {} # Key : value         attendee.id : attendee
        
    
    def ListOne(self):
        return self.name, self.time , self.location, self.ListAttendees() # Returns all relevant information for one Mainevent class object.
    
    
    def EditEvent(self, name, time, location): # Updates information for relevant class object to the new given values
        self.name = name
        self.time = time
        self.location = location
            
    
    def ListAttendees(self):
        return [f'{attendee.name()} - Attendee ID: {attendee.id}' for attendee in self.attendees.values()] # Returns all relevant data for Attendees within attendee dictionary in Mainevent class
        
    
    def Invite(self, first_name, last_name): # Makes Attendee class object with inputted information
        invitee = Attendee(first_name, last_name, self.genid())
        self.attendees[invitee.id] = invitee
        return invitee.id # Returns unique attendee ID

    def Revoke(self, attendid): # Removes Attendee from attendee dictionary
        del self.attendees[attendid]

class Attendee():
    
    def __init__(self, first_name, last_name, id): # Initialise Attendee Class
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    
    def name(self): # Returns the full name of an Attendee
        return f'{self.first_name} {self.last_name}'

