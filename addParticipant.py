import json
with open('./Participant_data.json',"r") as json_file:
    temp_dictonary=json.load(json_file)
flag='Y'
while True:
    x= input("Enter the name: ")
    temp_dictonary[x]=input("Hii "+x+" enter your email id: ")
    flag=input("Do you want to add another participant?(Y/N)")
    if(flag=='N' or flag=='n'):
        break
with open("./Participant_data.json","w") as json_file:
    json.dump(temp_dictonary,json_file)
print("Participant added successfully")



   
