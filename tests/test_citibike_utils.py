
from src.citibike.citibike_utils import get_trip_duration_min

def test_get_trip_duration_min(spark):
    data = [
        {"start_time": "2023-01-01 08:00:00", "end_time": "2023-01-01 08:30:00"},
        {"start_time": "2023-01-01 09:15:00", "end_time": "2023-01-01 09:45:00"},
    ]
    df = spark.createDataFrame(data)
    result_df = get_trip_duration_min(spark, df, "start_time", "end_time", "trip_duration_min")
    results = result_df.select("trip_duration_min").collect()
    assert results[0]["trip_duration_min"] == 1644685800.0
    assert results[1]["trip_duration_min"] == 1644690225.0
