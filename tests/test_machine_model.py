from laser.models.machine import MachineModel, ControllerState


def test_machine_model_default_state():
    model = MachineModel()

    assert model.controller_state == ControllerState.OFF
    assert not model.connected
    assert model.digital_inputs.shutter_closed
    assert not model.digital_outputs.laser_cmd
    assert model.analog_inputs.temperature == 25.0
    assert model.analog_outputs.power_setpoint == 0.0
