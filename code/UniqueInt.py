import sys
import time


class IntegerProcessor:

    def __init__(self, strip_function, sort_function):
        self.strip_function = strip_function
        self.sort_function = sort_function

    def process_file(self, file_lines):
        unique_integers = []
        for line in file_lines:
            stripped_line = self.strip_function(line)
            try:
                processed_integer = int(stripped_line)
                if processed_integer not in unique_integers:
                    unique_integers.append(processed_integer)
            except ValueError:
                # Skip non-integer lines
                pass

        return self.sort_function(unique_integers)

    def read_and_write_to_file(self, input_file_name):
        try:
            with open(input_file_name, 'r') as input_file:
                raw_data = input_file.readlines()
            processed_data = self.process_file(raw_data)
        except FileNotFoundError:
            print(f"No such file or directory: {input_file_name}")
            return

        output_file_name = f"{input_file_name[:-3]}txt_results.txt"
        with open(output_file_name, 'w') as output_file:
            for integer in processed_data:
                output_file.write(f"{integer}\n")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("No file name provided")
        print("Usage: python -u IntegerProcessor.py <filename>")
    else:
        start = time.time()
        file_name = sys.argv[1]
        processor = IntegerProcessor(strip_function=lambda x: x.strip(), sort_function=sorted)
        processor.read_and_write_to_file(file_name)
        end = time.time()

        print(f"Time Used: {end - start} seconds")
