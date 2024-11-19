from pydantic import BaseModel, Field
from typing import List, Optional

class ExternalUrl(BaseModel):
    spotify: str

class Artist(BaseModel):
    external_urls: ExternalUrl
    href: str
    id: str
    name: str
    type: str
    uri: str

class Track(BaseModel):
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrl
    href: str
    id: str
    name: str
    preview_url: Optional[str]
    track_number: int
    type: str
    uri: str
    is_local: bool

class SpotifyData(BaseModel):
    href: str
    items: List[Track]

    @classmethod
    def from_json(cls, json_data: dict) -> 'SpotifyData':
        return cls.parse_obj(json_data)

    def to_json(self) -> dict:
        return self.dict()
