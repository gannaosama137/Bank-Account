def start () : 
    welcome_list = ["Register" , "Login" , "Exit"] 
    pretty_print("Welcome To Python Bank")
    list_print_choose(welcome_list)
    return handleINT("Choose from the list : ")



def pretty_print(s) : 
    print(f"{"~"*10}{s}{"~"*10}")



def list_print_choose (list_to_print) : 
    i = 1
    for opt in list_to_print :
        print (f"{i}. {opt}") 
        i+=1   



def handleINT (s):
    while True :
      try :
         var = int(input (s))
         return var
      except ValueError :
         print("Please Enter Int")



def register() : 
    tries = len(bank_DB) 

    register_username = input("Please enter username : ").strip()

    while(tries ) :
    
        if(register_username == "" ) :
            register_username = input(f"Username can't be null , you have only {tries} try : ").strip()
            tries-=1 

        elif(register_username in bank_DB) : 
            register_username = input(f"Used Handle , you have only {tries} try : " ).strip()
            tries-=1 

        else :
            break     
        
    if(register_username == "" or register_username in bank_DB):
         print("Registration Failed")
         return

    register_password = input ("Pleaase enter long password (not less than 6 char) : ").strip()
    
    tries = 3
    while (tries ) :
        if(register_password == "") :
             register_password = input(f"Pasword can't be null , you have only {tries} try : ").strip()
             tries-=1 

        elif(len(register_password) <6 ) :
            register_password = input (f"Invalid Password , you have only {tries} try : ").strip()  
            tries-=1 

        else :
            bank_DB[register_username] = {
            "id": len(bank_DB) + 1,
            "password": register_password,
             "balance": 0
            }
            print ("You have been added successfully")
            return register_username
          
    print("Registration Failed")



def login() :

    login_username = input("Pleaase enter your username : " ).strip()  
    login_password = input ("Please input your password : ").strip()

    tries = 4 
    while(tries and (login_username not in bank_DB or  bank_DB[login_username]["password"] != login_password)) :
        
        if(tries ==1):
            pretty_print("Back to start")
            return 
        
        print(f"Invalid username or password , you have {tries-1} tries left")
        login_username = input ("Pleaase enter your username : " ).strip()
        login_password = input ("Please input your password : ").strip()
        tries-=1 

    return login_username



def change_password (user_name) :
    new_password = input ("Pleaase enter long password (not less than 6 char) : ").strip()
    
    tries = 3
    while (tries ) :
     
        if(new_password == "") :
             new_password = input(f"Pasword can't be null , you have only {tries} try : ").strip()
             tries-=1 


        elif(len(new_password) <6 ) :
            new_password = input (f"Invalid Password , you have only {tries} try : ").strip() 
            tries-=1 

             
        else :
            bank_DB[user_name]['password'] = new_password
            print ("Password have been changed successfully")
            return 
        
    print("Changing Password Failed")



def change_username (user_name) : 
    tries = len(bank_DB) 

    new_username = input("Please enter username : ").strip()

    while(tries ) :
        if(new_username == user_name) :
            new_username = input(f"new username can't be same like old, you have only {tries} try : ").strip()
            tries-=1      

        elif(new_username == "" ) :
            new_username = input(f"Username can't be null , you have only {tries} try : ").strip()
            tries-=1      

        elif(new_username in bank_DB) : 
            new_username = input(f"Used Handle ,you have only {tries} try : " ).strip()
            tries-=1      

        else :
            bank_DB[new_username] = bank_DB[user_name]
            del bank_DB[user_name]
            print ("Username have been changed successfully")
            return new_username 
            
        
    if(not tries):
         print("Changing username Failed")
         return



def transactio(user_name) : 
        touser = input("Please enter recipient's Username : ") 
        amount = handleINT("Please input amount : ") 

        if(touser == user_name ) : 
            print("A transfer to the same account is not allowed ")

        elif (touser not in bank_DB) :
            print("The other user doesn't exist")

        elif (amount <=0 ) :
            print ("Depost must be greater than 0")

        elif(amount >bank_DB[user_name]["balance"] ) : 
             print (f"Your Balance is less than this amount, max amout is {bank_DB[user_name]['balance']}")   

        else : 
            bank_DB[user_name]["balance"] -= amount 
            bank_DB[touser]['balance'] +=amount  
            print ("Successful Operation")



bank_DB = {
    "Jannah" : {
        "id" : 1 ,
        "password" : "4444444" , 
        "balance" : 1000
    } , 
    "Rana" : {
        "id" : 2 ,
        "password" : "5555555" , 
        "balance" : 2000
    } , 
     "Sohaila" : {
        "id" : 3 ,
        "password" : "6666666" , 
        "balance" : 3000
    } 
}



def main () : 
   username =""
   while True : 
        
        basic_op = start()
        if(basic_op==1) :
          username = register() 
          if username :
            break 

        elif (basic_op ==2 ) :
            username = login() 
            if username : 
               print(f"welcome,{username} \nYour Balance is {bank_DB[username]['balance'] }")
               break 
 
        elif(basic_op ==3):
            return

   while True : 
    
    pretty_print("Bank Menu")
    list = ["Check Balance" , "Deposit" , "Withdraw" ,
                     "Transfer" , "Change Password" ,"Change username" ,
                     "Number of Registered users" , "Logout" ]
    list_print_choose(list)
    op = handleINT("CHoose From List : ")

    if(op == 1) : 
      print(f"Your Balance is {bank_DB[username]['balance'] }")

    elif (op == 2 ) :
        depost = handleINT("Enter Depost : ")
        if(depost <= 0 ) :
            print ("Depost must be greater than 0")
        else :
            bank_DB[username]["balance"]+=depost 
            print ("Successful Operation")
            print(f"Your New Balance is {bank_DB[username]['balance'] }")


    elif (op == 3 ) : 
        withdraw = handleINT("Enter Withdraw : ") 

        if(withdraw <= 0 ) :
             print ("Depost must be greater than 0")

        elif(withdraw > bank_DB[username]['balance']) :
             print (f"Your Balance is less than withdraw , max amout is {bank_DB[username]['balance']}")   

        else : 
            bank_DB[username]["balance"] -= withdraw
            print ("Successful Operation")
            print(f"Your New Balance is {bank_DB[username]['balance'] }")


    elif (op == 4 ) : 
        transactio(username)

    elif (op == 5 ) :
         change_password(username) 

    elif (op == 6 ) :
        new_username = change_username(username)
        if new_username :
            username = new_username

    elif(op == 7 ) :   
        print (len(bank_DB)) 

    elif (op >8 or op <1) : 
        print("invalid number")
    else :
        print ("Logging out , thank you ")
        return     

main() 