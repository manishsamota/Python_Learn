def httpstatus(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Error"
        
print(httpstatus(200))
print(httpstatus(404))
print(httpstatus(500))
print(httpstatus(305))

