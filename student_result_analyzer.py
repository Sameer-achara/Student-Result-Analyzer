import pandas as pd
import matplotlib.pyplot as plt
import emoji
df = pd.read_csv("C:\\Users\\DELL\\Downloads\\marks.csv")
print(emoji.emojize("---------Mean Of The All Subjects:bar_chart:---------\n"))
print("Average Marks in Maths:", df["Math"].mean())
print("Average Marks in Science:", df["Science"].mean())
print("Average Marks in CS:", df["CS"].mean())
print("Average Marks in English:", df["English"].mean())
print("Average Marks in Hindi:", df["Hindi"].mean())
print(emoji.emojize("\n---------Highest Of The All Subjects:trophy::fire:---------\n"))
print("Highest Marks in Maths:", df["Math"].max())
print("Highest Marks in Science:", df["Science"].max())
print("Highest Marks in CS:", df["CS"].max())
print("Highest Marks in English:", df["English"].max())
print("Highest Marks in Hindi:", df["Hindi"].max())
print(emoji.emojize("\n---------Lowest Of The All Subjects:warning::stop_sign:---------\n"))
print("Lowest Marks in Maths:", df["Math"].min())
print("Lowest Marks in Science:", df["Science"].min())
print("Lowest Marks in CS:", df["CS"].min())
print("Lowest Marks in English:", df["English"].min())
print("Lowest Marks in Hindi:", df["Hindi"].min())
df["Total"] = df[["Math", "CS", "English","Hindi","Science"]].sum(axis=1)
df["Percentage"] = (df["Total"] / (5*100)) * 100
def check_fail_pass(Percentage):
    if(Percentage>75):
        return "Pass"
    else:
        return "Fail"
df["Result"]=df["Percentage"].apply(check_fail_pass)
topper = df.loc[df["Percentage"].idxmax()]
last_rank = df.loc[df["Percentage"].idxmin()]

print(emoji.emojize("\n---------Ranking:first_place_medal---------\n"))
print("Class Topper is", topper["Name"], "with", topper["Percentage"],"%")
print("Last Rank is", last_rank["Name"], "with", last_rank["Percentage"],"%")

def grade(Percentage):
   if Percentage >= 80:
    return "A"
   elif Percentage >= 75:
    return "B"
   elif Percentage >= 60:
    return "C"
   else:
    return "D"
   
print(emoji.emojize("\n------------Subject-Wise Toppers:books::crown:----------\n"))   
df["Grade"]=df["Percentage"].apply(grade)
math_topper=df.loc[df["Math"].idxmax()]
print("Math Topper is",math_topper["Name"],"with",math_topper["Math"],"marks")
Science_topper=df.loc[df["Science"].idxmax()]
print("Science Topper is",Science_topper["Name"],"with",Science_topper["Science"],"marks")
English_topper=df.loc[df["English"].idxmax()]
print("English Topper is",English_topper["Name"],"with",English_topper["English"],"marks")
Cs_topper=df.loc[df["CS"].idxmax()]
print("CS Topper is",Cs_topper["Name"],"with",Cs_topper["CS"],"marks")
Hindi_topper=df.loc[df["Hindi"].idxmax()]
print("Hindi Topper is",Hindi_topper["Name"],"with",Hindi_topper["Hindi"],"marks")

# ---------------- Final DataFrame ----------------
print(emoji.emojize("\n----------Final-List:memo::clipboard:----------\n"))
print(df)

# ---------------- Save to Excel ----------------
 df.to_excel(r"C:\Users\DELL\Downloads\final_results2.xlsx", index=False)

