

def generic_model_mutation_process(model, data, id=None, commit=True):
    """
    Modify a Database item or creates it if it doesn't exist :

    - If there is ID, gets the related item from the database 
    Tries to delete the id attribute from the data dictionary
    Set the data values to the field of the item using a for loop
    - If there is no ID, creates a new Item using the data

    Finally saves the object back to the database 
    """

    if id:
        # get item
        item = model.objects.get(id=id)
        # set the value of field to value of the item object
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        # Creates the object using the data
        item = model(**data)

    if commit:
        # saves the object back to the database
        item.save()

    return item
