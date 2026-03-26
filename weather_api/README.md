# Weather API Wrapper

A FastAPI service that wraps the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api), with Redis caching and rate limiting.

## Features

- Fetches current weather data by city name
- Caches responses in Redis for 12 hours to reduce upstream API calls
- Rate limited to 10 requests per minute per IP
- Input normalisation (case-insensitive, whitespace-tolerant)

## Requirements

- Python 3.10+
- Docker (for Redis)

## Setup

**1. Clone the repo and install dependencies**

```bash
pip install fastapi uvicorn httpx redis python-dotenv slowapi
```

**2. Start Redis**

```bash
docker run -d -p 6379:6379 --name redis redis
```

**3. Configure environment variables**

Create a `.env` file in the project root:

```
WEATHER_API_KEY=your_visual_crossing_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
```

You can get a free API key from [Visual Crossing](https://www.visualcrossing.com/weather-api).

**4. Run the server**

```bash
uvicorn app.weather:app --reload
```

The API will be available at `http://localhost:8000`.

## Endpoints

### `GET /weather/{city}`

Returns current weather data for the given city.

**Example:**

```
GET /weather/istanbul
```

**Response:** JSON weather data from Visual Crossing, including current conditions such as temperature, humidity, wind speed, and more.

**Errors:**

| Status | Reason |
|--------|--------|
| `400` | Rate limit exceeded |
| `404` | City not found |
| `502` | Upstream weather API error |

## Caching

Responses are cached in Redis using the city name as the key (`weather:{city}`) with a 12-hour TTL. Repeated requests for the same city within that window are served from cache without hitting the upstream API.

## Rate Limiting

Requests are limited to **10 per minute per IP address**. Exceeding this returns a `429 Too Many Requests` response.