# Class Logo(Label)
```
class Logo(Label):
	def __init__(self) -> None:
	super().__init__(LOGO, classes="title")
```

We Made a Custom Class Named Logo, wich is a Defined as a Label like in the Brackets. with that `yield Logo()` is now Possible as an widget.

# __init__
```
def __init__(self) -> None:
```
`___init__` is the Constructor of a Python Class.
It gets Automaticly executet when the Object gets used.

# super()
super takes the Parent Class. That would be Label, so the Code would be
```
Label.__init__(...)
```

The
```
(LOGO, classes="title")
```
would be:
```
Label( LOGO, classes="title" )
```

The full Line is:
```
Label.__init__Label( LOGO, classes="title" )
```