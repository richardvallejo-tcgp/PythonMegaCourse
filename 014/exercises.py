if __name__ == "__main__":
    print("Surprise!")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet_part = float(parts[0])
    inches_part = float(parts[1])
    inches_total = inches_part + (feet_part * 12)
    feet_total = inches_total / 12
    return {"feet": feet_part, "inches": inches_part, "feet_total": feet_total, "inches_total": inches_total}


def convert(us_std):
    meters = us_std["inches_total"] * 0.0254
    return meters


def check_height(metric_height, requirement = 1):
    eval = ""

    if metric_height < requirement:
        eval = "Yer too small, kid!"
    else:
        eval = "Get on the ride already!"

    return eval


FREEZE_POINT = 0
BOIL_POINT = 100

def check_state(temp):
    state = "Liquid"
    if temp >= BOIL_POINT:
        state = "Gas"
    elif temp <= FREEZE_POINT:
        state = "Solid"
    
    return state


def count(phrase):
    return phrase.count('.')