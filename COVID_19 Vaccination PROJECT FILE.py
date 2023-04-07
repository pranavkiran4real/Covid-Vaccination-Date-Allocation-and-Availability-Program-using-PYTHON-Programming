#                                                   MINI PROJECT

#                                                 COVID 19 PROJECT

#     Agenda for the COVID 19 mini project :-
#           1] Patient Details
#           2] MS Excel Database
#           3] Medical Issues
#           4] Vaccine Availability
#           5] Age wise Vaccine Dosage
#           6] Date Allotment 

while(True):  # to iterate the project , till the user exit the project 

    # 1] Displaying the Patient details in Table format
    def Display(name,age,gender,state,phno,patient_type): # Input is Passed from the Driver code

        for j in range(10000): # delay function to create a animation slide
              for k in range(10000):
                   pass

        print("\n")                                                                                              
        print("   PATIENT DETAILS   ".center(90,"="),"\n")   # center() -->  Returns a string with the original string
                                                             #               centered to a total of width columns
        print("    NAME       AGE  GENDER     STATE         PHONE NUMBER     TYPE  ")

        print(name.center(12," "),
              age.center(5," "),
              gender.center(7," "),
              state.center(16," "),
              phno.center(14," "),
              patient_type.center(12," "))   

    # 2] Storing the records in MS Excel using CSV module
    def database(name,age,gender,state,phno,patient_Type):

        for j in range(15000):        # delay function to Create a animation Slide
                  for k in range(15000):
                       pass
                    
        import csv  # CSV file ==> It is a human readable text file where each lines has a no of fields , separated by 
                    #                 commas or some other delimiters. CSV files have an extension of ".csv".
        print("\n")
        print("  MS EXCEL DATABASE  ".center(90,"="),"\n")           

        # storing the values in list 
        data = []
        data.extend([name,age,gender,state,phno,patient_Type])
                                                   #Extend() => To add multiple elements to the list in the same time
        print(" Storing the records in the MS Excel.............")

        for j in range(8000):        # delay function to Create a animation Slide
                  for k in range(8000):
                       pass
                    
        # using CSV module to store the list records in MS Excel
        
        with open("Excel_Database.csv","a") as WF:   # built-in function to open the CSV file
                                               # "WF" is the reference variable to access the CSV file 
                                               # "a" to append the data in the Excel 

            w = csv.writer(WF)   # Returns a writer object which converts the user's data into delimited string
            
            w.writerow(data)   # writes a row of data into the specified file

            print("")
            print(" The Patient details is successfully stored in the MS Excel Database !! ")
            print(" The records stored in the MS Excel sheet are :",data)

            WF.close()   # to close the CSV file
        
    # 3] Whether the patient experienced any medical issues
    def Medical_issue(name):

           for j in range(15000): # delay function to Create a animation slide
                  for k in range(15000):
                       pass

           print("\n")
           print("   MEDICAL ISSUES   ".center(90,"="),"\n")
           
           print(name,"have you Experienced any of the below issues :  \n")
           print(" 1] Experienced Cold,Cough,Fever,Breathlessness ")
           print(" 2] Have you tested against COVID-19 ")
           print(" 3] Free from Covid (normal) ")
           print("")
           choice = input(" Enter your option.........(1/2/3) : ")
           print("")
           
           if(choice == "1"):
                  print(" We request you to follow the guidelines issued by the government ")
                  print(" Don\'t forget to take the vaccine on your turn")

           elif(choice == "2"):
                  
                  ch = input(" Whether the result is Positive or Negative.......(P/N)")
                  print("")
                  if(ch == "P"):
                         print(" your test is Positive ")
                         print(" Take the Vaccine immediately!!! ")
                  else:
                         print(" your test is negative ")
                         print(" But don\'t forget to take the vaccine on your turn")

           else:
                  print(" Your Health condition is good ")
                  print(" But don\'t forget to take the vaccine on your turn")

                  
    # 4] Function to check for availability of vaccines in a particilar state
    def State_Vaccine_Availability (state):
            
        import csv
        for j in range(15000): # delay function to Create a animation slide
            for k in range(15000):
                pass
            
        print("\n")
        print("   VACCINE AVAILABILITY   ".center(90,"="),"\n")
        print(" Checking the Vaccine Availability in ",state,"............... \n")

        place = ""                      # input "State" may contain spaces or capital letters or small letters,  
        for i in state:                 # so converting all the letters to uppercase and without any spaces
            if ( i != " "):
                place += i.upper()
                    
        #A .csv file with various statename and corresponding vaccineavailability is created already
        
        #Opening the csv file in read mode to read the availability of vaccines
        with open ('AVAILABLEVAC.csv','r') as file1:
            content = csv.reader(file1)
            contentlist = list(content)#List to store each row of data as a list datatype

            #Removing empty lists in the content list
            contentlist = [i for i in contentlist if i != []]

            for i in range(len(contentlist)):
                if(place == contentlist[i][0]):
                    #If vaccines are available, number of vaccines in that state is reduced by 1 and availability is displayed
                    if (int(contentlist[i][1]) > 0 ):#If 
                        print("  Vaccine Available")
                        contentlist[i][1] = str(int(contentlist[i][1]) - 1)
                        print("  Remaining Vaccine available in {} is {}".format(state,contentlist[i][1]))
                    # If vaccine is not available in that particular state, "Vaccine not available is displayed "
                    else:
                        print("  Vaccine not available")

        #Opening the csv file in write mode to update the data
        with open ('AVAILABLEVAC.csv','w') as file2:
            writer = csv.writer(file2)
            writer.writerows(contentlist)# writerows to store multiple rows to a csv file
        
    # 5] Age wise Vaccine dosage for the Patients
    def Dosage(age,patient_type):

        for j in range(15000):        # delay function to Create a animation Slide
              for k in range(15000):
                   pass
                
        print("\n")
        print("   AGE WISE VACCINE DOSAGE   ".center(90,"="),"\n")
        print("  The patient age is ({}) and patient type is ({}) ".format(age,patient_type))
        print("")
        for j in range(10000):        # delay function to Create a animation Slide
              for k in range(10000):
                   pass
                
        age = int(age)        
        if(patient_type.lower()=="comorbidities"):    # Comorbidites --> The person who suffers from heart
                                                      #                  attack, sugar those traits
              if(age>=1 and age<=18):
                   print("    Required Vaccine Dosage is (250 ml)")

              elif(age>=18 and age<=50):
                   print("    Required Vaccine Dosage is (600 ml)")

              else:
                   print("    Required Vaccine Dosage is (450 ml)")

        else:     #Normal Person 

              if(age>=1 and age<=13):
                   print("    Required Vaccine Dosage is (250 ml)")

              elif(age>=13 and age<=18):
                   print("    Required Vaccine Dosage is (350 ml)")

              elif(age>=18 and age<=50):
                   print("    Required Vaccine Dosage is (450 ml)")

              else:
                   print("    Required Vaccine Dosage is (400 ml)")
               
    # 6] Date Allotment for the patient to visit the Hospital
    def inj_date(name,phno):

        for j in range(10000):        # delay function to Create a animation Slide
              for k in range(15000):
                   pass

        print("\n")
        print("   DATE ALLOTMENT   ".center(90,"="),"\n")
        
        # Input for the Date and the Month
        year= 2021
        dd = int(input(" Enter the day (in Digit) :"))  # 23/7/2021 # 7/4/2021
        mm = int(input(" Enter the month (in Digit) :"))
        
        print(" Checking the availability of the Date ................ ")
        
        for j in range(10000):        # delay function to Create a animation Slide
              for k in range(10000):
                   pass

        print("\n")
        print(" The Date is Available! ")
        print(" Your 1st injection date:{}-{}-{}".format(dd,mm,year))
        print(" . . . . . . . . . . . . . . . . . . . . . . .")
        print(" Mr/Mrs.{}, The 2nd injection date will be sent to your mobile no:{}".format(name,phno))
        print("\n")

        for j in range(15000):        # delay function to Create a animation Slide
              for k in range(15000):
                   pass
                
        # If statement to find the Date for Second injection

        print(" Opening the Inbox Messages in the Phone...................")
        print("")

        if(dd>15 and mm==4 or mm==6 or mm==9 or mm==11):
            dd=dd-15
            mm=mm+1
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))
            
        elif(dd<=15 and mm==4 or mm==6 or mm==9 or mm==11):
            dd=dd+15
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))

        elif(dd>16 and mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10):
            dd=dd-16
            mm=mm+1
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))
            
        elif(dd<=16 and mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10):
            dd=dd+15
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))

        elif(mm==12 and dd<=16):
            dd=dd+15
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))
        
        elif(mm==12 and dd>16):
            dd=dd-16
            mm=1
            year+=1
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))

        elif(mm==2 and dd<=13):
            dd=dd+15
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))

        elif(mm==2 and dd>13):
            dd=dd-13
            print("   Your 2nd injection date is {}-{}-{}".format(dd,mm,year))

        for j in range(10000):        # delay function to Create a animation Slide
                for k in range(10000):
                    pass
                    
        print("\n")
        print(" Wear Mask; keep Social Distance and Stay Healthy !!!!!! ".center(90,"`"))


    # DRIVER CODE
    # Display the Project Agenda
    print("\n")
    print("   MINI PROJECT   ".center(90,"`"),"\n")
    print("   COVID 19 PROJECT   ".center(90,"`"),"\n")
    print("  Agenda for the COVID 19 mini project :-   ")
    print("     1] Patient Details ")
    print("     2] MS Excel Database  ")
    print("     3] Medical Issue ")
    print("     4] Vaccine Availability ")
    print("     5] Age wise Vaccine Dosage ")
    print("     6] Date Allotment \n ")

    # Input for the program
    def Input_Validation():

         import re
         States_list = ["ANDHRAPRADESH","ARUNACHALPRADESH","ASSAM","BIHAR","CHATTISGARH","GOA","GUJARAT","HARYANA",
                   "HIMACHALPRADESH","JHARKHAND","KARNATAKA","KERALA","MADHYAPRADESH","MAHARASHTRA","MANIPUR",
                   "MEGHALAYA","MIZORAM","NAGALAND","ODISHA","PUNJAB","RAJASTHAN","SIKKIM","TAMILNADU","TELANGANA",
                   "TRIPURA","UTTARPRADESH","UTTARAKHAND","WESTBENGAL","ANDAMANANDNICOBAR","CHANDIGARH","DAMANANDDIU",
                   "DELHI","JAMMUANDKASHMIR","LADAKH","LAKSHADWEEP","PUDUCHERRY"]

         print("   INFORMATION:-      ")
         while (True):   # input to get NAME
              name = input(" Enter name: ")
              if(bool(re.match('[a-zA-Z\s]+$', name))):
                   break
              else:
                   print(" Invalid Input")              

         while (True):   # input to get AGE
              age = input(" Enter age: ")
              if(bool(re.match('[\d]{2}$', age))):
                   break
              else:
                   print(" Invalid Input")

         gender = input(" Enter your Gender( Male / Female / Others ): ") # input to get Gender
         
         while (True):   # input to get STATE NAME
              state = input(" Enter state: ")

              place = ""                      # input "State" may contain spaces or capital letters or small letters,  
              for i in state:                 # so converting all the letters to uppercase and without any spaces
                   if ( i != " "):
                        place += i.upper()
                        
              if(place in States_list):
                   break
              else:
                   print(" Invalid Input")

         while (True):   # input to get PHONE NUMBER
              phone_number = input(" Enter phone number: ")
              if(bool(re.match('[\d]{10}$', phone_number))):
                   break
              else:
                   print(" Invalid Input")

         patient_type = input(" Patient Type( Comorbidities / Normal ): ")#Comorbidites --> The person who suffers from 
                                                                          #             heart attack, sugar those traits
         return(name, age, gender, state, phone_number, patient_type)
    
    Name,Age,Gender,State,Phno,Patient_Type = Input_Validation() # Validation for the inputs

    # Calling the functions 
    Display(Name,Age,Gender,State,Phno,Patient_Type)       # Input is passed to the function "Display"

    database(Name,Age,Gender,State,Phno,Patient_Type)      # Input is passed to the function "database"
    
    Medical_issue(Name)                                    # Input is passed to the function "Medical_issue"
    
    State_Vaccine_Availability(State)                      # Input is passed to the function "State_Vaccine_Availability"

    Dosage(Age,Patient_Type)                               # Input is passed to the function "Dosage"
    
    inj_date(Name,Phno)                                    # Input is passed to the function "inj_date"

    
    # To Leave the Project
    print("\n")
    Choice = input(" Do you want to Exit the Page....................... (y / n)  ")
    if(Choice == "y"):
        print()
        print(" Leaving the Project........... ")
        break
