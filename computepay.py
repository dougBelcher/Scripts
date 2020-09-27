def computepay(hours, rate):
    rateovr40 = rate * 0.5
    if hours >= 40:
        ovr40 = hours - 40
    else:
        ovr40 = 0
    Pay = (hours * rate) + (rateovr40 * ovr40)
    return Pay
