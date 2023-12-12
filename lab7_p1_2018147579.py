import re

def find_functions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    function_declarations = {}
    function_calls = {}

    # Regular expression patterns
    declaration_pattern = r'def\s+(\w+)\('
    call_pattern = r'(\w+)\('

    # Find declarations and calls
    for i, line in enumerate(lines, 1):
        # Check for function declaration
        declaration_match = re.search(declaration_pattern, line)
        if declaration_match:
            func_name = declaration_match.group(1)
            function_declarations[func_name] = i

        # Check for function calls
        call_matches = re.finditer(call_pattern, line)
        for match in call_matches:
            func_name = match.group(1)
            function_calls.setdefault(func_name, []).append(i)

    return function_declarations, function_calls

def main():
    # Assuming the file 'input_7_1.txt' is in the same directory
    declarations, calls = find_functions("input_7_1.txt")

    # Output the results
    for func in declarations:
        print(f"{func}: def in {declarations[func]}, calls in {calls.get(func, [])}")

if __name__ == "__main__":
    main()
