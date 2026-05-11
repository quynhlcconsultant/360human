"""
L1: Astrology computation via astrology-api.io (v3)
Gọi tất cả 5 hệ thống song song bằng asyncio.gather()

API base: https://api.astrology-api.io
Auth: Bearer {API_KEY}
"""

import asyncio
from datetime import date

import httpx

from app.core.config import settings


class AstrologyService:
    def __init__(self):
        self.base_url = settings.ASTROLOGY_API_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {settings.ASTROLOGY_API_KEY}",
            "Content-Type": "application/json",
        }

    async def _post(self, client: httpx.AsyncClient, path: str, body: dict) -> dict:
        try:
            resp = await client.post(
                f"{self.base_url}{path}",
                json=body,
                headers=self.headers,
                timeout=30.0,
            )
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            return {"error": str(e), "status_code": e.response.status_code, "system": path}
        except httpx.HTTPError as e:
            return {"error": str(e), "system": path}

    def _build_birth_data(
        self,
        birth_date: date,
        birth_time: str | None,
        birth_lat: str | None,
        birth_lon: str | None,
        birth_timezone: str | None,
        full_name: str | None = None,
        gender: str | None = None,
        use_lat_lon: bool = True,  # False = use latitude/longitude
    ) -> dict:
        hour, minute = 12, 0
        if birth_time:
            try:
                parts = birth_time.split(":")
                hour = int(parts[0])
                minute = int(parts[1])
            except (ValueError, IndexError):
                pass

        bd: dict = {
            "year": birth_date.year,
            "month": birth_date.month,
            "day": birth_date.day,
            "hour": hour,
            "minute": minute,
        }
        if use_lat_lon:
            if birth_lat:
                bd["lat"] = float(birth_lat)
            if birth_lon:
                bd["lon"] = float(birth_lon)
        else:
            if birth_lat:
                bd["latitude"] = float(birth_lat)
            if birth_lon:
                bd["longitude"] = float(birth_lon)

        if birth_timezone:
            bd["timezone"] = birth_timezone
        if full_name:
            bd["name"] = full_name
        if gender:
            bd["gender"] = gender

        return bd

    async def compute_all(
        self,
        birth_date: date,
        birth_time: str | None,
        birth_lat: str | None,
        birth_lon: str | None,
        birth_timezone: str | None,
        full_name: str,
        gender: str | None,
    ) -> dict:
        """Gọi cả 5 hệ thống song song qua astrology-api.io v3, trả về dict raw data."""

        # Zi Wei: {birth_data: {..., lat, lon}, gender at root}
        bd_lat_lon = self._build_birth_data(
            birth_date, birth_time, birth_lat, birth_lon, birth_timezone,
            full_name=full_name, gender=None, use_lat_lon=True
        )
        ziwei_body = {"birth_data": bd_lat_lon, "gender": gender or "male"}

        # BaZi, Numerology: {subject: {birth_data: {..., lat, lon, gender}}}
        bd_lat_lon_full = self._build_birth_data(
            birth_date, birth_time, birth_lat, birth_lon, birth_timezone,
            full_name=full_name, gender=gender, use_lat_lon=True
        )
        subject_lat_lon = {"subject": {"birth_data": bd_lat_lon_full}}

        # Human Design, Vedic: {subject: {birth_data: {..., latitude, longitude, gender}}}
        bd_lat_long_full = self._build_birth_data(
            birth_date, birth_time, birth_lat, birth_lon, birth_timezone,
            full_name=full_name, gender=gender, use_lat_lon=False
        )
        subject_lat_long = {"subject": {"birth_data": bd_lat_long_full}}

        async with httpx.AsyncClient() as client:
            results = await asyncio.gather(
                self._post(client, "/api/v3/ziwei/chart", ziwei_body),
                self._post(client, "/api/v3/chinese/bazi", subject_lat_lon),
                self._post(client, "/api/v3/human-design/bodygraph", subject_lat_long),
                self._post(client, "/api/v3/vedic/birth-details", subject_lat_long),
                self._post(client, "/api/v3/numerology/comprehensive", subject_lat_lon),
                return_exceptions=False,
            )

        return {
            "zi_wei": results[0],
            "bazi": results[1],
            "human_design": results[2],
            "vedic": results[3],
            "numerology": results[4],
        }


astrology_service = AstrologyService()
