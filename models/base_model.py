#!/usr/bin/python3
import uuid  # Importing the uuid module for generating unique identifiers
import datetime  # Importing the datetime module for handling date and time
import models  # Importing the 'models' module which likely contains a storage interface


class BaseModel:
    """Class representing a base model with common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with either provided attributes or generates default ones.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime.datetime): Date and time of instance creation.
            updated_at (datetime.datetime): Date and time of instance update.
        """
        if kwargs:  # If keyword arguments are provided
            self.name = kwargs["name"]  # Assigning name if provided
            self.id = kwargs["id"]  # Assigning id if provided
            self.created_at = kwargs["created_at"]  # Assigning created_at if provided
            self.updated_at = kwargs["updated_at"]  # Assigning updated_at if provided
        else:  # If no keyword arguments provided, create default attributes
            self.id = str(uuid.uuid4())  # Generating a new unique id
            self.created_at = datetime.datetime.now()  # Setting creation time
            # Setting update time to creation time if 'created_at' is True, else using creation time
            self.updated_at = (
                datetime.datetime.now() if self.created_at is True else self.created_at
            )

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute and saves the instance to storage.
        """
        self.updated_at = datetime.datetime.now()  # Updating 'updated_at' attribute
        models.storage.save()  # Saving the instance to storage using models module

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Returns:
            dict: Dictionary containing instance attributes.
        """
        new_dict = dict(self.__dict__)  # Creating a copy of instance dictionary
        new_dict["__class__"] = (
            self.__class__.__name__
        )  # Adding class name to dictionary
        new_dict["created_at"] = (
            self.created_at.isoformat()
        )  # Converting created_at to ISO format
        new_dict["updated_at"] = (
            self.created_at.isoformat()
        )  # Converting updated_at to ISO format
        return new_dict  # Returning the dictionary
