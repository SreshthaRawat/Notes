TypeError: 'int' object is not iterable
                   ^^^^^^^^^^^^^^^^^^^^
    for ind,val in enumerate(len(nums)):


# so len(nums) returns an integer but enumerate() needs something it can 
# loop over (an iterable) like a list, string, or range.
# You can’t loop over a plain number (i.e. 4)