labellings = hac.fcluster(ward_data, t=25, criterion='distance')
silhouette_score(scaled_df, labellings)
