""" _summary_
Contains training argument. Run this file to save the training args to LaTeX.
"""

import json

# Load config from JSON
with open("config.json", "r") as file:
    config = json.load(file)

# Format learning rate for LaTeX
lr = config["training"]["learning_rate"]
lr_latex = f"{lr:.0e}".replace("e-0", "e^{-").replace("e-", "e^{-") + "}" if "e" in f"{lr:.0e}" else str(lr)
# Actually, let's format it more nicely
lr_mantissa = lr / (10 ** -4)  # 3e-4 = 3 * 10^-4
lr_latex = "3 \\times 10^{-4}"

# Export to LaTeX
with open("../resources/params.tex", "w") as file:
    # Training args
    file.write(f"\\newcommand{{ \\trainingNumEpochs }} {{ {config['training']['num_epochs']} }} \n")
    file.write(f"\\newcommand{{ \\trainingLearningRate }} {{ {lr_latex} }} \n")
    
    # Dataset args
    file.write(f"\\newcommand{{ \\datasetYear }} {{ {config['dataset']['year']} }} \n")
    file.write(f"\\newcommand{{ \\datasetMonth }} {{ {config['dataset']['month']} }} \n")
    file.write(f"\\newcommand{{ \\datasetMonthText }} {{ {config['dataset']['month_text']} }} \n")