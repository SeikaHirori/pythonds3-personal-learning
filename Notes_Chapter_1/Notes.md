
<h1> Activity 1.13.2 </h1>

- builtins.input VS sys.stdin:
    - Link: https://stackoverflow.com/a/65048163
    - TL;DR:
        - input() is a function
        - sys.stdin is an object (file object)

        - For my needs, using input() and Pytest works for needing to put multiple inputs.

- Mocker | using builtin AND Pytest-mocker
    - https://stackoverflow.com/questions/56498487/how-can-i-test-a-loop-with-multiple-input-calls/56498519#56498519


- NOR gate: 
    - https://en.wikipedia.org/wiki/NOR_gate
    - My understanding: 
        if a = 0 && b = 0:
            output = 1
        else:
            ouput = 0

- NAND gate:
    - https://en.wikipedia.org/wiki/NAND_gate
        - My understanding:
            if a = 1 && b = 1:
                output = 0
            else:
                output = 1
- Importing a file/class from another folder: https://stackoverflow.com/a/456491
    - Create a blank "__init__.py" file to do this.