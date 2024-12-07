def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()
    


def part_one():
    reports = get_input_lines_from_file()
    safe_report_count = 0
    for report in reports:
        levels = report.split(" ")
        levels = [int(level) for level in levels]
        fail = False
        curr = levels[0]


        # increasing
        print(report)
        if levels[1] > levels[0]:
            print("increasing")
            curr = levels[1]
            for level in levels[2:]:
                print(level, curr)
                if (level <= curr) or (abs(curr - level) > 3):
                    fail = True
                    break
                else:
                    curr = level

        # decreasing
        elif levels[1] < levels[0]:
            print("decreasing")
            curr = levels[1]
            for level in levels[2:]:
                print(level, curr)
                if (level >= curr) or (abs(level - curr) > 3):
                    fail = True
                    break
                else:
                    curr = level
        else:
            continue

        if not fail:
            safe_report_count += 1
        
        if fail:
            print("failed")
        else:
            print("passed")
    
    return safe_report_count
            

if __name__ == "__main__":
    print(part_one())