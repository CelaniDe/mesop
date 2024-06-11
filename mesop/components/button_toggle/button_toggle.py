import mesop.components.button_toggle.button_toggle_pb2 as button_toggle_pb
from mesop.component_helpers import insert_component, register_native_component


@register_native_component
def button_toggle(
  *,
  label: str,
  key: str | None = None,
):
  """
  This function creates a button_toggle.

  Args:
      label: The text to be displayed
  """
  insert_component(
    key=key,
    type_name="button_toggle",
    proto=button_toggle_pb.ButtonToggleType(
      label=label,
    ),
  )
