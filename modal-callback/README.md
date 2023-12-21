Show how to pass data back to the screen that created a modal.

Start with the code from `modal-styling`.

We start by adding IDs to the buttons and handling button presses on the screen.
We use `dismiss` to dismiss the modal screen with a Boolean value.

When pushing the screen, we specify the parameter `callback`.

Define the callback (that accepts a Boolean) and uses it to exit the app or not.
