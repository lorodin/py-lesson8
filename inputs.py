def f(title, positive_only = False, exit_if_error = True):
    try:
        val = float(input(f"Input {title}: "))
        if val > 0 or not positive_only:
            return val
        else:
            print(f"{title} must be only positive number")
    except ValueError:
        print(f"'{title}' must be only number")
    if exit_if_error:
        exit()


def i(title, positive_only = False, exit_if_error = True, validate_cb = None, error_message = "Invalid value"):
    try:
        validate_cb = validate_cb if validate_cb is not None else lambda x: x > 0 if positive_only else True
        val = int(input(f"Input {title}: "))
        if validate_cb(val):
            return val
        else:
            print(error_message)
    except ValueError:
        print(f"'{title}' must be only integer number")
    if exit_if_error:
        exit()


def s(title, not_empty = False, exit_if_error = True, validate_cb = None, error_message = "Invalid value"):
    validate_cb = validate_cb if validate_cb is not None else lambda s: s != '' if not_empty else True
    val = input(f"Input {title}: ")
    val = val.strip()
    if validate_cb(val):
        return val
    print(error_message)
    if exit_if_error:
        exit()

