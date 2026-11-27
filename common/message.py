import json
from dataclasses import dataclass, asdict


@dataclass
class Message:
    """Canonical message packet passed across the StormNet mesh.
    
    Attributes:
        id: Unique identifier (UUID4 string).
        kind: Message category, e.g., 'SOS', 'STATUS', 'ACK'.
        priority: Priority rank where 1 = highest/critical (e.g. medical, trapped),
                  up to 5 = lowest/comfort (e.g. social updates).
        lat: Latitude of origin or event.
        lon: Longitude of origin or event.
        created_at: Creation timestamp in simulation/epoch seconds.
        ttl: Time-To-Live in seconds; message expires and drops when expired.
        sender: Originating node identifier.
        payload: Short description or telemetry (kept tiny, ~100 bytes).
        signature: Hex-encoded digital signature populated by Module 4.
    """
    id: str
    kind: str
    priority: int
    lat: float
    lon: float
    created_at: float
    ttl: int
    sender: str
    payload: str = ""
    signature: str = ""

    def signing_bytes(self) -> bytes:
        """Serializes the message payload for cryptographic signing, omitting signature."""
        d = asdict(self)
        d.pop("signature", None)
        return json.dumps(d, sort_keys=True).encode()

    def to_json(self) -> str:
        """Serializes the complete message including signature to a JSON string."""
        return json.dumps(asdict(self))

    @staticmethod
    def from_json(s: str) -> "Message":
        """Deserializes a JSON string into a Message instance."""
        return Message(**json.loads(s))
