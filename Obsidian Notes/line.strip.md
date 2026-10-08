```
new_options = [line for line in output.splitlines() if line.strip()] #AI
```

line.strip: removes Spaces if its empty its FALSE
if line.strip: checks if the Line is TRUE and if not it removes it

## Why line for line in output.splitlines()?

The Output Variables has a Line for each character.

So `for line in output.splitlines()` would check every character.
But line for line in output.splitlines() checks where the actual Line ends and puts them together.