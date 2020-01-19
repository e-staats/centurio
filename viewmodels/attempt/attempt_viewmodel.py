from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
import centurio.services.attempt_services as attempt_service
import centurio.services.day_services as day_service


class AttemptViewModel(ViewModelBase):
    def __init__(self, attempt_id: str):
        super().__init__()
        self.attempt_id = attempt_id
        self.attempt = None
        if attempt_id:
            self.attempt_id = attempt_id.strip().lower()
            self.attempt = attempt_service.get_attempt_from_id(attempt_id)
            self.day_descriptions = {}
            for day in self.attempt.attempt_days:
                self.day_descriptions[day.ordinal] = day_service.get_description_from_day_id(day.day_id)



