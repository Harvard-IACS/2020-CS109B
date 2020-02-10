ms_kmeans = KMeans(n_clusters=4, init='random', n_init=3, random_state=109).fit(scaled_df)
plt.figure(figsize=(10,10))
plt.scatter(scaled_df['x'], scaled_df['y'], c=ms_kmeans.labels_);
plt.scatter(ms_kmeans.cluster_centers_[:,0],ms_kmeans.cluster_centers_[:,1], c='r', marker='h', s=100);

# plot a fancy silhouette plot
silplot(scaled_df.values, ms_kmeans)
