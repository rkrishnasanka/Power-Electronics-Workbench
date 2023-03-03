from typing import Tuple


def boost_avg_inductor_current(v_out: float, v_in: float, i_load: float) -> float:
    """Calculates the average current seen over the inductor for the basic Boost architecture.

    Args:
        v_out (float): The output voltage of the Boost converter.
        v_in (float): The input voltage of the Boost converter.
        i_load (float): The load current of the Boost converter.

    Returns:
        float: The value of the average current seen over the inductor.
    """
    avg_i_inductor = i_load * v_out / v_in
    return avg_i_inductor


def boost_delta_load_current(
    v_in: float, duty_cycle: float, time_period: float, inductance: float
) -> float:
    """Calculates the change in load current over the inductor for the basic Boost architecture.

    Args:
        v_in (float): The input voltage of the Boost converter.
        duty_cycle (float): The duty cycle of the Boost converter.
        time_period (float): The time period of the Boost converter.
        inductance (float): The inductance of the Boost converter.

    Returns:
        float: The change in load current over the inductor.
    """
    delta_i_load = v_in * duty_cycle * time_period / inductance
    return delta_i_load


def boost_duty_cycle(v_out: float, v_in: float) -> float:
    """Calculates the duty cycle based on the input and output voltages of the Boost converter.

    Args:
        v_out (float): The output voltage of the Boost converter.
        v_in (float): The input voltage of the Boost converter.

    Returns:
        float: The duty cycle of the Boost converter.
    """
    dutycycle = (v_out - v_in) / v_out
    return dutycycle


def boost_min_inductance(
    v_in: float, duty_cycle: float, time_period: float, i_load: float
) -> float:
    """Calculates the minimum inductance required for the given Boost converter.

    Args:
        v_in (float): The input voltage of the Boost converter.
        duty_cycle (float): The duty cycle of the Boost converter.
        time_period (float): The time period of the Boost converter.
        i_load (float): The load current of the Boost converter.

    Returns:
        float: The minimum inductance required for the Boost converter.
    """
    L_min = v_in * duty_cycle * time_period / (2 * i_load)
    return L_min


def boost_ripple_current(
    v_in: float, duty_cycle: float, time_period: float, inductance: float, i_load: float
) -> Tuple[float, float]:
    """Calculates the maximum and minimum ripple current over the inductor for the basic Boost architecture.

    Args:
        v_in (float): The input voltage of the Boost converter.
        duty_cycle (float): The duty cycle of the Boost converter.
        time_period (float): The time period of the Boost converter.
        inductance (float): The inductance of the Boost converter.
        i_load (float): The load current of the Boost converter.

    Returns:
        Tuple[float, float]: The maximum and minimum ripple current over the inductor.
    """
    i_max = i_load + v_in * duty_cycle * time_period / (2 * inductance)
    i_min = i_load - v_in * duty_cycle * time_period / (2 * inductance)
    return i_min, i_max


def boost_ripple_voltage(
    i_load: float, duty_cycle: float, frequency: float, capacitance: float
) -> float:
    """Calculates the ripple voltage for the given Boost converter.

    Args:
        i_load (float): The load current of the Boost converter.
        duty_cycle (float): The duty cycle of the Boost converter.
        frequency (float): The switching frequency of the Boost converter.
        capacitance (float): The capacitance of the Boost converter.

    Returns:
        float: The ripple voltage for the Boost converter.
    """
    v_ripple = i_load * duty_cycle / frequency / capacitance
    return v_ripple
