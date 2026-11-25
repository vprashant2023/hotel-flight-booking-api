from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Elsewhere Travel API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CITIES = [
    {"code": "DEL", "name": "Delhi", "region": "North India", "airport": "Indira Gandhi International"},
    {"code": "BOM", "name": "Mumbai", "region": "West India", "airport": "Chhatrapati Shivaji Maharaj International"},
    {"code": "BLR", "name": "Bengaluru", "region": "South India", "airport": "Kempegowda International"},
    {"code": "HYD", "name": "Hyderabad", "region": "South India", "airport": "Rajiv Gandhi International"},
    {"code": "MAA", "name": "Chennai", "region": "South India", "airport": "Chennai International"},
    {"code": "CCU", "name": "Kolkata", "region": "East India", "airport": "Netaji Subhas Chandra Bose International"},
    {"code": "JAI", "name": "Jaipur", "region": "Rajasthan", "airport": "Jaipur International"},
    {"code": "GOI", "name": "Goa", "region": "West India", "airport": "Manohar International"},
    {"code": "COK", "name": "Kochi", "region": "Kerala", "airport": "Cochin International"},
    {"code": "VNS", "name": "Varanasi", "region": "Uttar Pradesh", "airport": "Lal Bahadur Shastri International"},
]

FLIGHTS = [
    {"id": "ai-2431", "airline": "Air India", "flight_number": "AI 2431", "origin": "DEL", "destination": "GOI", "departure_time": "07:10", "arrival_time": "09:45", "duration": "2h 35m", "stops": 0, "price": 5890},
    {"id": "6e-5214", "airline": "IndiGo", "flight_number": "6E 5214", "origin": "DEL", "destination": "GOI", "departure_time": "10:25", "arrival_time": "13:00", "duration": "2h 35m", "stops": 0, "price": 6240},
    {"id": "uk-995", "airline": "Vistara", "flight_number": "UK 995", "origin": "DEL", "destination": "BOM", "departure_time": "08:00", "arrival_time": "10:10", "duration": "2h 10m", "stops": 0, "price": 4890},
    {"id": "6e-2131", "airline": "IndiGo", "flight_number": "6E 2131", "origin": "DEL", "destination": "JAI", "departure_time": "06:40", "arrival_time": "07:35", "duration": "55m", "stops": 0, "price": 2850},
    {"id": "ai-839", "airline": "Air India", "flight_number": "AI 839", "origin": "DEL", "destination": "COK", "departure_time": "09:15", "arrival_time": "12:25", "duration": "3h 10m", "stops": 0, "price": 7340},
    {"id": "6e-223", "airline": "IndiGo", "flight_number": "6E 223", "origin": "DEL", "destination": "VNS", "departure_time": "11:30", "arrival_time": "12:55", "duration": "1h 25m", "stops": 0, "price": 3590},
    {"id": "ai-503", "airline": "Air India", "flight_number": "AI 503", "origin": "DEL", "destination": "BLR", "departure_time": "07:35", "arrival_time": "10:25", "duration": "2h 50m", "stops": 0, "price": 6790},
    {"id": "6e-2246", "airline": "IndiGo", "flight_number": "6E 2246", "origin": "DEL", "destination": "HYD", "departure_time": "12:10", "arrival_time": "14:20", "duration": "2h 10m", "stops": 0, "price": 5980},
    {"id": "ai-440", "airline": "Air India", "flight_number": "AI 440", "origin": "DEL", "destination": "MAA", "departure_time": "08:20", "arrival_time": "11:15", "duration": "2h 55m", "stops": 0, "price": 7120},
    {"id": "6e-2789", "airline": "IndiGo", "flight_number": "6E 2789", "origin": "DEL", "destination": "CCU", "departure_time": "09:50", "arrival_time": "12:10", "duration": "2h 20m", "stops": 0, "price": 6340},
    {"id": "ai-506", "airline": "Air India", "flight_number": "AI 506", "origin": "BOM", "destination": "BLR", "departure_time": "07:50", "arrival_time": "09:25", "duration": "1h 35m", "stops": 0, "price": 4120},
    {"id": "6e-697", "airline": "IndiGo", "flight_number": "6E 697", "origin": "BOM", "destination": "GOI", "departure_time": "12:15", "arrival_time": "13:30", "duration": "1h 15m", "stops": 0, "price": 3290},
    {"id": "uk-847", "airline": "Vistara", "flight_number": "UK 847", "origin": "BOM", "destination": "HYD", "departure_time": "16:20", "arrival_time": "17:50", "duration": "1h 30m", "stops": 0, "price": 3980},
    {"id": "6e-6223", "airline": "IndiGo", "flight_number": "6E 6223", "origin": "BLR", "destination": "COK", "departure_time": "08:40", "arrival_time": "09:50", "duration": "1h 10m", "stops": 0, "price": 2980},
    {"id": "ai-564", "airline": "Air India", "flight_number": "AI 564", "origin": "BLR", "destination": "MAA", "departure_time": "10:05", "arrival_time": "11:10", "duration": "1h 5m", "stops": 0, "price": 3150},
    {"id": "6e-6324", "airline": "IndiGo", "flight_number": "6E 6324", "origin": "BLR", "destination": "HYD", "departure_time": "13:15", "arrival_time": "14:25", "duration": "1h 10m", "stops": 0, "price": 3270},
    {"id": "ai-951", "airline": "Air India", "flight_number": "AI 951", "origin": "HYD", "destination": "GOI", "departure_time": "14:00", "arrival_time": "15:25", "duration": "1h 25m", "stops": 0, "price": 3790},
    {"id": "6e-621", "airline": "IndiGo", "flight_number": "6E 621", "origin": "MAA", "destination": "CCU", "departure_time": "06:55", "arrival_time": "09:10", "duration": "2h 15m", "stops": 0, "price": 4780},
    {"id": "ai-763", "airline": "Air India", "flight_number": "AI 763", "origin": "CCU", "destination": "VNS", "departure_time": "15:35", "arrival_time": "16:50", "duration": "1h 15m", "stops": 0, "price": 3690},
    {"id": "6e-744", "airline": "IndiGo", "flight_number": "6E 744", "origin": "JAI", "destination": "BOM", "departure_time": "17:10", "arrival_time": "19:00", "duration": "1h 50m", "stops": 0, "price": 4490},
    {"id": "ai-426", "airline": "Air India", "flight_number": "AI 426", "origin": "COK", "destination": "BOM", "departure_time": "18:25", "arrival_time": "20:20", "duration": "1h 55m", "stops": 0, "price": 4720},
]

HOTELS = {
    "GOI": [
        {"id": "goa-01", "name": "Casa Solana", "neighborhood": "Candolim · North Goa", "category": "Beachside", "rating": 4.8, "price_per_night": 6800, "image_url": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=85"},
        {"id": "goa-02", "name": "The Palm House", "neighborhood": "Assagao · North Goa", "category": "Boutique stay", "rating": 4.7, "price_per_night": 9200, "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=900&q=85"},
        {"id": "goa-03", "name": "Susegad by the Sea", "neighborhood": "Palolem · South Goa", "category": "Quiet escape", "rating": 4.9, "price_per_night": 7400, "image_url": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=900&q=85"},
    ],
    "JAI": [
        {"id": "jai-01", "name": "Haveli Gulab", "neighborhood": "Civil Lines · Jaipur", "category": "Heritage stay", "rating": 4.8, "price_per_night": 5900, "image_url": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?auto=format&fit=crop&w=900&q=85"},
        {"id": "jai-02", "name": "The Amber Courtyard", "neighborhood": "Amer · Jaipur", "category": "Courtyard hotel", "rating": 4.7, "price_per_night": 8200, "image_url": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=85"},
    ],
    "COK": [
        {"id": "cok-01", "name": "Tide & Timber", "neighborhood": "Fort Kochi · Kerala", "category": "Heritage stay", "rating": 4.8, "price_per_night": 6300, "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=900&q=85"},
        {"id": "cok-02", "name": "Backwater House", "neighborhood": "Mattancherry · Kochi", "category": "Waterfront", "rating": 4.6, "price_per_night": 7100, "image_url": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=85"},
    ],
    "DEL": [
        {"id": "del-01", "name": "The Neem Courtyard", "neighborhood": "Hauz Khas · New Delhi", "category": "Boutique stay", "rating": 4.7, "price_per_night": 7800, "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=900&q=85"},
        {"id": "del-02", "name": "Garden House", "neighborhood": "Mehrauli · New Delhi", "category": "Quiet escape", "rating": 4.8, "price_per_night": 9400, "image_url": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=85"},
    ],
    "BOM": [
        {"id": "bom-01", "name": "Sea Glass House", "neighborhood": "Bandra West · Mumbai", "category": "City retreat", "rating": 4.6, "price_per_night": 8900, "image_url": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=85"},
        {"id": "bom-02", "name": "The Old Quarter", "neighborhood": "Colaba · Mumbai", "category": "Heritage stay", "rating": 4.7, "price_per_night": 11200, "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=900&q=85"},
    ],
    "BLR": [
        {"id": "blr-01", "name": "Mango & Mint", "neighborhood": "Indiranagar · Bengaluru", "category": "Garden stay", "rating": 4.7, "price_per_night": 6500, "image_url": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=85"},
        {"id": "blr-02", "name": "The Canopy", "neighborhood": "Koramangala · Bengaluru", "category": "City retreat", "rating": 4.6, "price_per_night": 7200, "image_url": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?auto=format&fit=crop&w=900&q=85"},
    ],
    "HYD": [
        {"id": "hyd-01", "name": "Deccan House", "neighborhood": "Banjara Hills · Hyderabad", "category": "Boutique stay", "rating": 4.7, "price_per_night": 7100, "image_url": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=85"},
    ],
    "MAA": [
        {"id": "maa-01", "name": "Coral Tree House", "neighborhood": "Alwarpet · Chennai", "category": "Garden stay", "rating": 4.6, "price_per_night": 6200, "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=900&q=85"},
    ],
    "CCU": [
        {"id": "ccu-01", "name": "The Calcutta Room", "neighborhood": "Park Street · Kolkata", "category": "Heritage stay", "rating": 4.8, "price_per_night": 5800, "image_url": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=900&q=85"},
    ],
    "VNS": [
        {"id": "vns-01", "name": "Ganga Vista", "neighborhood": "Assi Ghat · Varanasi", "category": "Riverside", "rating": 4.7, "price_per_night": 4900, "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Varanasi_panorama.jpg?width=900"},
    ],
}


@app.get("/api/health")
def health():
    return {"status": "ok", "database": None}


@app.get("/api/cities")
def list_cities():
    return CITIES


@app.get("/api/flights")
def list_flights(
    origin: str = Query(min_length=3, max_length=3),
    destination: str = Query(min_length=3, max_length=3),
    date: str | None = None,
):
    origin_code = origin.upper()
    destination_code = destination.upper()
    city_codes = {city["code"] for city in CITIES}
    if origin_code not in city_codes or destination_code not in city_codes:
        raise HTTPException(status_code=404, detail="Unknown city code")
    return [
        {**flight, "date": date}
        for flight in FLIGHTS
        if flight["origin"] == origin_code and flight["destination"] == destination_code
    ]


@app.get("/api/hotels")
def list_hotels(city: str = Query(min_length=3, max_length=3)):
    city_code = city.upper()
    if city_code not in {item["code"] for item in CITIES}:
        raise HTTPException(status_code=404, detail="Unknown city code")
    return HOTELS.get(city_code, [])