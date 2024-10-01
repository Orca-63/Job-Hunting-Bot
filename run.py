from Jobs.jobs import jobs
import time

with jobs() as bot:
    bot.land_first_page()
    time.sleep(2)
    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)
    try:
        bot.choose_Job_Title(input(" Please enter your preferred Job : "))
        time.sleep(2)
    except:
        print('Sorry, no jobs found!')

    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)
    try:

        bot.choose_Job_Location(
            input(" Please enter your preferred Location : "))
        time.sleep(2)
    except:
        print('Sorry,no jobs found!')
    try:

        bot.close_Pop_Up()
        bot.close_suggestion()

    finally:
        time.sleep(2)
    try:
        bot.choose_Education_Level(
            input(" Please enter your current/highest level of education : "))
        time.sleep(2)
    except:
        print('Sorry,no jobs found!')
    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)
    try:
        bot.choose_industry(input(" Please enter your preferred industry : "))
        time.sleep(2)
    except:
        print('Sorry,no jobs found!')
    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)

    try:
        bot.choose_Salary(input('Please enter your expected salary : '))
        time.sleep(2)
    except:
        print('Sorry,no jobs found!')
    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)
    try:
        bot.choose_Job_Type(
            input(' Please enter your preferred role(Internship/Full-time) : '))
        time.sleep(2)
    except:
        print('Sorry,no jobs found!')
    try:
        bot.close_Pop_Up()
        bot.close_suggestion()
    finally:
        time.sleep(2)
    print('Available Jobs are : ')
    bot.display_results()
    print("Exiting...")
