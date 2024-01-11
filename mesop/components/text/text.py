from typing import Literal

import mesop.components.text.text_pb2 as text_pb2
from mesop.component_helpers import Style, insert_component, to_style_proto
from mesop.utils.validate import validate


@validate
def text(
  text: str,
  *,
  type: Literal[
    "headline-1",
    "headline-2",
    "headline-3",
    "headline-4",
    "headline-5",
    "headline-6",
    "subtitle-1",
    "subtitle-2",
    "body-1",
    "body-2",
    "caption",
    "button",
  ]
  | None = None,
  style: Style | None = None,
  key: str | None = None,
):
  """
  Create a text component.

  Args:
      text: **Required.** The text to display.
      type: The typography level for the text.
      style: Style to apply to component. Follows [HTML Element inline style API](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style).
      key: An optional key to uniquely identify the component. Defaults to None.

  """
  # The Python and Proto enum values should be exactly 1:1
  # typography_level = cast(
  #   text_pb2.TextType.TypographyLevel.ValueType, type.value
  # )
  insert_component(
    key=key,
    type_name="text",
    proto=text_pb2.TextType(
      text=text,
      type=type,
      # typography_level=typography_level,
    ),
    style=to_style_proto(style) if style else None,
  )
