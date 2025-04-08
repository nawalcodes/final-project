# main.py
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from models import Base, SmartLocation
import geojson

# Database connection string, adjust user, password, and host as needed.
DATABASE_URL = "postgresql://nawalnaz:kahanahmed@localhost/sld"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Uncomment if you need to create the tables (if not already imported)
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Location API")

@app.get("/map_data")
def get_map_data():
    session = SessionLocal()
    try:
        data = session.query(SmartLocation).limit(1000).all()  # limit for performance
        features = []
        for row in data:
            geom = to_shape(row.shape)
            geo = mapping(geom)
            feature = geojson.Feature(
                geometry=geo,
                properties={"objectid": row.objectid}
            )
            features.append(feature)

        return geojson.FeatureCollection(features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
