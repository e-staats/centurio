from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
import centurio.services.attempt_services as attempt_service
import centurio.services.day_services as day_service
import centurio.services.attemptday_services as attemptday_services


class AttemptViewModel(ViewModelBase):
    def __init__(self, attempt_id: str):
        super().__init__()
        self.attempt_id = attempt_id
        self.attempt = None
        if attempt_id:
            self.attempt_id = attempt_id.strip().lower()
            self.attempt = attempt_service.get_attempt_from_id(attempt_id)
            self.attempt_days = []
            self.day_descriptions = {}
            for attempt_day_id in self.attempt.attempt_days:
                attempt_day = attemptday_services.get_attempt_day_from_id(attempt_day_id)
                self.attempt_days.append(attempt_day)
                self.day_descriptions[attempt_day.ordinal] = day_service.get_description_from_day_id(attempt_day.day_id)




