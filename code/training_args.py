""" _summary_
Contains training argument. Run this file to save the training args to LaTeX.
"""

from datetime import datetime
from dotenv import load_dotenv

training_args = {
	"NumEpochs": "3",
	"LearningRate": "3 \\times 10^{-4}"
}

ds_date = datetime(2015, 5, 1)

dataset_args = {
	"Year": str(ds_date.year),
	"Month": str(ds_date.month),
	"MonthText": ds_date.strftime("%B")
}

with open("../resources/params.tex", "w") as file:
    for key, val, in training_args.items():
        file.write(f"\\newcommand{{ \\training{key} }} {{ {val} }} \n")
        
    for key, val, in dataset_args.items():
        file.write(f"\\newcommand{{ \\dataset{key} }} {{ {val} }} \n")