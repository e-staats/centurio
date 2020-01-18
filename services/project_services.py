from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.projectattempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import datetime
# pylint: disable=no-member

def get_project_from_id(project_id):
    project = Project.objects(id=project_id).first()
    if not project:
        return None
    return project

def get_project_from_link_id(project_link_id):
    project = Project.objects(link_identifier=project_link_id).first()
    if not project:
        return None
    return project

def get_project_summaries() -> dict:
    mongo_setup.global_init()
    projects = {}
    for project in Project.objects():
        projects[project.id] = {
            'name': project.name,
            'desc': project.description,
            'link_identifier': project.link_identifier,
            'days': {}
        }
        # for i in range(1,6):
        #     project[project.id]['days'][i]=

    return projects

def format_project_list_for_user(project_dict, user) -> dict:
    user_projects = get_project_statuses_for_user(user)
    for project_id in project_dict:
        if project_id in user_projects:
            project_dict[project_id]['user_status'] = user_projects[project_id]
            project_dict[project_id]['user_status_formatted'] = user_projects[project_id].replace("-"," ").title()
        else:
            project_dict[project_id]['user_status'] = ''

def get_project_statuses_for_user(user):
    return_dict = {}
    attempt_list = user.attempts
    for attempt_id in attempt_list:
        attempt = Attempt.objects(id=attempt_id).first()
        project_id = attempt.project_id
        return_dict[project_id] = attempt.status
    return return_dict

def get_projects_for_user(user):
    return_list = []
    attempt_list = user.attempts
    for attempt_id in attempt_list:
        attempt = Attempt.objects(id=attempt_id).first()
        project_id = attempt.project_id
        project = get_project_from_id(project_id)
        return_list.append(project)
    return return_list

def add_project_to_user(user, project_link):  
    user_id = user.id  
    project = Project.objects().filter(link_identifier=project_link).first()
    if not project:
        return
    start_date = datetime.date.today()
    date = start_date

    project_attempt = Attempt()
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
        return
    success = User.objects(id=user_id).update_one(push__attempts=project_attempt.id)
    if not success:
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


def _add_project_test():
    project = Project()
    project.name = "20 days of Pushups" #input("What is the name of this project? ")
    project.description = "In this project, you will do an ever increasing amount of pushups." #input("Describe this project? ")
    project.link_identifier = "20-days-of-pushups"

    for i in range(1,21):
        day = Day()
        day.name = "Day " + str(i)
        day.description = f"Do {i} pushups"
        day.ordinal = i
        day.est_minutes = 2
        project.days.append(day)

    project.save()

    project2 = Project()
    project2.name = "25 days of Python" #input("What is the name of this project? ")
    project2.description = "In this project, you will code a cool app" #input("Describe this project? ")
    project2.link_identifier = "25-days-of-python"


    for i in range(1,26):
        day = Day()
        day.name = "Day " + str(i)
        day.description = f"Code for {3*i} minutes"
        day.ordinal = i
        day.est_minutes = 3*i
        project2.days.append(day)

    project2.save()

def _add_user_attempt_test(user):
    add_project_to_user(user, "20-days-of-pushups")


