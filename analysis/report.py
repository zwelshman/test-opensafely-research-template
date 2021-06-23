import pandas as pd
import seaborn as sns

data = pd.read_csv("output/input.csv")

fig = sns.catplot(
    data=data, kind="bar", x="death_category", y="patient_id", hue="sex"
)

fig.savefig("output/descriptive.png")