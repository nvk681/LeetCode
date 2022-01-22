def numUniqueEmails(emails):
    updated_emails = []
    for email in emails:
        split_email = email.split('@')
        user = split_email[0].replace('.', '')
        user = user.split('+')[0]
        updated_emails.append(str([user, '@', split_email[1]]))
    set_of_emails = set(updated_emails)
    return len(set_of_emails)