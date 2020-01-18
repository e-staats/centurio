import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
import centurio.services.mongo_setup as mongo_setup
from centurio.data.users import User
from faker import Faker
from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.projectattempts import ProjectAttempt
from centurio.data.attemptdays import AttemptDay
from centurio.data.cohorts import Cohort
import datetime

# pylint: disable=no-member

def main():
    print_header()
    config_mongo()
    user_loop()

def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|               Centurio v.01                 |')
    print('|                POC edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()

def config_mongo():
    mongo_setup.global_init()

def user_loop():
    while True:
        print("Available actions:")
        print(" * list [u]sers and projects")
        print(" * list a[v]ailable projects")
        print(" * list all [d]ays in project")
        print(" * [w]hat's next for user")
        print(" * [a]dd project")
        print(" * add u[s]er")
        print(" * add [p]roject to user")
        print(" * co[m]plete day for user")
        print(" * [c]lear and refresh")
        print(" * [t]est_ad_hoc")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'u':
            list_users_and_projects()
        elif ch == 'v':
            list_available_projects()
        elif ch == 'd':
            list_days_in_project()
        elif ch == 'w':
            whats_next_for_user()
        elif ch == 'a':
            add_project()
        elif ch == 's':
            add_user()
        elif ch == 'p':
            user_id = add_user()
            add_project_to_user(user_id)
        elif ch == 'm':
            complete_day()
        elif ch == 'c':
            clear_and_refresh()
        elif ch == 't':
            test_ad_hoc()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def test_ad_hoc():
    pass


def clear_and_refresh():
    User.drop_collection()
    Project.drop_collection()
    ProjectAttempt.drop_collection()
    AttemptDay.drop_collection()
    Cohort.drop_collection()
    add_project()
    for i in range(20):
        user_id = add_user()
        add_project_to_user(user_id)
    return

def whats_next_for_user():
    start_date = datetime.date(2020,1,1) #these should be parameters, but I'm lazy.
    end_date = datetime.date(2020,1,7) #
    user = User.objects().first() #input("enter user ID: ")
    day_info_for_timerange(user,start_date,end_date)


def day_info_for_timerange(user,start_date,end_date):
    print()
    print(f"Here's the plan for {user.name}: ")
    attempt_list = ProjectAttempt.objects().filter(user_id=user.id,start_date__gte=start_date,start_date__lte=end_date)
    date = start_date
    while date >= start_date and date <= end_date:
        print(date)
        results = []
        for attempt in attempt_list:
            if attempt.status != 1:
                continue
            project = Project.objects(id=attempt.project_id).first()
            result_dict = get_attempt_info_for_date(attempt,date,project)
            if result_dict:
                results.append(result_dict)
        if len(results) != 0:
            for result in results:
                print(f"{result['project'].name} - Day {result['ordinal']}: {result['day'].description}")
        else:
            print("Nothing planned")
        date = date + datetime.timedelta(1)
 
        
def get_attempt_info_for_date(attempt,date,project):
    try:
        attempt_days_list = attempt.attempt_days[str(date)]
    except:
        return

    if not project:
        project = Project.object(id=attempt.project_id).first()
    if not project:
        return
    
    for attempt_day_id in attempt_days_list:
        attempt_day = AttemptDay.objects(id=attempt_day_id).first()
        day = project.days.get(ordinal=attempt_day.ordinal)
        return {"project": project,
                "ordinal": attempt_day.ordinal,
                "day": day,
                }

def complete_day():#attempt,date,project):
    user, attempt, project, day, attempt_day = test_get_user_attempt_project_day()
    success = AttemptDay.objects(id=attempt_day.id).update_one(complete_instant=datetime.datetime.now, status=2)

def test_get_user_attempt_project_day(ordinal=1):
    user = User.objects().first() #input("enter user ID: ")
    attempt = ProjectAttempt.objects().filter(user_id=user.id).first()
    attempt_day = AttemptDay.objects().filter(attempt_id=attempt.id).first()
    project = Project.objects(id=attempt.project_id).first()
    day = project.days.get(ordinal=ordinal)
    return (user,attempt,project,day,attempt_day)

def list_users_and_projects():
    for user in User.objects():
        print(user.name)
        for attempt_id in user.attempts:
            attempt = ProjectAttempt.objects(id=attempt_id).first()
            project = Project.objects(id=attempt.project_id).first()
            print(f"  started {project.name} on {attempt.start_date}")

def list_available_projects():
    for project in Project.objects():
        print(project.name)

def list_days_in_project():
    for project in Project.objects():
        print(project.name)
        for day in project.days:
            print(f"  {day.name}")

def add_project():
    project = Project()
    project.name = "100 days of Pushups" #input("What is the name of this project? ")
    project.description = "In this plan, you will do an ever increasing amount of pushups." #input("Describe this project? ")

    for i in range(1,101):
        day = Day()
        day.name = "Day " + str(i)
        day.description = f"Do {i} pushups"
        day.ordinal = i
        day.est_minutes = 2
        project.days.append(day)

    project.save()

def add_user():
    faker = Faker()
    user = User()
    user.name = faker.name()
    user.status = 1

    user.save()
    print(f"{user.name} added")
    return user.id


def add_project_to_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        print(f"Could not find user {user_id}")
        return
    
    project = Project.objects().first() #TEST
    if not project:
        print(f"Could not find project")
        return
    start_date = datetime.date(2020,1,1) #input("what is the start date of the Project? ")
    date = start_date

    project_attempt = ProjectAttempt()
    project_attempt.user_id = user_id
    project_attempt.project_id = project.id
    project_attempt.start_date = start_date
    success = project_attempt.save()
    if not success:
        print("unable to add project. Check the IDs and try again.")
        return
    
    update_dict={}
    for day in project.days:
        project_attempt_day = AttemptDay()
        project_attempt_day.ordinal = day.ordinal
        project_attempt_day.scheduled_day = date
        project_attempt_day.attempt_id = project.id
        project_attempt_day.save()
        update_dict[str(date)]=[project_attempt_day.id]
        date = date + datetime.timedelta(days=1)
    
    project_attempt.attempt_days = update_dict
    success = project_attempt.save()
    if not success:
        print("unable to add project. Check the IDs and try again.")
        return
    success = User.objects(id=user_id).update_one(push__attempts=project_attempt.id)
    if not success:
        print("unable to add project. Check the IDs and try again.")
        return
    
    cohort_id = find_cohort(project.id)
    add_user_to_cohort(user_id,cohort_id)

    print(f"{project.name} added to {user.name}")

def find_cohort(project_id):
    cohort = Cohort.objects().filter(project_id=project_id,status=1).first()
    if not cohort:
        cohort = Cohort()
        cohort.project_id = project_id
        cohort.save()
    return cohort.id

#needs testing
def add_user_to_cohort(user_id,cohort_id):
    success = Cohort.objects(id=cohort_id).update_one(push__users=user_id)
    if not success:
        print("unable to add user to cohort. Check the IDs and try again.")
        return
    
    success = User.objects(id=user_id).update_one(push__cohorts=cohort_id)
    if not success:
        print("unable to add cohort to user. Check the IDs and try again.")
        return
    
    cohort = Cohort.objects(id=cohort_id).first()
    if len(cohort.users) >= get_cohort_max():
        success = Cohort.objects(id=cohort_id).update_one(status=2)
        if not success:
            print("unable to close cohort. Check the IDs and try again.")
            return
    return True
    
def get_cohort_max():
    return 15

if __name__ == '__main__':
    main()