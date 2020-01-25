from centurio.data.projectsuggestions import ProjectSuggestion
from centurio.data.days import Day
from centurio.data.attempts import Attempt
from centurio.data.users import User
from centurio.data.cohorts import Cohort
from centurio.data.attemptdays import AttemptDay
import centurio.services.mongo_setup as mongo_setup
import centurio.services.day_services as day_service
import datetime
# pylint: disable=no-member


def add_project_suggestion(vm):
    mongo_setup.global_init()
    project = ProjectSuggestion()
    project.name = vm.title
    project.description = vm.description
    project.submitting_user = vm.user_id
    for day in [vm.day_1,vm.day_2,vm.day_3]:
        project.suggested_days.append(day)
    project.save()
    return True

