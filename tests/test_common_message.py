from common.message import Message
from common.router_api import EpidemicRouter


def test_message_creation_and_serialization():
    msg = Message(
        id="test-msg-123",
        kind="SOS",
        priority=1,
        lat=13.0827,
        lon=80.2707,
        created_at=100.0,
        ttl=300,
        sender="node_alpha",
        payload="medical, 2 people trapped"
    )
    
    # Test JSON serialization & deserialization roundtrip
    json_str = msg.to_json()
    reconstructed = Message.from_json(json_str)
    
    assert reconstructed.id == msg.id
    assert reconstructed.priority == 1
    assert reconstructed.kind == "SOS"
    assert reconstructed.payload == "medical, 2 people trapped"
    assert reconstructed.signature == ""


def test_message_signing_bytes():
    msg1 = Message("id1", "SOS", 1, 10.0, 70.0, 0.0, 100, "node1", "help", signature="")
    msg2 = Message("id1", "SOS", 1, 10.0, 70.0, 0.0, 100, "node1", "help", signature="sample_sig")
    
    # signing_bytes must ignore the signature field so it can be verified
    assert msg1.signing_bytes() == msg2.signing_bytes()


def test_epidemic_router_selection():
    class MockNode:
        def __init__(self, nid, seen_ids=None):
            self.id = nid
            self.seen = seen_ids if seen_ids is not None else set()

    router = EpidemicRouter()
    sender = MockNode("node_0")
    nb1 = MockNode("node_1", seen_ids=set())
    nb2 = MockNode("node_2", seen_ids={"msg_01"})
    nb3 = MockNode("node_3", seen_ids=set())

    msg = Message("msg_01", "STATUS", 3, 0.0, 0.0, 0.0, 100, "node_0", "safe")
    
    # nb2 has already seen msg_01, so router should only return nb1 and nb3
    next_hops = router.select_next_hops(sender, msg, [nb1, nb2, nb3], now=10.0)
    assert next_hops == [nb1, nb3]
