Show how to pass custom data to a (modal) screen.

(Modal) Screens are regular Python objects so you can customise them on instantiation.

Define `YesOrNo.__init__` to accept a parameter `question`.
Use `question` inside `YesOrNo.compose`.
Provide `question` when instantiating `YesOrNo`.
