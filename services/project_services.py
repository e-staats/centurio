from centurio.data.projects import Project
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import centurio.services.day_services as day_service
import datetime
# pylint: disable=no-member

def get_project_from_id(project_id):
    mongo_setup.global_init()
    project = Project.objects(id=project_id).first()
    if not project:
        return None
    return project

def get_project_from_link_id(project_link_id):
    mongo_setup.global_init()
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
            attempt_id, attempt_status,last_completion_date = user_projects[project_id]
            project_dict[project_id]['attempt_id'] = attempt_id
            project_dict[project_id]['user_status'] = attempt_status
            project_dict[project_id]['completion_date'] = last_completion_date
            project_dict[project_id]['user_status_formatted'] = attempt_status.replace("-"," ").title()
        else:
            project_dict[project_id]['user_status'] = ''

def get_project_statuses_for_user(user):
    return_dict = {}
    attempt_list = Attempt.objects(user_id=user.id)
    for attempt in attempt_list:
        project_id = attempt.project_id
        last_completion_date = get_last_completion_for_project_and_user(project_id, user.id)
        return_dict[project_id] = (attempt.id, attempt.status, last_completion_date)
    return return_dict

def get_last_completion_for_project_and_user(project_id,user_id):
    attempt = Attempt.objects(project_id=project_id,user_id=user_id).filter(status="complete").order_by('-completion_date').first()
    if attempt:
        return attempt.completion_date.strftime("%B %d %Y")


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
    cohort_id = find_cohort(project.id)
    start_date = datetime.date.today()
    date = start_date

    attempt = Attempt()
    attempt.user_id = user_id
    attempt.project_id = project.id
    attempt.start_date = start_date
    attempt.name = user.name + "\'s " + project.name
    attempt.cohort_id = cohort_id
    success = attempt.save()
    if not success:
        print("unable to add project. Check the IDs and try again.")
        return
    
    for day_id in project.days:
        day = day_service.get_day_from_id(day_id)
        attempt_day = AttemptDay()
        attempt_day.user_id = user_id
        attempt_day.attempt_id = attempt.id
        attempt_day.ordinal = day.ordinal
        attempt_day.scheduled_date = date
        attempt_day.project_id = project.id
        attempt_day.day_id = day.id
        success = attempt_day.save()
        if not success:
            print("unable to add attempt day. Check the IDs and try again.")
            return
        success = Attempt.objects(id=attempt.id).update_one(push__attempt_days=attempt_day.id)
        if not success:
            return
        date = date + datetime.timedelta(days=1)
    
    success = attempt.save()
    if not success:
        return

    success = User.objects(id=user_id).update_one(push__attempts=attempt.id)
    if not success:
        return

        
    add_user_to_cohort(user_id,cohort_id)

    return attempt.id

def find_cohort(project_id):
    cohort = Cohort.objects().filter(project_id=project_id,status=1).first()
    if not cohort:
        cohort = Cohort()
        cohort.project_id = project_id
        cohort.save()
    return cohort.id

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

def get_day_objects(project):
    results = []
    for day_id in project.days:
        day = Day.objects(id=day_id).first()
        results.append(day)
    return results


##############################################################

def _add_project_test():
    project = Project()
    project.name = "20 days of Pushups" #input("What is the name of this project? ")
    project.description = "In this project, you will do an ever increasing amount of pushups." #input("Describe this project? ")
    project.link_identifier = "20-days-of-pushups"
    project.save()

    for i in range(1,21):
        day = Day()
        day.name = "Day " + str(i)
        day.description = f"Do {i} pushups"
        day.ordinal = i
        day.est_minutes = 2
        success = day.save()
        if success:
            project.days.append(day.id)

    project.save()

    project2 = Project()
    project2.name = "25 days of Python" #input("What is the name of this project? ")
    project2.description = "In this project, you will code a cool app" #input("Describe this project? ")
    project2.link_identifier = "25-days-of-python"
    project2.save()

    for i in range(1,26):
        day = Day()
        day.name = "Day " + str(i)
        day.description = f"Code for {3*i} minutes"
        day.ordinal = i
        day.est_minutes = 3*i
        success = day.save()
        if success:
            project2.days.append(day.id)

    project2.save()

def _add_user_attempt_test(user):
    add_project_to_user(user, "20-days-of-pushups")


