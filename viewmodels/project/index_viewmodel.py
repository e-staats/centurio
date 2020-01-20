from centurio.viewmodels.shared.viewmodel_base import ViewModelBase

class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        if  'link_identifier' in self.request_dict:
            self.link_identifier =  self.request_dict['link_identifier']
