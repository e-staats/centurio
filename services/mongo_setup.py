import mongoengine

alias_core = 'default'
db = "centurio"

data = dict(

    )

def global_init():
    mongoengine.register_connection(alias=alias_core, name=db)