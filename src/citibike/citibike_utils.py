from pyspark.sql.functions import unix_timestamp, col, to_timestamp

def get_trip_duration_min(spark, df, start_col, end_col, output_col):

    """
    function to calculate the duration of a trip in minutes

    """
    start_ts = to_timestamp(col(start_col))   # or specify format, see below
    end_ts   = to_timestamp(col(end_col))
    return df.withColumn(output_col, unix_timestamp(col(end_col)) - unix_timestamp(col(start_col)) / 60
                         )