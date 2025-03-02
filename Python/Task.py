#Class to model Tasks that are store in the Task database
class Task:
    def __init__(self, ID, Title, Description, Progress):
        self.ID = ID
        self.Title = Title
        self.Description = Description
        self.Progress = Progress
    
    #Add __str__() function to return Task objects in json format
