Show that compute methods get called when other reactives change.
The compute method kicks in to compute the new value, which is then assigned.
Only then do watch methods trigger.

Start with the basic app layout but with the RGB colour components disconnected from the final static that will show the colour.
