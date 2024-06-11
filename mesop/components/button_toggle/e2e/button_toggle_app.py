import mesop as me


@me.page(path="/components/button_toggle/e2e/button_toggle_app")
def app():
  me.button_toggle(label="Hello, world!")
