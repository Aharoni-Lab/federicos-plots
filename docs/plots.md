---
file_format: mystnb
mystnb:
    output_stderr: remove
    render_text_lexer: python
    render_markdown_format: myst
myst:
    enable_extensions: ["colon_fence"]
---

# Plots

## Example Plot

```{code-cell}
---
tags: [hide-cell]
---

from pathlib import Path
from federicos_plots.demo import plot_csv
```

```{code-cell}
plot_csv(Path('../data/demo.csv'))
```