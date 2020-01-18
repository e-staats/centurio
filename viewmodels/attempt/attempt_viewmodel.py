from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
import centurio.services.attempt_services as attempt_service


class AttemptViewModel(ViewModelBase):
    def __init__(self, attempt_id: str):
        super().__init__()
        self.attempt_id = attempt_id
        self.attempt = None
        if attempt_id:
            self.attempt_id = attempt_id.strip().lower()
            self.attempt = attempt_service.get_attempt_from_id(attempt_id)


