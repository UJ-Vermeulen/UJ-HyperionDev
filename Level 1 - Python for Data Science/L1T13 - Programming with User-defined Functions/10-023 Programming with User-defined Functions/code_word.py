"""
This program demonstrates the use of dictionaries in Python to handle codewords
and call corresponding functions based on the codeword received.

Imagine we have a long list of codewords and each codeword triggers
a specific function to be called.
For example, the codeword 'go' which calls the function handle_go,
and another codeword 'ok' which calls the function handle_ok.
We can use a dictionary in Python to encode this.
A dictionary in Python is a collection of key-value pairs,
where each key is unique and maps to a specific value.
"""


def handle_go(x):
    """
    Handles the codeword 'go'.

    Args:
    x (str): Argument to be handled along with 'go'.

    Returns:
    str: A message indicating the handling of 'go'.
    """

    return "Handling a go! " + x


def handle_ok(x):
    """
    Handles the codeword 'ok'.

    Args:
    x (str): Argument to be handled along with 'ok'.

    Returns:
    str: A message indicating the handling of 'ok'.
    """

    return "Handling an ok! " + x


# Dictionary that pairs codewords (strings) to functions.
codewords = {
    "go": handle_go,  # Maps the string 'go' to handle_go function.
    "ok": handle_ok,  # Maps the string 'ok' to handle_ok function.
}

# Now, we see a codeword given to us:
codeword = "go"  # Feel free to change to 'ok', to see how the output.

# Check if the given codeword exists in the 'codewords' dictionary.
if codeword in codewords:
    # If the codeword exists, call the corresponding function
    # with an argument ("add_argument") and store the result in 'answer'.
    answer = codewords[codeword]("add_argument")  # Try changing 'add_argument'

    # Print the result.
    print(answer)
else:
    # If the codeword doesn't exist in the dictionary, print an error message.
    print("I don't know that codeword.")
