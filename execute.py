from threading import*
import main_code as x 
from main_code import*
#importing the main file


x.create("sastra",25)
#creates a key with key_name,value given and with no time-to-live property


x.create("src",70,3600) 
#creates a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("sastra")
#returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("src")
#returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("sastra",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("sastra",55)
#it replaces the initial value of the respective key with new value 

 
x.delete("sastra")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
