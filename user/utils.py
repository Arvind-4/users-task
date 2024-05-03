import re
from .models import Manager


def validate_full_name(full_name):
    if not full_name:
        return "Full name is required."
    return None


def validate_mob_num(mob_num):
    mob_num = mob_num.replace("+91", "").replace("0", "")
    if not mob_num.isdigit() or len(mob_num) != 10:
        return "Invalid mobile number."
    return mob_num


def validate_pan_num(pan_num):
    pattern = r"^[A-Z]{5}\d{4}[A-Z]$"
    if not re.match(pattern, pan_num.upper()):
        return "Invalid PAN number."
    return pan_num.upper()


def validate_manager_id(manager_id):
    try:
        manager = Manager.objects.get(manager_id=manager_id)
    except Manager.DoesNotExist:
        return False
    return True


def validate_data(data):
    error = {}

    full_name = data.get("full_name")
    full_name_error = validate_full_name(full_name)
    if full_name_error:
        error["full_name"] = full_name_error

    mob_num = data.get("mob_num")
    mob_num_error = validate_mob_num(mob_num)
    if mob_num_error:
        error["mob_num"] = mob_num_error
    else:
        data["mob_num"] = mob_num_error

    pan_num = data.get("pan_num")
    pan_num_error = validate_pan_num(pan_num)
    if pan_num_error:
        error["pan_num"] = pan_num_error
    else:
        data["pan_num"] = pan_num_error

    manager_id = data.get("manager_id")
    if manager_id and not validate_manager_id(manager_id):
        error["manager_id"] = "Invalid manager ID."

    if error:
        return {"error": error}

    return data
