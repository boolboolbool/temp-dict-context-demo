class ShallowModifyDict(object):
    """
        Context manager class to make temporary changes to dictionary values
        within the context manager
        
        Note that this is a shallow operation in the sense that
        sub-dictionaries must be updated as a whole

        Example usage
        -------------
        >>> my_dict = {'key_1': 'old val'}
        >>> with ShallowModifyDict(my_dict, {'key_1': 'new val'}):
        ...     # my_dict now has key 'key_1' modified
        ...     print(my_dict['key_1'])
        'new val'
        ... # upon exiting context manager, revert back to original values
        >>> print(my_dict['key_1'])
        'old val'
    """
    def __init__(self, dictionary, tmp_kvs):
        """
            Initialise dictionary context

            :param dict dictionary: The dictionary to be temporarily modified
            :param dict tmp_kvs: A dictionary whose keys are a subset of
                                 :data:`dictionary` and their temporary
                                 modified values
        """
        self._dictionary = dictionary
        self._tmp_kvs = tmp_kvs

        # keep track of original key value pairs changed
        self._og_kvs = {}
        for key in tmp_kvs:
            if key in dictionary:
                self._og_kvs[key] = dictionary[key]
    def __enter__(self):
        """
            On entering context, update dictioanry with temporary key values
        """
        self._dictionary.update(self._tmp_kvs)
        return self._dictionary
    def __exit__(self, exc_type, exc_value, traceback):
        """
            On leaving context, revert dictionary to original sate, pre-context
        """
        self._dictionary.update(self._og_kvs)
