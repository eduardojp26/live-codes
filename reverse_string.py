def reverse_string(original_string):
    #1. base case
    if len(original_string) == 0 or len(original_string) == 1:
        return original_string
    # 2. recurrence relation
    return reverse_string(original_string[1:]) + original_string[0]

if __name__ == '__main__':
    string = input()
    reversed_string = reverse_string(string)
