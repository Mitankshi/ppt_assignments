def compress(chars):
    read = write = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[read]:
            count += 1
        else:
            chars[write] = chars[read]
            write += 1

            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1

            count = 1
            read = i

    chars[write] = chars[read]
    write += 1

    if count > 1:
        count_str = str(count)
        for digit in count_str:
            chars[write] = digit
            write += 1

    return write

chars = ["a","a","b","b","c","c","c"]
print(compress(chars=chars))