import sys
import time
from funcs import SortIntLines, strip_string


class UniqueInt:
    def processFile(file_lines):
        output_list = []
        for line in file_lines:
            raw_line = strip_string(line)

            try:
                processed_line = int(raw_line)
                if processed_line not in output_list:
                    output_list += [processed_line]
            except Exception as e:
                continue

        return output_list

    def ReadAndWriteToFile(input_file_name):
        processed_data = []

        try:
            with open(input_file_name, 'r') as input_file:
                raw_data = input_file.readlines()

                processed_data = UniqueInt.processFile(raw_data)
                SortIntLines(processed_data)

        except FileNotFoundError:
            print(f"No such file or directory: {input_file_name}")
            return

        output_file_name = input_file_name[:-3] + 'txt_results.txt'

        with open(output_file_name, 'w') as output_file:
            for line in processed_data:
                output_file.write(f'{line}\n')


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("No file name provided")
        print("Usage: python -u UniqueInt.py")
    else:
        start_time = time.time()
        file_name = sys.argv[1]
        strip_string(file_name)
        UniqueInt.ReadAndWriteToFile(file_name)
        end_time = time.time()

        print(f"Elapsed time: {end_time - start_time} seconds")
