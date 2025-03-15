FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY browse_shp.py /app/browse_shp.py

ENTRYPOINT [ "python3", "/app/browse_shp.py" ]