from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt


def plot_csv(path: Path) -> None:
    df = pd.read_csv(path)
    plt.plot(df["time"], df["value"])
