import re
"""
Given a document potential-contacts, find and collect all email addresses and phone numbers.
Phone numbers may be in various formats.
(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
phone numbers with missing area code should presume 206
phone numbers should be stored in xxx-yyy-zzzz format.
Once emails and phone numbers are found they should be stored in two separate documents.
The information should be sorted in ascending order.
Duplicate entries are not allowed.
"""


def get_doc(path):
    # read the file
    with open(path, 'r') as file:
        text = file.read()
    return text


# get text from file w/ helper
incoming_doc = get_doc("potential-contacts.txt")


def get_phone_nums(txt):
    # regex string that extracts number from '' space to '' space and split them into groups
    regex_key = r"((\(\d{3}\)|\d{3})?[\s-]?(\d{3})[\s-]?(\d{4}))"
    # find all string that match our regex key and return a collection
    numbers = re.findall(regex_key, txt)
    # set phone numbers to an empty collection
    fixed_numbers = []
    for num in numbers:
        # set prefix to empty string
        prefix = ""
        # if no num @ index one add 206
        if not len(num[1]):
            prefix += "206"
        # if len is 5 attach prefix to char 1-4 of index 1 to remove paren
        elif len(num[1]) == 5:
            prefix += num[1][1:4]
        else:
            # else num is already formatted correctly
            prefix += num[1]
        # format num correctly
        working_num = f"{prefix}-{num[2]}-{num[3]}"
        # add formatted num to fixed numbers without duplication
        if not working_num in fixed_numbers:
            fixed_numbers.append(working_num)
    # sort fixed numbers
    fixed_numbers.sort()
    return fixed_numbers


# pass text from file through phone number formatting function
new_numbers = get_phone_nums(incoming_doc)


def store_p_nums(p_nums):
    # write new numbers to empty txt file using w and file.write
    with open("phone_numbers.txt", 'w') as file:
        file.write("\n".join(p_nums))


def get_emails(txt):
    # regex string to find emails
    regex_key = r"(\w+(\.\w+)*@\w+\.\w+)"
    # finad all that match key within the document 'txt'
    emails = re.findall(regex_key, txt)
    # set pulled emails to an empty collection
    pulled_emails = []
    for email in emails:
        # add emails without duplication
        if not email[0] in pulled_emails:
            pulled_emails.append(email[0])
    # sort emails
    pulled_emails.sort()
    return pulled_emails


# pull the emails from the doc with our function
new_emails = get_emails(incoming_doc)


def store_emails(emails):
    with open("emails.txt", 'w') as file:
        file.write("\n".join(emails))


# write formatted and extracted numbers to text file
store_p_nums(new_numbers)
# write new emails to emails text file
store_emails(new_emails)
