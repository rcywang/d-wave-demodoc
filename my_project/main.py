"""
It contains some NumPy style docstrings to be picked up by the *autodoc* directive.
"""



def about_me(your_name):
    """
    Return the most important thing about a person.


    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """
    return "{} is a LaTeX enthusiast.".format(your_name)



class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
        Initialization

        Parameters
        ----------
        name
            A string to assign the `name` instance attribute.

        """
        self.name = name


    
    def about_self(self):

        """
        Return information about an instance created from ExampleClass.
        """
        return "I am a very smart {} object.".format(self.name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()