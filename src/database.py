import psycopg2
import os

def get_connection():
    db_conn = os.getenv("SUPABASE_URL")
    if not db_conn:
        raise Exception("SUPABASE_URL not found in environment variables")
    return psycopg2.connect(db_conn)

def insert_weather_data(weather_data):
    with get_connection() as conn:
        with conn.cursor() as cur:
            for record in weather_data.get('list', []):
                # Extract values, handling missing keys
                dt = record.get('dt', 0)
                temp = int(record.get('main', {}).get('temp', 0))
                feels_like = int(record.get('main', {}).get('feels_like', 0))
                temp_max = int(record.get('main', {}).get('temp_max', 0))
                temp_min = int(record.get('main', {}).get('temp_min', 0))
                humidity = record.get('main', {}).get('humidity', 0)
                

                weather_desc = record.get('weather', [{}])[0].get('description', 'unknown')
                
                cloud_coverage = record.get('clouds', {}).get('all', 0)
                wind_speed = int(record.get('wind', {}).get('speed', 0))
                wind_gusts = int(record.get('wind', {}).get('gust', 0))
                wind_direction = str(record.get('wind', {}).get('deg', 0))
                
                # Rain data might not always be present
                rain_upcoming = str(record.get('rain', {}).get('3h', '0'))
                
                cur.execute('''
                    INSERT INTO weather_data
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                        ON CONFLICT (date_time)
                        DO UPDATE SET
                            temperature = EXCLUDED.temperature,
                            feels_like = EXCLUDED.feels_like,
                            temp_max = EXCLUDED.temp_max,
                            temp_min = EXCLUDED.temp_min,
                            humidity = EXCLUDED.humidity,
                            weather_description = EXCLUDED.weather_description,
                            cloud_coverage = EXCLUDED.cloud_coverage,
                            wind_speed = EXCLUDED.wind_speed,
                            wind_gusts = EXCLUDED.wind_gusts,
                            wind_direction = EXCLUDED.wind_direction,
                            rain_upcoming = EXCLUDED.rain_upcoming,
                            last_updated = NOW()
                ''', (dt, temp, feels_like, temp_max, temp_min, humidity, 
                      weather_desc, cloud_coverage, wind_speed, wind_gusts, 
                      wind_direction, rain_upcoming))
        conn.commit()