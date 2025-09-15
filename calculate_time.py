'''
    CS 5001
    Lab 1
    Exercise 4
    Name:
'''

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''

def main():
# What time is it and when will the alarm go off?

    time_now = int(input('What time is it homie?'))
    hours_to_wait = int(input('How much longer until your alarm goes off?'))

# Now we calcuate what time the alarm will go off.

    alarm = (time_now + hours_to_wait) % 24
    if alarm >= 13: 
        print (f'Your alarm is going to go off at {alarm}pm?')
    else:
        print (f'Your alarm is going to go off at {alarm}am?')


if __name__ == '__main__':
    main()


