# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

#changing the input to see if the output is different.
print(mean_var_std.calculate([1,2,3,4,5,6,7,8,9]))

# Run unit tests automatically
main(module='test_module', exit=False)