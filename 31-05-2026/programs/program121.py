def return_only_integer(lst):
# Use list comprehension to filter out integers
   return [x for x in lst if isinstance(x, int) and not isinstance(x, int)]
