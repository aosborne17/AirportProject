import time

class Menu_interface():
    def create_booking(self):
        passenger_input = input("Please select from the options.")

        if passenger_input == 't':
            passenger_information = []
            print("one moment please...")
            time.sleep(1)
            print("\nPlease follow the prompts and ensure the information is carefully inputted.\n")
            p_title = input(("Please enter the passenger's title of courtesy: (as it appears on the travel document: \n "))
            passenger_information.append(p_title)
            # first_name_confirmation = str(input("would you like to continue with the first name: {}\n (y/n)".format(passenger_first_name))
            p_first_name = str(input("Please enter the passenger's first name: (as it appears on the travel document) \n")).title()
            passenger_information.append(p_first_name)
            # last_name
            p_last_name = str(input("Please enter the passenger's last name: (as it appears on the travel document) \n")).title()
            passenger_information.append(p_last_name)
            # dob
            p_dob =  input("Please enter the passenger's date of birth: (yyyy/mm/dddd format) \n")
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
            return passenger_information
            # all_passengers.append(passenger_information)

    # def