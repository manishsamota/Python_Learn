# def httpstatus(status):
#     match status:
#         case 200:
#             return "Ok"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Error"
        
# print(httpstatus(200))
# print(httpstatus(404))
# print(httpstatus(500))
# print(httpstatus(305))

# DICTIONARY MERGE & UPDATE OPERATORS 
dict1  = {"a":1, "b" :2}
dict2  = {"c":3, "d" :4}

merged = dict1  | dict2

print(merged)

