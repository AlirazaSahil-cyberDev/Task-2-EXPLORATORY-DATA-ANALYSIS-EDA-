# All visualizations ek folder mein save karo

import os
os.makedirs('eda_visualizations', exist_ok=True)

# Save all plots
plots = [
    'univariate_analysis.png',
    'bivariate_analysis.png', 
    'correlation.png',
    'outliers.png'
]

for plot in plots:
    if os.path.exists(plot):
        os.rename(plot, f'eda_visualizations/{plot}')

print("✅ All visualizations saved!")