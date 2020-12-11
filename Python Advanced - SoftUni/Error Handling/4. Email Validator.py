class NameTooShortError(Exception):
    """ Raised when the name in the email is less than or equal to <= 4 characters """
    pass


class MustContainAtSymbolError(Exception):
    """ Raised when there is no "@" in the email """
    pass


class InvalidDomainError(Exception):
    """ Raised when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org) """
    pass

allowed_domains = ["com", "org", "bg", "net"]
command = input()
while command != "End":
    invalid_email = False
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
        invalid_email = True
    else:
        name = command.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
        invalid_email = True
    domain = command.split(".")[1]
    if domain not in allowed_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        invalid_email = True
    if not invalid_email:
        print("Email is valid")
    command = input()