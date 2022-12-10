def target_string_count(s, target):
    #1. base case
    # s "at" target "cat"
    if len(s) < len(target):
        return 0

    #2. recurrence relation 
    if s[0: len(target)] == target:
        return 1 + target_string_count(s[1:], target)
    else:
        return target_string_count(s[1:], target)

def sum_element(a_list):
    if len(a_list) == 0:
         return 0
    return a_list[0] + sum_element(a_list[1:])

def main():
    s, target=input()
    print(target_string_count(s,target))


if __name__ == '__main__':
    main()