# temporary dictionary context demo module

shallowmodifydict is a mini module demo containing a class for temporarily
modifying a dictionaries' keys setup as a context manager.

## Installation
No need for any package manager, a simple copy paste of the module file
contents `shallowmodifydict.py` or clone of this git repository will do.

## Usage
import the class from the module and use as you do with a context manager.
``` python
from shallowmodifydict import ShallowModifyDict

# create dictionary
my_dict = {'a': 1, 'b': {'bb': 22}, 'c': 3}

# example usage a
with ShallowModifyDict(my_dict, {'a': -1, 'b': -2, 'd': -4}):
    # my_dict is modified with new values and key at this point
    print(my_dict)
# my_dict is reverted to original state as first declared
print(my_dict)

# example usage b
with ShallowModifyDict(my_dict, {'a': -1, 'b': -2, 'd': -4}) as tmp_dict:
    # tmp_dict is a reference to the modified my_dict
    print(tmp_dict)
# my_dict is reverted to original state as first declared
print(my_dict)
```

## Limitations
Note from the class name, this is a shallow modification of dictionary, which
means that we cannot just modify a single sub-key of a key, as it will
overwrite the key to contain just the temporary sub-key and value you provided.

## Attribution
This implementation is modified from
[a stackoverflow question](https://codereview.stackexchange.com/questions/128985/dictionary-as-context-manager)

Original Author: [MSeifert](https://codereview.stackexchange.com/users/86014/mseifert)

## License
[MIT](LICENSE)
