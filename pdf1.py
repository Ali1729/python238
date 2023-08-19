import pandas as pd

data = {
  "calories": [420, 380, 390,None],
  "duration": [50, 40, 45,None]
}

data1 = {
  "calories": [421, 380, 390,343,None],
  "duration": [50, 40, 45,56,None]
}
data = pd.DataFrame(data)
data1 = pd.DataFrame(data1)

# pdf = pd.DataFrame("calories","duration")
pdf = pd.DataFrame()


pdf = pd.concat([data,data1],ignore_index=True)
print(pdf)
pdf = pdf.drop_duplicates(ignore_index=True,keep="first")

print(pdf)