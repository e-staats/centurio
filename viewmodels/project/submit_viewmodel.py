import sys
import os
from centurio.viewmodels.shared.viewmodel_base import ViewModelBase
import centurio.services.user_services as user_service

class SubmitViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.title = self.request_dict.title
        self.description = self.request_dict.description
        self.day_1 = self.request_dict.sample_day_1
        self.day_2 = self.request_dict.sample_day_2
        self.day_3 = self.request_dict.sample_day_3


    def validate(self):
        if not self.title or not self.title.strip():
            self.error = "You must specify an title"
        elif not self.description or not self.description.strip():
            self.error = "You must specify a description"

