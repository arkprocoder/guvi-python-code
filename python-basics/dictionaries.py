mydict={
   "employeeName":"Ark",
   "employeeRole":"Developer",
   "since":2021,
   "salary":154782.36,
   "skills":['java','python','c++'],
   "interest":{'cricket','volleyball','football'},
   "isActive":True 
}
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# for key,value in mydict.items():
#     print(key,value)

# print(mydict.get("employeeName"))
# print(mydict.get("skills"))
# print(mydict.get("isActive"))
# print(mydict.get("aa"))

mydict.update({
    "phone":87452136987,
    "city":'Bangalore'
})

mydict.update({
    "isActive":False
})

mydict2=mydict.copy()

print(mydict)
print(mydict2)

mydict2.clear()
print(mydict2)