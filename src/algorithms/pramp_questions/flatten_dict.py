def flatten_dictionary(dictionary):
    output = {}
    get_flattened_dict("", dictionary, output)
    return output


def get_flattened_dict(prev_key, value, output):
    # base case: found a int or string
    if type(value) is not dict:
        output[prev_key] = str(value)
        return

    # recurse on dictionary
    for next_key, v in value.items():
        if prev_key == "":
            new_key = next_key
        elif next_key == "":
            new_key = prev_key
        else:
            new_key = prev_key + "." + next_key
        get_flattened_dict(new_key, v, output)

    return
