def pin_extractor(poems):
    """
    poems: list of poem strings
    Returns: list of secret codes (strings), one per poem
    """
    secret_codes = []                 # will store result for each poem

    for poem in poems:                # process poems one by one
        secret_code = ''              # build the code for this poem
        lines = poem.split('\n')      # split poem into lines

        # enumerate gives (line_index, line_text)
        for line_index, line in enumerate(lines):
            words = line.split()      # split the line into words

            # If the line has a word at position line_index,
            # add the length of that word as the next digit.
            # Otherwise add '0' to keep the code length consistent.
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'

        secret_codes.append(secret_code)  # save this poem's code

    return secret_codes
