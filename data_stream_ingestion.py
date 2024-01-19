class DataStream:
    def __init__(self):
        """
        Initializes empty dictonary to store docstring and timstamp data.
        """
        self.data_dict = {}

    def should_output_data_str(self, timestamp, data_string):
        """
        Determines whether a data string should be output based on its timestamp.

        Parameters:
            timestamp (int): The timestamp of the data string.
            data_string (str): The data string to be processed.

        Returns:
            bool: True if the data string should be output, False otherwise.
        """
        if data_string not in self.data_dict or timestamp - self.data_dict[data_string]>=5:
            self.data_dict[data_string] = timestamp
            return True
        else:
            return False

