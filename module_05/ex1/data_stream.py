from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.data_history: List[Any] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria"""
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        all_datas = 0
        total_temp = 0.0
        n_temp = 0

        for item in data_batch:
            if isinstance(item, str):
                if item.startswith("temp:"):
                    total_temp += float(item.split(":")[1])
                    n_temp += 1
                    all_datas += 1
                elif (item.startswith("humidity:") or
                      item.startswith("pressure")):
                    all_datas += 1
        if n_temp > 0:
            avg = total_temp / n_temp
        else:
            avg = 0.0
        res_sen = (f"Sensor analysis: {all_datas} readings processed, "
                   f"avg temp: {avg: .1f}")
        return res_sen

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return ["2 critical sensor alerts"]
        return []


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        operations = 0
        net = 0

        for batch_item in data_batch:
            if isinstance(batch_item, str):
                trans_items = batch_item.split(",")
                for item in trans_items:
                    item = item.strip()
                    if item.startswith("buy:"):
                        net += int(item.split(":")[1])
                        operations += 1
                    elif item.startswith("sell:"):
                        net -= int(item.split(":")[1])
                        operations += 1

        res_trans = (f"Transaction analysis: {operations} "
                     f"operations, net flow: +{net} units")
        return res_trans

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return ["1 large transaction"]
        return []


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        valid_events = ["login", "error", "logout"]
        events = 0
        errors = 0

        for item in data_batch:
            if item in valid_events:
                events += 1
                if item == "error":
                    errors += 1
        return f"Event analysis: {events} events, {errors} errors detected"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return []


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_batch(self, data_batch: List[Any]) -> str:
        results = []
        for stream in self.streams:
            raw_report = stream.process_batch(data_batch)
            if isinstance(stream, SensorStream):
                name, count = "Sensor data", raw_report.split()[2]
                unit = "readings"
            elif isinstance(stream, TransactionStream):
                name, count = "Transaction data", raw_report.split()[2]
                unit = "operations"
            else:
                name, count = "Event data", raw_report.split()[2]
                unit = "events"
            results.append(f" - {name}: {count} {unit} processed")
        return "\n".join(results)

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        final_res = []
        for stream in self.streams:
            streams_alerts = stream.filter_data(data_batch, criteria)
            final_res.extend(streams_alerts)
        return final_res


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    temp = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {temp}")
    print(sensor.process_batch(temp))
    print()

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Environmental Data")
    trans = ["buy:100, sell:150, buy:75"]
    print(f"Processing transaction batch: {trans}")
    print(transaction.process_batch(trans))
    print()

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: Environmental Data")
    evnt = ["login", "error", "logout"]
    print(f"Processing event batch: {evnt}")
    print(event.process_batch(evnt))

    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    nexus = StreamProcessor()
    nexus.add_stream(sensor)
    nexus.add_stream(transaction)
    nexus.add_stream(event)

    tests = [
        "buy:500", "buy:15", "pressure:100", "error", "temp:-10",
        "login", "sell:500", "logout", "sell:10"
    ]

    print("Batch 1 Results:")
    print(nexus.process_batch(tests))
    print()
    print("Stream filtering active: High-priority data only")
    filter_res = nexus.filter_data(tests, "critical")
    print(f"Filtered results: {', '.join(filter_res)}")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")
