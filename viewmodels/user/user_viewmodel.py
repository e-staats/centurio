from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
import centurio.services.day_services as day_service


class UserViewModel(ViewModelBase):
    def __init__(self, user_id: str):
        super().__init__()
        self.user_id = user_id




