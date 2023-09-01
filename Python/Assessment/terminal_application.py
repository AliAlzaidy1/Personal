from datetime import datetime
from classes import Mainevent
import random
import string
import pickle

def updatefile(eventdict): #Function to update pickle file
    with open('events.pkl', 'wb') as outfile: #Opens file in binary mode
        pickle.dump(eventdict,outfile) #Puts/serialises the events dictionary object into the pickle file


def loadfile(): #Function to load pickle object from file
    try: #Gaurd against first time use where the file doesn't yet exist
        with open ('events.pkl','rb') as infile: #Opens file in binary mode
            return pickle.load(infile) #Returns deserialised class object (reconverts from pickle form into deserialised data)
    except:
        return {} #initialise a dictionary if file doesn't exist

eventdict = loadfile() #Assign a variable to function above



def validateEventID(eventid): #Check if event ID exists/validate event
    if eventdict.get(eventid):
        return True
    else:
        return False

def listone(eventid):
    if validateEventID(eventid): # If event ID exists, execute command to show the event
        name, time, location, attendees = eventdict[eventid].ListOne()
        print( f'name: {name} \ntime: {time} \nlocation: {location} \nattendees: {attendees} ' )
    else: #If it doesn't exist print an error statement then return to action page
        print("Invalid ID. Returning to main menu.")


def EditEvent(eventid, name, time, location):
    if validateEventID(eventid): #check If event ID exists
        try:
            time = datetime.strptime(time,'%d.%m.%Y %H:%M') #Make sure date is given in the right format
        except ValueError: #If it's the wrong format print an error message
            print("Invalid time format. Returning to main menu")
        else: #If the date is in the right format it will allow the edit and proceed with it
            eventdict[eventid].EditEvent(name, time, location)
            (f'Event {eventid} Edited!')
    else: #If the event ID doesn't exist print an error message and return to action screen
        print("Invalid event ID. Returning to main menu.")



def listAttendees(eventid):
    if validateEventID(eventid): #Check if the event ID exists
        print(eventdict[eventid].ListAttendees()) #Print all attendees at the event by calling class function ListAttendees
    else:
        print("Invalid event ID. Returning to main menu.") 



def Invite(eventid, first_name, last_name):
    if validateEventID(eventid): #Check if event ID exists
        print(f'Attendee ID: {eventdict[eventid].Invite(first_name, last_name)}') #Call class function Inivte to add data to Attendee class
        print(f'Guest {first_name} {last_name} has been invited!') #Print statement confirming the attendee has been invited 
    else:
        print("Invalid event ID. Returning to main menu.") #Statement when event ID doesn't exist


def Revoke(eventid, attendid):
    if validateEventID(eventid): #Check if event ID exists
        eventdict[eventid].Revoke(attendid) #Using event ID in eventdict, removes the attendee by calling class function
        print(f'Guest {attendid} not allowed to come anymore!') #Confirmation statement
    else:
        print("Invalid event ID. Returning to main menu.") #Error statement


def DeleteEvent(eventid):
    if validateEventID(eventid): #validate event ID
        del eventdict[eventid] # Delete event from event dictionary
        print(f'Event {eventid} Deleted!') #Confirmation message
    else:
        print("Invalid event ID. Returning to main menu.") #Error statement


def listAll():
    for id, event in eventdict.items(): #Print all events in event dict
        print([f'Event name: {event.name}, Event ID: {id}, Event Location: {event.location}, Event time: {event.time}' ]) #Presenting in a readable manner


def CreateEvent(name, time, location): 
    try:
        time = datetime.strptime(time, '%d.%m.%Y %H:%M') # Validate correct format for date and time
    except ValueError: # Won't allow wrong format
        print("Invalid time Format. Returning to main menu") # If the format is wrong it will return an error message
    else: #If format is correct, create the event with given name time and location
        newevent = Mainevent(name, time, location, genid()) # Assign an ID to the event and initialise as class object
        eventdict[newevent.id] = newevent # Adds event to event dictionary
        print(f'Event {newevent.name} Created!') # Confirmation message
        print(f'Your Event ID is: {newevent.id}')


def genid(): #Generate unique ID for events
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) #Generate a random string of alpha numerical characters of length 8 to use an a unique ID
    while id in eventdict.keys(): #If the ID already exists it will keep generating new ID's until it generates one that doesn't already exist
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return id #Returns unique ID



dictfunction = {0:"0: Create an Event",
                1:"1: List all Events",
                2: "2: List an individual event using event ID",
                3: "3: Edit an event",
                4: "4: Delete an event",
                5: "5: List the attendees attending an event",
                6: "6: Add an attendee to an event",
                7: "7: Delete an attendee from an event",
                8: "8: Exit program"} # Create a dictionary for options shown in terminal application




while True: # Ensure it loops through the options so that you can perform multiple actions in one session
    print("Please input one of the following options (0 - 7)")
    for i in dictfunction.values():
        print(i) # Prints the values of the previously made dictionary to show options to user

    validanswer = False
    while not validanswer: # Ensure the user inputs the correct numbers, if any number above 7 or lower than 0 is selected the loop will continue until a valid number is inputted
        answer = input()
        if answer.isdigit(): # Ensure only numbers are taken as valid options
            if int(answer) < 9 and int(answer) >= 0:
                validanswer = True
            else:
                print("Please input a valid number between 1 and 7")  
        else:
            print("Please input a valid number between 1 and 7")


    match int(answer): # Match the input given to a function, each case will have the relevant amount of inputs with a description that asks for the relevant data and describes how the data should be presented when format is an issue.
        case 0:
            case0name = input("Input Event name: \n")
            case0location = input("Input Event location: \n") 
            case0time = input("Input Event time in the following format -> 'DD.MM.YYYY HH:MM' E.g '26.01.2025 18:30':\n")
            CreateEvent(case0name, case0time, case0location) # Each case corresponds to its own function and takes the user inputs as variables for each respective function

        case 1:
            print("All events listed below")
            listAll()

        case 2:
            case2 = input("Input Event ID: \n")
            listone(case2)

        case 3:
            case3id = input("Input Event ID for the event that you'd like to change:\n")
            case3name = input("Input new name:\n")
            case3location = input("Input new location:\n") 
            case3time = input("Input new time in the following format -> 'DD.MM.YYYY HH:MM' E.g '26.01.2025 18:30':\n")
            EditEvent(case3id, case3name, case3time, case3location)
        case 4:
            case4 = input("Input Event ID of the Event you'd like to delete:\n")
            DeleteEvent(case4)
        case 5:
            case5 = input("Input Event ID:\n")
            listAttendees(case5)
        case 6:
            case6id = input("Input Event ID of the event you'd like to invite a guest to:\n")
            case6fname = input("Input guest first name:\n")
            case6lname = input("Input guest last name:\n") 
            Invite(case6id, case6fname, case6lname)
        case 7:
            case7eid = input("Input Event ID of the event you'd like to uninvite a guest to:\n")
            case7aid = input("Input the attendee ID of the guest you'd like to uninvite:\n")
            Revoke(case7eid, case7aid)

        case 8:
            break # Exit program

    updatefile(eventdict) # Updates the pickle file at the end of each action execution then returns to the start of the while loop to allow user to perform other actions





