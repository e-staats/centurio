from centurio.services import project_services
from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
from centurio.data.projects import Project
# pylint: disable=no-member

class ProjectDetailsViewModel(ViewModelBase):
    def __init__(self, project_link_id: str):
        super().__init__()
        self.project_link_id = project_link_id
        self.project = None
        if project_link_id:
            self.project_link_id = project_link_id.strip().lower()
            self.project = project_services.get_project_from_link_id(project_link_id)
        self.project_days = project_services.get_day_objects(self.project)