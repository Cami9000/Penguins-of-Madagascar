## Feature Selection - Decision Process
To determine the most relevant features for classifying penguin species, we applied multiple feature selection techniques:
- **Mutual Information**: Identified features with the highest information gain.
- **Recursive Feature Elimination (RFE)**: Selected the most relevant features by iteratively removing the least important ones.
- **Random Forest Feature Importance**: Evaluated feature contributions using a tree-based model.
- **Permutation Importance**: Measured feature impact by shuffling values.

Based on these analyses, we selected the following final features:
- bill_length_mm
- flipper_length_mm
- bill_depth_mm

The feature `body_mass_g` and `island_id` was removed, as it was not consistently important across methods.


