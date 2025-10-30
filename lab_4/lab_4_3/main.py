import pandas as pd
import matplotlib.pyplot as plt

campaign_data = pd.read_csv("entrance_campaign.csv")

average_admission_scores = (
    campaign_data.groupby("admission_year")["admission_score"]
    .mean()
    .round(1)
    .sort_index()
)
plt.figure(figsize=(10, 6))
plt.plot(average_admission_scores.index.astype(str), average_admission_scores.values, c="green", alpha=0.7, marker="o", linewidth=3)
plt.xlabel("Год поступления", fontsize=12)
plt.ylabel("Средняя сумма баллов", fontsize=12)
plt.title("Динамика средней суммы баллов при поступлении абитуриентов в БГУ за 2020-2024 гг.", fontsize=14, pad=15)
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

average_certificate_scores = (
    campaign_data.groupby("admission_year")["certificate_score"]
    .mean()
    .round(2)
    .sort_index()
)
plt.figure(figsize=(8, 6))
plt.plot(average_certificate_scores.index.astype(str), average_certificate_scores.values, c="orange", alpha=0.7, marker="o", linewidth=2.5)
plt.xlabel("Год поступления", fontsize=12)
plt.ylabel("Средний балл аттестата", fontsize=12)
plt.title("Динамика среднего балла аттестата абитуриентов БГУ (2020–2024 гг.)", fontsize=14, pad=15)
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()