"""Take in a cell phone number and the phone's carrier service
(e.g., Verizon, AT&T) and convert them into a cell phone email
address."""

import string

def transform_cell_number(number, carrier):
    """Main function; take number and carrier
    and return cell phone email address"""
    carrier_domains = {
        'att': '@txt.att.net',
        'boost': '@sms.myboostmobile.com',
        'sprint': '@messaging.sprintpcs.com',
        'tmobile': '@tmomail.net',
        'verizon': '@vtext.com',
        'virgin': '@vmobl.com'
    }
    carrier_formatted = _standardize_carrier(carrier)
    return str(number) + carrier_domains[carrier_formatted]


def _standardize_carrier(carrier):
    """Turn carrier names into lowercase,
    remove extraneous characters and words"""
    carrier_lower = carrier.lower()
    replacement_values = [
        *string.punctuation,
        ' ',
        'mobile',
        'wireless',
    ]
    for i in replacement_values:
        if i in carrier_lower:
            carrier_lower = carrier_lower.replace(i, '')
    return carrier_lower
