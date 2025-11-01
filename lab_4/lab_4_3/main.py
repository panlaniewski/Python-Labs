import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

campaign_data = pd.read_csv("entrance_campaign.csv")

# ave_certificate_score = campaign_data.groupby("admission_year")["certificate_score"].mean().sort_index()
# plt.plot(ave_certificate_score.index.astype("str"), ave_certificate_score.values, linewidth=3, marker='o')
# plt.grid(linestyle = '--', alpha=0.7)
# plt.title("Динамика среднего балла аттестата абитуриентов за 2020-2025 гг.")
# plt.xlabel("Год")
# plt.ylabel("Средний балл")
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.histplot(campaign_data["admission_score"], bins=25, color="skyblue")
# plt.title("Распределение общей суммы баллов при поступлении за 2020-2024 гг.", fontsize=14)
# plt.xlabel("Общая сумма баллов")
# plt.ylabel("Количество абитуриентов")
# plt.show()

# ave_faculty_score = (
#     campaign_data.groupby("faculty_short_name")["admission_score"]
#     .mean()
#     .sort_values()
#     .reset_index() 
# )
# plt.figure(figsize=(10, 6))
# sns.barplot(data=ave_faculty_score, x="faculty_short_name", y="admission_score", palette="Set2")
# plt.ylim(300, 340)
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.title("Рейтиг факультетов по среднему баллу при поступлении")
# plt.ylabel("Общая сумма баллов")
# plt.xlabel("")
# plt.show()

# plt.figure(figsize=(10, 6))
# year_counts = campaign_data["admission_year"].value_counts().sort_index()
# sns.barplot(x=year_counts.index.astype(str), y=year_counts.values, color="green", alpha=0.7)
# plt.title("Количество абитуриентов в 2020-2024 годах")
# plt.xlabel("Год")
# plt.ylabel("Количество абитуриентов")
# plt.show()

# year_data = campaign_data[campaign_data["admission_year"] == 2021]
# faculty_year_counts = (
#     year_data.groupby(["faculty_short_name", "admission_year"])
#     .size()
#     .sort_values()
#     .reset_index(name="count")
# )
# plt.figure(figsize=(10, 6))
# sns.barplot(
#     data=faculty_year_counts,
#     x="faculty_short_name",
#     y="count",
#     palette="crest"
# )
# plt.ylabel("Количество поступивших абитуриентов")
# plt.xlabel("")
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# pivot = campaign_data.pivot_table(
#     index="faculty_short_name",
#     columns="admission_year",
#     values="admission_score",
#     aggfunc="mean"
# )
# plt.figure(figsize=(10, 6))
# sns.heatmap(pivot, annot=True, fmt=".1f", cmap="crest")
# plt.title("Динамика среднего проходного балла по факультетам")
# plt.xlabel("Год")
# plt.ylabel("")
# plt.tight_layout()
# plt.show()

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Итоги приёмной кампании БГУ за 2020-2024 год", fontsize=16, weight='bold')

ave_certificate_score = campaign_data.groupby("admission_year")["certificate_score"].mean().sort_index()
axes[0,0].plot(ave_certificate_score.index.astype("str"), ave_certificate_score.values, marker='o', c='teal', lw=2)
axes[0,0].set_title("Средний балл аттестата")
axes[0,0].set_xlabel("Год")
axes[0,0].grid(alpha=0.5)

sns.histplot(campaign_data["admission_score"], bins=25, color="skyblue", ax=axes[0,1])
axes[0,1].set_title("Распределение суммы баллов")
axes[0,1].set_xlabel("")
axes[0,1].set_ylabel("")

ave_faculty_score = (
    campaign_data.groupby("faculty_short_name")["admission_score"]
    .mean().sort_values(ascending=False).reset_index()
)
sns.barplot(data=ave_faculty_score, y="faculty_short_name", x="admission_score", palette="Set2", ax=axes[0,2], orient='h')
axes[0,2].set_title("Средний балл по факультетам")
axes[0,2].set_xlim(300, 330)
axes[0,2].set_xlabel("")
axes[0,2].set_ylabel("")

year_counts = campaign_data["admission_year"].value_counts().sort_index()
sns.barplot(x=year_counts.index.astype(str), y=year_counts.values, color="green", alpha=0.7, ax=axes[1,0])
axes[1,0].set_ylim(1750, 2100)
axes[1,0].set_title("Количество абитуриентов по годам")
axes[1,0].set_xlabel("")

year_data = campaign_data[campaign_data["admission_year"] == 2021]
faculty_year_counts = year_data.groupby("faculty_short_name").size().reset_index(name="count")
sns.barplot(data=faculty_year_counts, y="faculty_short_name", x="count", palette="crest", ax=axes[1,1], orient='h')
axes[1,1].set_title("2021 год: поступившие по факультетам")
axes[1,1].set_ylabel("")
axes[1,1].set_xlabel("Количество поступивших абитуриентов")

pivot = campaign_data.pivot_table(
    index="faculty_short_name",
    columns="admission_year",
    values="admission_score",
    aggfunc="mean"
)
sns.heatmap(pivot, annot=False, cmap="crest", ax=axes[1,2])
axes[1,2].set_title("Средний балл по годам и факультетам")
axes[1,2].set_ylabel("")
axes[1,2].set_xlabel("")

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()


