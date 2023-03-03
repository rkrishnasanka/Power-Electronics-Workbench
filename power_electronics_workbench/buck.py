def buck_min_inductance(
    v_out: float, v_in: float, time_period: float, i_load: float
) -> float:
    """Calculates the minimum inductance required for the given Buck converter.

    Args:
        v_out (float): The output voltage of the Buck converter.
        v_in (float): The input voltage of the Buck converter.
        time_period (float): The time period of the Buck converter.
        i_load (float): The load current of the Buck converter.

    Returns:
        float: The minimum inductance required for the Buck converter.
    """
    duty_cycle = v_out / v_in
    min_inductance = (v_in - v_out) * duty_cycle * time_period / (2 * i_load)
    return min_inductance
