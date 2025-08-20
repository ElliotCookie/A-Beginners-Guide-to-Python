#Write a function, which takes a non-negative integer (seconds) 
# as input and returns the time in a human-readable format (HH:MM:SS)

#HH = hours, padded to 2 digits, range: 00 - 99
#MM = minutes, padded to 2 digits, range: 00 - 59
#SS = seconds, padded to 2 digits, range: 00 - 59
#The maximum time never exceeds 359999 (99:59:59)

#You can find some examples in the test fixtures.

"""     test.assert_equals(make_readable(0), "00:00:00")
        test.assert_equals(make_readable(59), "00:00:59")
        test.assert_equals(make_readable(60), "00:01:00")
        test.assert_equals(make_readable(3599), "00:59:59")
        test.assert_equals(make_readable(3600), "01:00:00")
        test.assert_equals(make_readable(86399), "23:59:59")
        test.assert_equals(make_readable(86400), "24:00:00")
        test.assert_equals(make_readable(359999), "99:59:59") """

""" def make_readable(seconds):
    pass """

def make_readable(seconds):
    #Calculate hours in the seconds 
    hours_counter = int(seconds / (60 * 60))
    remaining_seconds = seconds - (hours_counter * 3600)

    #calculate the minutes in the seconds left
    minutes_counter = int(remaining_seconds / 60)
    remaining_seconds = int(remaining_seconds - (minutes_counter * 60))

    #Seconds left is already calculated? 

    formatted_time = str(hours_counter).zfill(2) + ":" + str(minutes_counter).zfill(2) + ":"+ str(remaining_seconds).zfill(2)

    return formatted_time



print(make_readable(0))
print(make_readable(3599))
print(make_readable(86399))
print(make_readable(359999))