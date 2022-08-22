CREATE TABLE if not exists WEATHER_DATA
(region VARCHAR2(50),
record_date DATE,
min_temp NUMBER,
max_temp NUMBER,
amount NUMBER,
CONSTRAINT UC_row UNIQUE (region, record_date)
);

CREATE TABLE if not exists  YIELD
(region VARCHAR2(50),
year VARCHAR2(4),
amount NUMBER,
CONSTRAINT UC_row UNIQUE (region, year)
);

CREATE TABLE if not exists  WEATHER_DATA_MATRICS
(region VARCHAR2(50),
year VARCHAR2(4),
avg_min_temp NUMBER,
avg_max_temp NUMBER,
total_amount NUMBER,
CONSTRAINT UC_row UNIQUE (region, year)
);
