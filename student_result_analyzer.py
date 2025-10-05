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
subjects = ["Math", "Science", "CS", "English", "Hindi"]
topper_marks = [df[subjects].max() for sub in subjects]


# ---------------- Final DataFrame ----------------
print(emoji.emojize("\n----------Final-List:memo::clipboard:----------\n"))
print(df)

# ---------------- Save to Excel ----------------
# df.to_excel(r"C:\Users\DELL\Downloads\final_results2.xlsx", index=False)

co = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
    "#8c564b",  # Brown
    "#e377c2",  # Pink
    "#7f7f7f",  # Gray
    "#bcbd22",  # Olive
    "#17becf"   # Cyan
]
plt.bar(df["Name"], df["Percentage"], color="#17becf")
plt.xticks(rotation=90)
plt.title("Student Percentages")
plt.ylabel("Percentage")
plt.ylim(0, 100)
plt.show()


plt.bar(df["Name"],df["Total"], color="#1f77b4")
plt.xticks(rotation=90)
plt.title("Student Total Marks")
plt.ylabel("Total Marks")
plt.ylim(0, 500)
plt.show()

stu_grade=df["Grade"].value_counts()
plt.pie(stu_grade,labels=stu_grade.index,autopct="%1.1f%%")
plt.title("Grade Distribution of Students")
plt.show()


avg=[df["Math"].mean(),df["CS"].mean(),df["Hindi"].mean(),df["English"].mean(),df["Science"].mean()]
sub=["Math","CS","Hindi","English","Science"]
labels = [f"{sub[i]} ({avg[i]:.1f})" for i in range(len(sub))]
plt.pie(avg,labels=labels)
plt.title("Average of All Subjects")
plt.show()

avg=[df["Math"].max(),df["CS"].max(),df["Hindi"].max(),df["English"].max(),df["Science"].max()]
sub=["Math","CS","Hindi","English","Science"]
labels = [f"{sub[i]} ({avg[i]:.1f})" for i in range(len(sub))]
plt.pie(avg,labels=labels)
plt.title("Highest of All Subjects")
plt.show()


avg=[df["Math"].min(),df["CS"].min(),df["Hindi"].min(),df["English"].min(),df["Science"].min()]
sub=["Math","CS","Hindi","English","Science"]
labels = [f"{sub[i]} ({avg[i]:.1f})" for i in range(len(sub))]
plt.pie(avg,labels=labels)
plt.title("Lowest of All Subjects")
plt.show()
