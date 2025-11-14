

def get_all_add_on_names(ADD_ON_CLASS):

    add_on_names = [
        getattr(ADD_ON_CLASS, attr)
        for attr in dir(ADD_ON_CLASS)
        if not attr.startswith('_') and isinstance(getattr(ADD_ON_CLASS, attr), str)
    ]
    return add_on_names