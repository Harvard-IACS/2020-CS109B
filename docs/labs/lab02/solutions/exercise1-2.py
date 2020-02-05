ax2 = diab.plot.scatter(x='age',y='y',c='Red',title="Diabetes data with least-squares cubic fit")
ax2.set_xlabel("Age at Diagnosis")
ax2.set_ylabel("Log C-Peptide Concentration")

ax2.plot(predict_df.age, poly_predictions['mean'],color="green")
ax2.plot(predict_df.age, poly_predictions['mean_ci_lower'], color="blue",linestyle="dashed")
ax2.plot(predict_df.age, poly_predictions['mean_ci_upper'], color="blue",linestyle="dashed");

ax2.plot(predict_df.age, poly_predictions['obs_ci_lower'], color="skyblue",linestyle="dashed")
ax2.plot(predict_df.age, poly_predictions['obs_ci_upper'], color="skyblue",linestyle="dashed");
