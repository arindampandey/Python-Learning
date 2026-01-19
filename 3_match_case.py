def htp_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not OK"
        case 500:
            return "Error !!"
        case _: # Default Condition
            "Unknown Status"

print(htp_status(404))
print(htp_status(200))
print(htp_status(500))
print(htp_status(330))