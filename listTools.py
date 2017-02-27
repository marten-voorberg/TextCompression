def ListContainsItem(list, item):
    """Checks if a certain list contains a specific item. The List can also be a string"""
    for listItem in list:
        if item == listItem:
            return True

    return False
