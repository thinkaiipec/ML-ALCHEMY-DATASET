np.random.seed(42)

days = np.random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], size=200)
temperature = np.random.randint(low=-10, high=35, size=200)
windspeed = np.random.randint(low=0, high=30, size=200)
events = np.random.choice(['Sunny', 'Rainy', 'Cloudy', 'Windy'], size=200)

data = {
    'Day': days,
    'Temperature': temperature,
    'WindSpeed': windspeed,
    'Event': events
}
df = pd.DataFrame(data)

df.loc[np.random.choice(df.index, size=20, replace=False), 'Temperature'] = np.nan
df.loc[np.random.choice(df.index, size=15, replace=False), 'WindSpeed'] = np.nan
# df.loc[np.random.choice(df.index, size=10, replace=False), 'Event'] = np.nan

df.to_csv('weather_data.csv', index=False)
