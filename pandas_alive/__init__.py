from .plot import plot,AnimatedAccessor
from .base import load_dataset

# Register animated_plot accessor for Pandas DataFrames and Series:
import pandas as pd
from pandas.core.accessor import CachedAccessor

plot_animated = CachedAccessor("plot_animated", AnimatedAccessor)
pd.DataFrame.plot_animated = plot_animated
pd.Series.plot_animated = plot