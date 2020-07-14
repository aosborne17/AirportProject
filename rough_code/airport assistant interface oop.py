import time

class AirportAssistantInterface():

    def Welcome_interface(self):
        print("\n*** Airport Assistant Passenger Booking Interface ***")
        assistant_first_name = str(input("Please enter your name: \n")).title()
        print("Hello {}, what service does the passenger require:".format(assistant_first_name))
        user_exit_status = False
        user_help = "\nInstructions:\n\n" + "-> Create a new booking [T]\n" + "-> view an existing booking [S]\n" +\
                        "-> Amend an existing booking [E]\n" + "-> View Terms & Conditions of booking [D]\n" + "-> Count down to booking [A]\n" +\
                            "-> For help type [H]\n"
        print(user_help)
        
        while not user_exit_status:
            passenger_input = input("Please select from the options.")
            if passenger_input == 't':
                self.Passenger_Booking()
            elif passenger_input == 's':
                self.View_Existing_Booking()
            elif passenger_input == 'e':
                self.Amend_Booking()
            elif passenger_input == 'd':
                self.View_TCs_Booking()
            elif passenger_input == 'a':
                self.CountDown_To_Booking()
       

    def Passenger_Booking(self):
        
        all_passengers = []
        passenger_information = []
        print("one moment please...")
        time.sleep(1)
        print("\nfollow the prompts and ensure the information is carefully inputted\n")
        number_of_passengers = str(input("is this booking for more than one person (y/n):")).lower()
      
        if number_of_passengers == 'y':
            print("*** REMINDER *** customers can only make a booking for up to 5 passengers per booking")
            self.Multiple_Passengers_Per_Booking()
        else:
        # first_name_confirmation = str(input("would you like to continue with the first name: {}\n (y/n)".format(passenger_first_name))
            p_first_name = str(input("Please enter the passenger's first name: (as it appears on the travel document) \n")).title()
            passenger_information.append(p_first_name)
            # last_name
            p_last_name = str(input("Please enter the passenger's last name: (as it appears on the travel document) \n")).title()
            passenger_information.append(p_last_name)
            # dob
            p_dob =  input("Please enter the passenger's date of birth: (dd/mm/yyyy format) \n")
            passenger_information.append(p_dob)
            # gender
            print("\nMale")
            print("Female\n")
            p_gender = str(input("please select the passenger's gender: \n")).lower()
            if p_gender == 'male':
                passenger_information.append("Male")
            else:
                passenger_information.append("Female")
            # nationality
            p_nationality = str(input("Please confirm the passenger's nationality: \n")).title()
            passenger_information.append(p_nationality)
            # passport/travel document
            print("\n** Passport")
            print("** National Identity Card (Only Valid for European Travel)\n")
            p_travel_document = str(input("please confirm the passenger's travel document: \n"))
            if p_travel_document == 'passport':
                passenger_information.append("passport")
            else:
                passenger_information.append("National Identity Card")
            # travel document numbers 
            p_travel_document_number = int(input("please enter the passenger's travel document number: \n"))
            passenger_information.append(p_travel_document_number)
            print(passenger_information)
            all_passengers.append(passenger_information)
        
    def Amend_Booking(self):
        pass

    def View_Existing_Booking(self):
        pass
        
    def View_TCs_Booking(self):
        pass
        
    def CountDown_To_Booking(self):
        pass
    
    def Multiple_Passengers_Per_Booking(self):
        number_of_passengers = int(input("How many passengers are you booking for: \n"))
        for i in range(1, number_of_passengers):
            self.Passenger_Booking()


        pass



    


        







obj = AirportAssistantInterface()
obj.Welcome_interface()
obj.Passenger_Booking()
